FROM python:3.9-slim

# Define o diretório de trabalho dentro do servidor
WORKDIR /app

# Instala apenas o essencial para o Python compilar algumas bibliotecas
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copia os requisitos e instala as bibliotecas do Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o resto do código do seu projeto
COPY . .

# AJUSTE DE CAMINHO: Isso resolve o erro anterior do "No module named ui"
ENV PYTHONPATH=/app

# Porta padrão do Streamlit
EXPOSE 8501

# Comando para iniciar o SaaS
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
