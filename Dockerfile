<<<<<<< HEAD
 Usar a imagem base do Python
=======
# Usar a imagem base do Python
>>>>>>> parent of 77b4dae (update cloudbuild e dockerfile with personalized image)
FROM python:3.9

# Define a versão do kubectl
ARG KUBECTL_VERSION=v1.26.5

# Adicionar o kubectl
ADD https://storage.googleapis.com/kubernetes-release/release/${KUBECTL_VERSION}/bin/linux/amd64/kubectl /usr/local/bin/kubectl
RUN chmod +x /usr/local/bin/kubectl

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