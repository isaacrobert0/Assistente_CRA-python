import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

# Inicializa cliente Groq
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Carrega informações da Uninassau
def carregar_md(caminho_arquivo="uninassau_infos.md"):
    caminho = os.path.join(os.path.dirname(__file__), caminho_arquivo)
    if not os.path.exists(caminho):
        return "Arquivo .md não encontrado."
    with open(caminho, "r", encoding="utf-8") as f:
        return f.read()

conteudo_md = carregar_md()

# Palavras de saudação
saudacoes = ["oi", "olá", "ola", "bom dia", "boa tarde", "boa noite", "hey", "e ai"]

# Função principal para responder
def responder(pergunta):
    pergunta_lower = pergunta.lower().strip()

    if pergunta_lower in saudacoes:
        return "Oi! Eu sou o assistente virtual da Uninassau João Pessoa. Como posso te ajudar?"

    system_prompt = f"""
Você é um assistente especializado em informações sobre a Uninassau João Pessoa.
Responda **apenas sobre a pergunta do usuário**, usando as informações abaixo como referência.

Se a pergunta do usuário envolver estágio, pergunte primeiro:
1. Se ele é PF ou PJ
2. Se o estágio é Obrigatório ou Não Obrigatório

Depois que o usuário responder, entregue apenas a informação correspondente.

{conteudo_md}

Se a pergunta não estiver relacionada à Uninassau João Pessoa, responda:
'Desculpe, só posso responder sobre a Uninassau João Pessoa!'
"""

    resposta = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": pergunta}
        ]
    )

    return resposta.choices[0].message["content"]
