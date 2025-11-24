import os
from openai import OpenAI

client = OpenAI()

def responder(pergunta):
# Instrução de Sistema
   instrucao_assistente= (
    "Você é um **ASSISTENTE DE IA COM RESTRIÇÃO CRÍTICA DE CONHECIMENTO**. "
    "Sua área é **EXCLUSIVAMENTE** a **UNINASSAU campus de João Pessoa/PB**. "
    "Se o usuário perguntar sobre QUALQUER OUTRA FACULDADE ou ASSUNTO GERAL, "
    "você deve **IMEDIATAMENTE** e **SEM EXCEÇÃO** retornar APENAS a frase de recusa. "
    "**Não insira informações adicionais ou desculpas além da frase padrão.** "
    "FRASE DE RECUSA OBRIGATÓRIA: 'Minha área de especialização é a UNINASSAU João Pessoa. Sinto muito por não ter essa informação.'"
)
    # ----------------------------------------

def responder(pergunta):
    resposta = client.responses.create(
        model="gpt-4o-mini",
        input=[
            {"role": "system", "content": "instrucao_assistente"},
            {"role": "user", "content": pergunta}
        ]
    )
    return resposta.output_text
