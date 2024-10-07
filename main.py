from CreatePDF import CreatePDF
from Assistant import LlamaConfig
from fastapi import FastAPI, HTTPException, File, UploadFile
from fastapi.responses import FileResponse
import shutil
import os 

app = FastAPI()


@app.post("/assistant-ai")
async def root(File: UploadFile):
    try:
        diretorio = "files"

        try:
            shutil.rmtree(diretorio)
        except OSError as e:
            # Informe o usuário sobre quaisquer erros
            print(f"Erro: {e.filename} - {e.strerror}")
        
        if not os.path.exists(diretorio):
            os.makedirs(diretorio)
            print(f"Pasta '{diretorio}' criada com sucesso.")
        else:
            print(f"Pasta '{diretorio}' já existe.")

    
        filename = File.filename
        print('nome arquivo:', filename)

        caminho_arquivo = os.path.join(diretorio, filename)

        with open(caminho_arquivo, "wb") as arquivo:
            # Escreve o conteúdo do arquivo enviado
            arquivo.write(File.file.read())

        response = LlamaConfig.trancribe_textAI(caminho_arquivo)

        text = LlamaConfig.call_AI(response)

        response = CreatePDF.create_doc_pdf(text, filename)

        return FileResponse(response, media_type="application/pdf", filename=f"{filename}.pdf")

    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro interno do servidor: {str(e)}")
    


