import os
from openai import OpenAI

client = OpenAI()

def responder(pergunta):
# Instrução de Sistema
    INSTRUCAO_SISTEMA = (
        "Você é um Assistente Virtual do CRA UNINASSAU focado exclusivamente no campus de João Pessoa PB."
        "Seu único objetivo é fornecer informações corretas sobre a faculdade (CRA, cursos, etc.)."
        "REGRA CRÍTICA: Você deve RECUSAR educadamente qualquer pergunta que não esteja relacionada à UNINASSAU João Pessoa, "
        "incluindo (mas não se limitando a) outras unidades da UNINASSAU, outras faculdades ou conhecimento geral. "
        "Ao recusar, use a frase: 'Minha área de especialização é a UNINASSAU João Pessoa. Sinto muito por não ter essa informação.'"
    )
    # ----------------------------------------

def responder(pergunta):
    resposta = client.responses.create(
        model="gpt-4o-mini",
        input=[
            {"role": "system", "content": "Você é um assistente do CRA UNINASSAU João Pessoa."},
            {"role": "user", "content": pergunta}
        ]
    )
    return resposta.output_text
