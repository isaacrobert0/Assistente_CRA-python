import streamlit as st
from logica_chat import responder

st.set_page_config(page_title="ASSISTENTE VIRTUAL CRA UNINASSAU", layout="centered")

avatar_uninassau = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRu-WxeGPMERFd0TGfOBYXt5RtHi4nbT4F_bw&s"
avatar_user = "imagens/user.png"

if "logado" not in st.session_state:
    st.session_state["logado"] = False
    st.session_state["usuario"] = None
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Tela inicial
col1, col2, col3 = st.columns([1, 3, 1])
with col2:
    st.image("imagens/uninassaulogo.svg", width=300)

st.markdown("<h2 style='text-align: center;'>ASSISTENTE VIRTUAL CRA - João Pessoa</h2>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Informe seus dados para iniciar a conversa.</h3>", unsafe_allow_html=True)

# Formulário de cadastro
if not st.session_state["logado"]:
    with st.form("form_cadastro", clear_on_submit=False):
        nome = st.text_input("Nome completo")
        tipo_usuario = st.selectbox("Você é:", ["aluno", "professor", "colaborador", "externo"])
        matricula = st.text_input("Matrícula (interno)")
        email = st.text_input("E-mail")

        if st.form_submit_button("Iniciar conversa"):
            if not nome or not email:
                st.error("Por favor, preencha Nome e E-mail.")
            else:
                st.session_state["logado"] = True
                st.session_state["usuario"] = {
                    "nome": nome,
                    "email": email,
                    "tipo": tipo_usuario,
                    "matricula": matricula
                }
                st.rerun()

# Tela de chat
if st.session_state["logado"]:
    st.title("Chat Iniciado!")
    st.write(f"Conectado(a) como: **{st.session_state['usuario']['nome']}**")

# Histórico
    for message in st.session_state["messages"]:
        avatar_role = avatar_uninassau if message["role"] == "assistant" else avatar_user
        with st.chat_message(message["role"], avatar=avatar_role):
            st.markdown(message["content"])

# Entrada do usuário
    if prompt := st.chat_input("Digite sua dúvida aqui..."):

        st.session_state["messages"].append({"role": "user", "content": prompt})
        with st.chat_message("user", avatar=avatar_user):
            st.markdown(prompt)

        with st.chat_message("assistant", avatar=avatar_uninassau):
            with st.spinner("O assistente está buscando a resposta..."):
                resposta = responder(prompt)
            st.markdown(resposta)

        st.session_state["messages"].append({"role": "assistant", "content": resposta})

# Botão sair
with st.sidebar:
    if st.button("Sair e Encerrar Sessão"):
        st.session_state.clear()
        st.rerun()
