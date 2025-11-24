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
saudacoes = ["oi", "olá", "ola", "bom dia", "boa tarde", "boa noite", "hey", "e ai"]

# Função principal de resposta
def responder(pergunta):
    pergunta_lower = pergunta.lower().strip()

    # Saudação simples
    if pergunta_lower in saudacoes:
        return "Oi! Eu sou o assistente virtual da Uninassau João Pessoa. Como posso te ajudar?"

    # Prompt para o modelo
    system_prompt = f"""
Você é um assistente especializado em informações sobre a Uninassau João Pessoa.
Responda **apenas sobre a pergunta do usuário**, usando as informações abaixo como referência.

Se a pergunta do usuário envolver estágio, note que existem informações diferentes para:
- Pessoa Física (PF) ou Pessoa Jurídica (PJ)
- Estágio Obrigatório ou Não Obrigatório

Antes de fornecer a resposta completa sobre estágio, pergunte ao usuário:
1. Se ele é PF ou PJ
2. Se o estágio é Obrigatório ou Não Obrigatório

Depois que o usuário responder, entregue somente a informação correspondente.

{conteudo_md}

Se a pergunta não estiver relacionada à Uninassau João Pessoa, responda:
'Desculpe, só posso responder sobre a Uninassau João Pessoa!'
"""
    
    resposta = client.responses.create(
        model="gpt-4o-mini",
        input=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": pergunta}
        ]
    )

    return resposta.output_text

# Exibir saudação automática ao iniciar
def iniciar_chat():
    print("Oi! Eu sou o assistente virtual da Uninassau João Pessoa. Como posso te ajudar?")

# Exemplo de uso no console
if __name__ == "__main__":
    iniciar_chat()
    while True:
        pergunta = input("Você: ")
        resposta = responder(pergunta)
        print("Assistente:", resposta)
