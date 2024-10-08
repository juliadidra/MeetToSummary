## Instruções:

- instale o ambiente virtual: `py -m venv .venv`
- ative o ambiente virtual: `.venv/Scripts/Activate`
- Instale as dependencias do projeto contidas no arquivo requirements_dev.txt: `pip install -r requirements_dev.txt` 
- crie o arquivo .env com o seguinte conteudo:
  ```  
    GROQ_API_KEY="sua api key do llama ai (consiga a sua api key em: https://console.groq.com/playground)"
    assemblyAI_key="sua api key do assemblyAI (consiga sua api key em: https://www.assemblyai.com/dashboard/signup)"
  ```
### Para rodar o projeto
- ainda dentro do ambiente virtual insira: `uvicorn main:app --reload`
- acesse: `http://localhost:8000/docs` (escolha a porta em que o fastapi esteja rodando no seu ambiente)
  
