FROM python:3.11
WORKDIR /app
COPY requirements.txt .
# Instale as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir Flask==2.0.1
COPY . /app
# Exponha a porta em que a aplicação será executada
EXPOSE 8080
# Comando para rodar a aplicação Flask
CMD ["python3", "comment.py"]
