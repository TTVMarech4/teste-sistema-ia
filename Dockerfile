FROM python:3.9-slim

# Define o diretório de trabalho
WORKDIR /app

# Instala dependências do sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    && rm -rf /var/lib/apt/lists/*

# Copia os arquivos de requisitos e instala
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o projeto
COPY . .

# VARIÁVEL CRUCIAL: Adiciona o diretório atual ao PATH do Python
ENV PYTHONPATH=/app

# Expondo a porta do Streamlit
EXPOSE 8501

# Comando para rodar
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]