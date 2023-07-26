from flask import Flask, Response
from prometheus_client import Counter, generate_latest, CollectorRegistry

app = Flask(__name__)

request_count = Counter('gin_flask_request_count', 'Total number of requests received')
# Rota principal para a página inicial
@app.route('/')
def home():
    return 'Hello, World! This is a simple Flask app running on Kubernetes.'

# Rota para receber métricas personalizadas
@app.route('/metrics')
def custom_metrics():
    # create a Prometheus registry and register the request_count metric
    registry = CollectorRegistry()
    registry.register(request_count)
    
    return Response(generate_latest(registry), content_type='text/plain')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)