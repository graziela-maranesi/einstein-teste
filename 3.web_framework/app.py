from flask import Flask, request

app = Flask(__name__)

@app.route('/saudacao', methods=['GET'])
def saudacao():
    nome = str(request.args.get('nome', '')).strip()
    if len(nome) == 0:
        return f'Olá! Bem vindo ao meu teste!'

    return f'Olá, {nome}! Bem vindo ao meu teste!'

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)