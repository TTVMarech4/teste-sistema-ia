import streamlit as st
import pandas as pd
import os
import openai
import json

# --- 1. CONFIGURAÇÃO DE PÁGINA (ESTILO PREMIUM) ---
st.set_page_config(page_title="AuraFit AI | Premium SaaS", layout="wide")

# --- 2. THEME ENGINE (UX/UI Designer) ---
# Movemos o código do ui/styles/theme.py para cá
st.markdown("""
    <style>
    .main { background-color: #0E1117; color: #FFFFFF; }
    .stButton>button { 
        background-color: #00D1FF; 
        color: black; 
        border-radius: 10px; 
        font-weight: bold; 
        width: 100%;
        border: none;
        padding: 0.5rem;
    }
    .stMetric { 
        background-color: #161B22; 
        border-radius: 10px; 
        padding: 15px; 
        border: 1px solid #30363D; 
    }
    h1, h2, h3 { color: #00D1FF !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. AI ENGINE (IA Specialist) ---
# Movemos a lógica do core/ai_engine/coach.py para cá
class AuraFitAI:
    def __init__(self, api_key):
        self.api_key = api_key
    
    def generate_plan(self, user_data):
        if not self.api_key:
            return "Erro: Chave de API não configurada nas variáveis do Railway."
        # Simulação de resposta da IA para o MVP
        return {
            "treino": "Treino A: Foco em Hipertrofia (Supino, Agachamento, Remada)",
            "dieta": "Dieta Hipercalórica: 2800kcal | 160g Proteína",
            "insight": "Seu volume de treino aumentou 12% desde a última semana. Mantenha a constância!"
        }

# --- 4. INTERFACE PRINCIPAL (Product Manager) ---
st.sidebar.title("🌌 AURAFIT AI")
st.sidebar.markdown("---")
menu = st.sidebar.radio("Navegação", ["Dashboard", "Treino IA", "Nutrição", "Assinatura", "Admin"])

# Inicializa a IA com a chave das variáveis de ambiente
api_key = os.getenv("OPENAI_API_KEY")
coach = AuraFitAI(api_key)

if menu == "Dashboard":
    st.title("Performance Dashboard ⚡")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1: st.metric("Peso Atual", "82.5 kg", "-0.5 kg")
    with col2: st.metric("Energia", "92%", "+5%")
    with col3: st.metric("Streak", "15 Dias 🔥")
    with col4: st.metric("XP Total", "2,850", "Top 3%")

    st.subheader("Análise de Evolução (IA)")
    chart_data = pd.DataFrame({'Força': [10, 25, 45, 60, 85], 'Resistência': [20, 30, 40, 55, 70]})
    st.line_chart(chart_data)

elif menu == "Treino IA":
    st.header("🦾 Personal Trainer Digital")
    st.write("A IA analisa seus dados em tempo real para ajustar sua carga.")
    
    if st.button("Gerar Plano Adaptativo"):
        with st.spinner("IA calculando sua nova rotina..."):
            resultado = coach.generate_plan({"peso": 82})
            st.success("Plano Gerado com Sucesso!")
            st.info(f"**Treino Sugerido:** {resultado['treino']}")
            st.warning(f"**Ajuste de Dieta:** {resultado['dieta']}")
            st.chat_message("assistant").write(resultado['insight'])

elif menu == "Assinatura":
    st.header("💳 Gerencie seu Plano")
    st.info("Você está no Plano **PREMIUM PRO**")
    st.button("Fazer Upgrade para Corporate")

# --- 5. RODAPÉ DE COMPLIANCE (Legal Specialist) ---
st.sidebar.markdown("---")
st.sidebar.caption("AuraFit AI v1.0.0 | LGPD Compliant")
