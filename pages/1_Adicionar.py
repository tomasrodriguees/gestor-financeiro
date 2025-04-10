import streamlit as st
from db.database import insert_transaction
from utils.helpers import get_categories
from datetime import date

st.title("➕ ADICIONAR MOVIMENTOS")

with st.form("add_form"):
    type_ = st.selectbox("Tipo", ["Receita", "Despesa"])
    amount = st.number_input("Valor", min_value=0.0, format="%.2f")
    category = st.selectbox("Categoria", get_categories())
    date_input = st.date_input("Data", value=date.today())
    notes = st.text_input("Notas (opcional)")

    submitted = st.form_submit_button("Adicionar")

    if submitted and amount > 0:
        insert_transaction(type_, amount, category, str(date_input), notes)
        st.success("Movimento adicionado com sucesso!")
