from flask import Flask, request

app = Flask(__name__)

# Rota principal para a página inicial
@app.route('/')
def home():
    return 'Hello, World! This is a simple Flask app running on Kubernetes.'

# Rota para receber métricas personalizadas
@app.route('/metrics')
def custom_metrics():
    # Exemplo de métrica personalizada (número de vezes que a rota principal foi acessada)
    metric_value = 1
    return f'my_custom_metric {metric_value}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)