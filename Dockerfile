# Usar a imagem base do Python
FROM python:3.9

# Diretório de trabalho
WORKDIR /app

# Copiar os arquivos de dependências
COPY requirements.txt .

# Instalação das dependências do Flask
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o código do aplicativo para a imagem
COPY . .

# Expor a porta em que o aplicativo Flask está sendo executado
EXPOSE 5000

# Comando para iniciar o aplicativo Flask
CMD ["python", "app.py"]
