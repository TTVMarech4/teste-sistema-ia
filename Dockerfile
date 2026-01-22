# Usa uma imagem leve do Python
FROM python:3.9-slim

# Define o diretório onde o código vai morar no servidor
WORKDIR /app

# Instala ferramentas essenciais para compilação de pacotes
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copia os requisitos primeiro (ajuda na velocidade do build)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia todos os arquivos do seu projeto para dentro do servidor
COPY . .

# --- CONFIGURAÇÕES EXECUTIVAS (O segredo do sucesso no Railway) ---

# Garante que o Python encontre as pastas 'ui' e 'core'
ENV PYTHONPATH=/app

# Força o Streamlit a rodar em modo servidor (sem abrir navegador)
ENV STREAMLIT_SERVER_HEADLESS=true

# Desabilita proteções que às vezes bloqueiam o acesso externo no Railway
ENV STREAMLIT_SERVER_ENABLE_CORS=false
ENV STREAMLIT_SERVER_ENABLE_XSRF_PROTECTION=false

# Comando final que liga o sistema usando a porta dinâmica fornecida pelo Railway
# O Streamlit vai ler automaticamente a variável $PORT do Railway
CMD streamlit run app.py --server.port $PORT --server.address 0.0.0.0
