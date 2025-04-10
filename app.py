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
            background-color: #2e2e2e;  /* Cor cinza suave */
            color: white;  /* Texto em branco para contraste */
        }
        .css-1d391kg {  /* Mudança no estilo do título para destacar melhor */
            color: white;
        }
    </style>
    """, unsafe_allow_html=True)

# Título com um estilo mais destacado
st.title("Gestor Financeiro 💰")
st.markdown("""
### Bem-vindo à tua aplicação de gestão financeira pessoal!

Usa o menu à esquerda para navegar pelas funcionalidades da aplicação:
- **Adicionar movimentos**: Registra as tuas receitas e despesas.
- **Ver histórico**: Consulta o histórico completo dos teus movimentos financeiros.
""")

# Divisão da página em colunas para um layout mais limpo
col1, col2 = st.columns([1, 2])

with col1:
    # Adiciona alguns botões com ícones ou emojis para interações rápidas
    st.button("Adicionar Receita 🏦")
    st.button("Adicionar Despesa 💳")
    
with col2:
    # Exibe um resumo simples ou uma introdução à funcionalidade
    st.markdown("""
    ### O que podes fazer aqui:
    - **Adicionar receitas** quando receberes dinheiro.
    - **Adicionar despesas** para controlar os teus gastos.
    - Ver um **resumo do teu saldo** e categorias de movimentação.
    """)

# Botão de histórico (na parte inferior da tela)
if st.button("Ver Histórico de Movimentos 📜"):
    st.write("Aqui estará o histórico de todos os teus movimentos financeiros.")

    
