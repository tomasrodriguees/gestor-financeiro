import streamlit as st
from db.database import init_db

# Configuração da página
st.set_page_config(page_title="Gestor Financeiro", page_icon="💰", layout="centered")

# Inicia o banco de dados
init_db()

# Adiciona um estilo CSS para configurar a cor de fundo
st.markdown(
    """
    <style>
        body {
            font-size: 16px;
        }
        .stButton>button {
            background-color: #FF6347;  /* Cor de fundo para os botões */
            color: white;  /* Cor do texto no botão */
            border-radius: 10px;
            padding: 10px;
            font-size: 14px;  /* Ajusta o tamanho da fonte dos botões */
        }
        /* Responsividade para telas menores */
        @media (max-width: 600px) {
            body {
                font-size: 14px;  /* Ajusta o tamanho da fonte no mobile */
            }
            .stButton>button {
                font-size: 12px;  /* Ajusta o tamanho da fonte nos botões */
            }
        }
    </style>
    """, unsafe_allow_html=True
)

# Título com um estilo mais destacado
st.title("Wallet Tomás Rodrigues 💰")

# Sidebar para navegação
page = st.sidebar.selectbox("Escolha uma opção", ["Início", "Adicionar Movimento", "Histórico de Movimentos"])

# Condicionais para redirecionar o usuário para as páginas
if page == "Início":
    st.markdown("""
    ### O que podes fazer aqui:
    - **Adicionar receitas** quando receberes dinheiro.
    - **Adicionar despesas** para controlar os teus gastos.
    - Ver um **resumo do teu saldo** e categorias de movimentação.
    """)

elif page == "Adicionar Movimento":
    # Adiciona o código para a página de adicionar receitas/despesas
    import streamlit as st
    from db.database import insert_transaction
    from utils.helpers import get_categories
    from datetime import date

    st.title("➕ Adicionar Movimento")

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

elif page == "Histórico de Movimentos":
    # Adiciona o código para a página de histórico
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
