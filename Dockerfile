# Use a imagem base do Google Cloud SDK
FROM gcr.io/google.com/cloudsdktool/cloud-sdk:alpine

# Defina a versão do kubectl
ARG KUBECTL_VERSION=v1.26.5

# Adicione o kubectl
RUN gcloud components install kubectl

# Copie o kubectl para a pasta /usr/local/bin/
ADD https://storage.googleapis.com/kubernetes-release/release/${KUBECTL_VERSION}/bin/linux/amd64/kubectl /usr/local/bin/kubectl
RUN chmod +x /usr/local/bin/kubectl

# Defina o diretório de trabalho
WORKDIR /app

# Instale as dependências do Flask
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie o código do aplicativo para a imagem
COPY . .

# Exponha a porta em que o aplicativo Flask está sendo executado
EXPOSE 5000

# Comando para iniciar o aplicativo Flask
CMD ["python", "app.py"]
