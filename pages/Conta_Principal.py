import streamlit as st
import pandas as pd
from db.database import insert_transaction, get_all_transactions
from datetime import date

# Página de Conta Principal
st.title("💼 CONTAS")

# Obter todos os movimentos registados
data = get_all_transactions()
df = pd.DataFrame(data, columns=["ID", "Tipo", "Valor", "Categoria", "Data", "Notas"])

if df.empty:
    st.info("Ainda não há movimentos registados.")
else:
    # Calcular o saldo da conta principal
    receita_total = df[df["Tipo"] == "Receita"]["Valor"].sum()
    despesa_total = df[df["Tipo"] == "Despesa"]["Valor"].sum()
    saldo_atual = receita_total - despesa_total

    st.markdown(f"**Saldo Atual da Conta Principal**: R${saldo_atual:.2f}")

# Criar nova conta
st.subheader("🔧 Criar Nova Conta")
with st.form("form_nova_conta"):
    nome_conta = st.text_input("Nome da Conta", max_chars=50)
    tipo_conta = st.selectbox("Tipo de Conta", ["Principal", "Poupança", "Investimentos", "Outros"])
    submit_conta = st.form_submit_button("Criar Conta")

    if submit_conta and nome_conta:
        # Registar nova conta no banco de dados (esta funcionalidade depende da estrutura do banco de dados)
        # Vamos criar uma nova transação associada à nova conta para poder visualizar mais tarde
        st.success(f"Conta '{nome_conta}' criada com sucesso!")
        # Aqui você pode adicionar lógica para armazenar a conta em um banco de dados ou em uma tabela
