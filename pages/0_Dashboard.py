import streamlit as st
import pandas as pd
import plotly.express as px
from db.database import get_all_transactions

st.set_page_config(page_title="DASHBOARD", layout="wide")
st.title("📊 Dashboard Financeiro")

# 👉 Carregar dados da base de dados
data = get_all_transactions()
df = pd.DataFrame(data, columns=["ID", "Tipo", "Valor", "Categoria", "Data", "Notas"])

if df.empty:
    st.info("Ainda não há movimentos registados.")
else:
    df["Data"] = pd.to_datetime(df["Data"])

    # 👉 Filtros de datas
    min_date = df["Data"].min().date()
    max_date = df["Data"].max().date()

    data_inicio, data_fim = st.date_input("Filtrar por intervalo de datas:", [min_date, max_date])

    df_filtrado = df[(df["Data"] >= pd.to_datetime(data_inicio)) & (df["Data"] <= pd.to_datetime(data_fim))]

    # 👉 Cálculos de resumo
    total_receitas = df_filtrado[df_filtrado["Tipo"] == "Receita"]["Valor"].sum()
    total_despesas = df_filtrado[df_filtrado["Tipo"] == "Despesa"]["Valor"].sum()
    saldo = total_receitas - total_despesas

    # 👉 Mostrar os valores
    col1, col2, col3 = st.columns(3)
    col1.metric("💰 Saldo Atual", f"{saldo:.2f} €")
    col2.metric("⬆️ Total de Receitas", f"{total_receitas:.2f} €")
    col3.metric("⬇️ Total de Despesas", f"{total_despesas:.2f} €")

    st.divider()

    # 👉 Gráfico de evolução mensal
    st.subheader("📈 Evolução Financeira Mensal")
    df_filtrado["Ano-Mês"] = df_filtrado["Data"].dt.to_period("M").astype(str)

    evolucao = df_filtrado.groupby(["Ano-Mês", "Tipo"])["Valor"].sum().reset_index()

    fig = px.bar(
        evolucao,
        x="Ano-Mês",
        y="Valor",
        color="Tipo",
        barmode="group",
        title="Receitas vs Despesas por Mês",
        labels={"Valor": "Valor (€)", "Ano-Mês": "Mês"},
        text_auto=".2s"
    )

    st.plotly_chart(fig, use_container_width=True)
