import os
from openai import OpenAI

client = OpenAI( )

def responder(pergunta):
    resposta = client.responses.create(
        model="gpt-4o-mini",
        input=[
            {"role": "system", "content": "Você é um assistente do CRA UNINASSAU João Pessoa."},
            {"role": "user", "content": pergunta}
        ]
    )
    return resposta.output_text
