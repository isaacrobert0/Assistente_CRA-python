import os
from openai import OpenAI

client = OpenAI()

# Carrega o conteúdo do arquivo .md
def carregar_md(caminho_arquivo="uninassau_infos.md"):
    caminho = os.path.join(os.path.dirname(__file__), caminho_arquivo)
    if not os.path.exists(caminho):
        return "Arquivo .md não encontrado."
    with open(caminho, "r", encoding="utf-8") as f:
        return f.read()

conteudo_md = carregar_md()

# Lista de palavras para saudações
saudacoes = ["oi", "olá", "ola", "bom dia", "boa tarde", "boa noite", "hey", "e aí"]

def responder(pergunta):
    pergunta_lower = pergunta.lower().strip()

    # Se for uma saudação simples, responder dessa forma
    if pergunta_lower in saudacoes:
        return "Oi! Eu sou o assistente virtual da Uninassau João Pessoa. Como posso te ajudar?"

    # Prompt restritivo para perguntas relacionadas à Uninassau
    system_prompt = (
    "Você é um assistente especializado em informações sobre a Uninassau João Pessoa, "
    "incluindo matrícula, aditamentos, cursos e processos acadêmicos. "
    "Use o conteúdo do arquivo Markdown como referência, mas você também pode usar conhecimento geral "
    "sobre a Uninassau João Pessoa caso a informação não esteja no arquivo ou no site ofical da Uninassau. "
    "Se a pergunta for sobre outro assunto fora da Uninassau João Pessoa, responda: "
    "'Desculpe, só posso responder sobre a Uninassau João Pessoa!'\n\n"
    f"Aqui está o conteúdo do arquivo Markdown:\n\n{conteudo_md}"
)


    resposta = client.responses.create(
        model="gpt-4o-mini",
        input=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": pergunta}
        ]
    )

    return resposta.output_text
