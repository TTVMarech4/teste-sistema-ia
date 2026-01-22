import sys
import os

# Força o Python a reconhecer a pasta atual como raiz de módulos
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import streamlit as st
from ui.styles.theme import apply_theme
from core.ai_engine.coach import AuraFitAI

# ... resto do código igual
import streamlit as st
from ui.styles.theme import apply_theme
from core.ai_engine.coach import AuraFitAI

st.set_page_config(page_title="AuraFit AI", layout="wide")
apply_theme()

st.sidebar.title("🌌 AURAFIT AI")
menu = st.sidebar.selectbox("Menu", ["Dashboard", "Treino IA", "Financeiro", "Comunidade", "Configurações"])

if menu == "Dashboard":
    st.title("Performance Dashboard")
    col1, col2, col3 = st.columns(3)
    col1.metric("Streak Semanal", "5 Dias 🔥", "+1")
    col2.metric("XP Total", "12,450", "Top 5%")
    col3.metric("Plano Atual", "Premium Pro")
    
    st.subheader("Seu Progresso de Força (IA Analysis)")
    st.line_chart([10, 25, 40, 35, 50, 65])

elif menu == "Treino IA":
    st.header("🦾 Personal Trainer Digital")
    if st.button("Gerar Nova Rotina Semanal"):
        st.info("A IA está calculando seu volume de treino ideal...")
        st.success("Plano pronto! Verifique seu e-mail e o dashboard.")

elif menu == "Financeiro":
    st.header("💳 Gestão de Assinatura")
    st.write("Plano Pro: Ativo (Próxima cobrança: 15/10/2023)")
    st.button("Upgrade para Corporate (B2B)")

