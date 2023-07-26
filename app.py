from flask import Flask, Response, render_template_string
from prometheus_client import Counter, generate_latest, CollectorRegistry

app = Flask(__name__)

request_count = Counter('gin_flask_request_count', 'Total number of requests received')
# Rota principal para a página inicial
html_template = '''
<!DOCTYPE html>
<html>
<head>
    <title>Efeito Bounce com Diferentes Atrasos</title>
    <style>
        body {
            margin: 0;
            overflow: hidden;
            background-color: #f0f0f0;
        }
        #container {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .bounce-letters {
            font-size: 48px;
            font-weight: bold;
            color: #007bff;
            display: inline-block;
        }
        .bounce-letters span {
            display: inline-block;
            animation: bounce 0.5s infinite alternate;
        }
        @keyframes bounce {
            from {
                transform: translateY(0);
            }
            to {
                transform: translateY(-20px);
            }
        }
    </style>
</head>
<body>
    <div id="container">
        <div class="bounce-letters">
            <span style="animation-delay: 0s;">H</span>
            <span style="animation-delay: 0.1s;">e</span>
            <span style="animation-delay: 0.2s;">l</span>
            <span style="animation-delay: 0.3s;">l</span>
            <span style="animation-delay: 0.4s;">o</span>
            <span style="animation-delay: 0.5s;">,</span>
            <span style="animation-delay: 0.6s;"> </span>
            <span style="animation-delay: 0.7s;">W</span>
            <span style="animation-delay: 0.8s;">o</span>
            <span style="animation-delay: 0.9s;">r</span>
            <span style="animation-delay: 1s;">l</span>
            <span style="animation-delay: 1.1s;">d</span>
            <span style="animation-delay: 1.2s;">!</span>
        </div>
    </div>
</body>
</html>
'''
@app.route('/')
def home():
    return render_template_string(html_template)

# Rota para receber métricas personalizadas
@app.route('/metrics')
def custom_metrics():
    # create a Prometheus registry and register the request_count metric
    registry = CollectorRegistry()
    registry.register(request_count)
    
    return Response(generate_latest(registry), content_type='text/plain')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)