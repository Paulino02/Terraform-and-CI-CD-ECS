# Use a imagem base do Python 3.11
FROM python:3.11

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia o arquivo de requisitos (requirements.txt) para o diretório de trabalho
COPY requirements.txt .

# Instala as dependências do Python listadas no requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o conteúdo do diretório atual para o diretório de trabalho no container
COPY . /app

# Exponha a porta 8080 para permitir o acesso externo à aplicação
EXPOSE 8080

# Define o comando padrão para rodar a aplicação Flask
CMD ["python3", "comment.py"]