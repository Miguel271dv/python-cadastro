import streamlit as st
from datetime import date

st.title("Cadastro de clientes")

nome = st.text_input("Digite o nome do cliente")
endereco = st.text_input("Digite o endereço")
dt_nasc = st.date_input("Escolha a data de nascimento")
tipo_cliente = st.selectbox("Tipo de cliente", 
                            ["Pessoa física", "Pessoa jurídica"])

cadastrar = st.button("Cadastrar cliente")

if cadastrar:
    
    hoje = date.today()
    
    if not nome.strip():
        st.error("O nome é obrigatório.")

    elif not endereco.strip():
         st.error("O endereço é obrigatório.")
    elif dt_nasc > hoje:
         st.error("Data de nascimento não pode ser no futuro.")

    else:
        with open("clientes.csv", "a", encoding="utf8") as arquivo:
              arquivo.write(f"{nome},{endereco},{dt_nasc},{tipo_cliente}\n")
        st.success("Cliente cadastrado com sucesso!")