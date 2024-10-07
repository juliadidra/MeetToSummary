
import os
from dotenv import load_dotenv
from groq import Groq
import assemblyai as aai

load_dotenv()

class LlamaConfig():
    def trancribe_textAI(audio):
        
        config = aai.TranscriptionConfig(language_code="pt")
        aai.settings.api_key = os.environ.get("assemblyAI_key")
        transcriber = aai.Transcriber(config=config)

        transcript = transcriber.transcribe(audio)

        print(transcript.text)
        text = transcript.text
        return text



    def call_AI(text):
        client = Groq(
        api_key=os.environ.get("GROQ_API_KEY"),
        )

        content = 'Você é um assistente que irá fazer resumos de textos, voce devera analisar o contexto do texto e destacar os pontos mais importantes dele. Vale ressaltar que o texto será a transcrição de audio de reuniões, sendo assim seu objetivo é gerar resumos que serão transformados em documentos para auxiliar o usuário'

        user_content = f"""Analise o texto abaixo, identifique os principais pontos e gere um resumo organizado da seguinte forma:

            - Crie um título ou subtítulo que capture o tema central do texto.

            - Organize o resumo em tópicos principais e subtópicos, destacando as informações mais importantes de forma clara e objetiva.

            - Use listas numeradas ou com marcadores para apresentar os pontos principais quando relevante.

            - Formate o conteúdo de maneira que seja compatível com a criação de um arquivo PDF, utilizando títulos em negrito para os tópicos principais e parágrafos curtos e concisos.

            - Finalize com um parágrafo de conclusão que resuma as ideias principais do texto.

        Esse é o texto:
            '''{text}'''

            """

        chat_completion = client.chat.completions.create(
            messages=[
        {
            "role": "system",
            "content": content
        },
        {
            "role": "user",
            "content": user_content,
        }
    ],

    model="llama3-8b-8192",
    temperature=0.5,
    max_tokens=1024,
    top_p=1,
    stop=None,
    stream=False,
        )

        print(chat_completion.choices[0].message.content)

        response = chat_completion.choices[0].message.content
    
        return response
