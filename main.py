import streamlit as st

def substituir_nomes(query_antiga):
    # dicionário com as substituições necessárias
    substituicoes = {
        'data-bronze-prd-12.sandbox.credit_portfolio_vlucas': 'data-silver-prd-11.credit.credit_portfolio_bau',
        'data-bronze-prd-12.sandbox.fpa_classifica_industria': 'data-silver-prd-11.fpa.fpa_classifica_industria',
        'data-bronze-prd-12.sandbox.controladoria_Cashout_Installments_Settled_com_Anticipation': 'data-silver-prd-11.fpa.fpa_controladoria_cashout_anticipation',
        'data-bronze-prd-12.sandbox.fpa_credit_engine': 'data-silver-prd-11.fpa.fpa_credit_engine',
        'data-bronze-prd-12.sandbox.fpa_novo_recorrente': 'data-silver-prd-11.data_silver.companies'
        'data-bronze-prd-12.core.companies': 'data-silver-prd-11.data_silver.companies'
        'data-bronze-prd-12.core.invoices': 'data-silver-prd-11.data_silver.invoices'
        'data-bronze-prd-12.sandbox.vw_credit_portfolio': 'data-silver-prd-11.credit.installments_payment_registry'
        'sandbox.vw_credit_portfolio': 'data-silver-prd-11.credit.installments_payment_registry'

    }
    
    # substituir os nomes antigos pelos novos na query
    for nome_antigo, nome_novo in substituicoes.items():
        query_antiga = query_antiga.replace(nome_antigo, nome_novo)
    
    return query_antiga

st.title("Correção de Nomes de Tabelas")

query_antiga = st.text_area("Cole sua query aqui:")
if st.button("Corrigir Nomes"):
    query_nova = substituir_nomes(query_antiga)
    st.text_area("Query Corrigida:", value=query_nova, height=200)

