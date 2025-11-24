import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def responder(pergunta):
    resposta = client.responses.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Você é um assistente do CRA UNINASSAU João Pessoa."},
            {"role": "user", "content": pergunta}
        ]
    )
    return resposta.output_text
