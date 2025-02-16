## Questão 7

`Security Practices (15 pontos) Identifique e corrija as vulnerabilidades no seguinte código Flask:
`

```
from flask import Flask, request
app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
	username = request.form['username']
	password = request.form['password']
	if username == 'admin' and password == '1234':
        return "Acesso concedido"
	return "Acesso negado"

if __name__ == '__main__':
    app.run(debug=True)

```

### Passo a passo

- Instalar dependencias projeto:

```
pip install -r requirements.txt

```

- Executar código:

```
python3 app.py

```
