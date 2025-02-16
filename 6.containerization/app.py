from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/saudacao', methods=['GET'])
def saudacao():
    nome = str(request.args.get('nome', '')).strip()
    if len(nome) == 0:
        return f'Olá! Bem vindo ao meu teste!'

    return f'Olá, {nome}! Bem vindo ao meu teste!'

@app.route('/soma', methods=['POST'])
def soma():
    valores = request.get_json()
    primeiro_valor = valores.get('valor1')
    segundo_valor = valores.get('valor2')

    if primeiro_valor is None:
        return jsonify({"erro": "O atributo 'valor1' é obrigatório."}), 400

    if segundo_valor is None:
        return jsonify({"erro": "O atributo 'valor2' é obrigatório."}), 400

    try:
        return jsonify({"soma": float(primeiro_valor) + float(segundo_valor)})
    except Exception:
        return jsonify({"erro": "'Parametros invalidos'."}), 400


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)