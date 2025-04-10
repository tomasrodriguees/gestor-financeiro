import streamlit as st
from db.database import init_db

# Inicia o banco de dados
init_db()

# Configuração da página
st.set_page_config(page_title="Gestor Financeiro", page_icon="💰", layout="centered")

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