import streamlit as st
from datetime import date
import csv

st.title("Cadastro de clientes")

nome = st.text_input("Digite o nome do cliente", key="nome")
endereco = st.text_input("Digite o endereço", key="endereco")

hoje = date.today()
dt_nasc = st.date_input(
                       "Escolha a data de nascimento",
                        min_value=date(1900, 1, 1),
                        max_value=hoje,
                        key="dt_nasc"
)
tipo_cliente = st.selectbox(
        "Tipo de cliente", 
        ["Pessoa física", "Pessoa jurídica"],
        key="tipo"
)
cadastrar = st.button("Cadastrar cliente")
if cadastrar:
     
     if not nome:
          st.warning("Por favor, digite o nome do cliente!")

     elif not endereco:
          st.warning("Por favor, digite o endereço!")

     elif dt_nasc > hoje:
          st.warning("Data de nascimento inválida!")

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
else:
     
     existe = False
     try:
          with open("clientes.csv","r", newline="") as arquivo:
            reader = csv.reader(arquivo, delimiter=";")
            for linha in reader:
                    
                if linha and (linha[0] == nome or linha[1 == endereco]):
                    existe = True
                    break
     except FileNotFoundError:
                    pass
                    
     if existe:
         st.error("Cliente já cadastrado!")
     else:
         with open("clientes.csv", "a", newline="") as arquivo:
             writer = csv.writer(arquivo, delimiter=";")
             writer.writerow([nome, endereco, dt_nasc, tipo_cliente])
         st.success("Cliente cadastrado com sucesso!")