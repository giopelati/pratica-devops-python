from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Olá, Mundo! Mais uma imagem Docker publicada com sucesso via GitHub Actions!</h1>'

if __name__ == '__main__':
    
    app.run(host='0.0.0.0', port=5000)