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
pages = st.sidebar.selectbox("Escolha uma opção", ["Início", "Adicionar Movimento", "Histórico de Movimentos"])

# Condicionais para redirecionar o usuário para as páginas
if pages == "Início":
    st.markdown("""
    ### O que podes fazer aqui:
    - **Adicionar receitas** quando receberes dinheiro.
    - **Adicionar despesas** para controlar os teus gastos.
    - Ver um **resumo do teu saldo** e categorias de movimentação.
    """)

elif pages == "Adicionar Movimento":
    # Adiciona o código para a página de adicionar receitas/despesas
    
    st.write("## Adicionar Movimento")
    st.markdown("""
    Esta página permite adicionar movimentos financeiros, como receitas ou despesas.
    """)

elif pages == "Histórico de Movimentos":
    # Adiciona o código para a página de histórico
    st.write("## Histórico de Movimentos")
    st.markdown("""
    Esta página mostra todos os movimentos financeiros registados.
    """)
    # Ao utilizar multi-páginas, não é necessário duplicar o código aqui