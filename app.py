import streamlit as st
from db.database import init_db

st.set_page_config(page_title="Gestor Financeiro", layout="centered")

init_db()

st.title("💰 Gestor Financeiro Pessoal")
st.markdown("""
Bem-vindo à tua aplicação de gestão financeira pessoal.  
Usa o menu à esquerda para:
- Adicionar movimentos
- Ver o histórico de receitas e despesas
""")
