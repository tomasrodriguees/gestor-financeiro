import streamlit as st
import pandas as pd
from db.database import get_all_transactions

st.title("📄 Histórico de Movimentos")

data = get_all_transactions()
df = pd.DataFrame(data, columns=["ID", "Tipo", "Valor", "Categoria", "Data", "Notas"])

if df.empty:
    st.info("Ainda não há movimentos registados.")
else:
    st.dataframe(df.drop(columns="ID"), use_container_width=True)
