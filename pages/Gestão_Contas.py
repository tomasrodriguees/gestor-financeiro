import streamlit as st
from db.database import get_all_contas, get_saldo_conta
from datetime import date
from db.database import insert_transaction

# Página de Gestão de Contas
st.title("🔑 Gestão de Contas")

# Obter todas as contas criadas
contas = get_all_contas()

# Verifica se há contas
if not contas:
    st.info("Ainda não há contas criadas. Crie uma conta na página 'Conta Principal'.")
else:
    # Exibir lista de contas
    conta_selecionada = st.selectbox("Escolha uma conta", [conta[1] for conta in contas])  # Nome das contas

    # Obter o ID da conta selecionada
    conta_id = [conta[0] for conta in contas if conta[1] == conta_selecionada][0]

    # Exibir saldo da conta selecionada
    saldo = get_saldo_conta(conta_id)
    st.markdown(f"**Saldo da Conta '{conta_selecionada}'**: R${saldo:.2f}")

    # Adicionar dinheiro à conta
    st.subheader("💵 Adicionar Dinheiro à Conta")
    with st.form("form_adicionar_dinheiro"):
        valor = st.number_input("Valor a Adicionar", min_value=0.01, format="%.2f")
        notes = st.text_input("Notas (opcional)")
        submit_dinheiro = st.form_submit_button("Adicionar Dinheiro")

        if submit_dinheiro and valor > 0:
            # Registar o movimento de adição de dinheiro
            insert_transaction("Receita", valor, "Depósito", str(date.today()), notes, conta_id)
            st.success(f"R${valor:.2f} adicionados à conta '{conta_selecionada}' com sucesso!")
