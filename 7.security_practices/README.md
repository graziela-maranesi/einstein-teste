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

### Problemas encontrados

- Os valores para usuário e senha estão hardcode
- Não é verificado se os valores para os parametros foram enviados
- Esta aceitando espaços em branco a esquerda e a direita
- Em vez de comparar o valor da senha, poderiamos gerar um hash e fazer a comparação de hash
- Pode ser feito sanitização para evitar sql injection
-

### Observações

Como não está falando para utilizar um banco de dados, acredito que poderiamos colocar essas credenciais em variaveis de ambiente

Eu deixei o ponto env com os valores de username e password, pois já estavam no enunciado.
Em um projeto de produção essas variáveis do .env-template não seriam preenchidas.

A solução com correções de segurança se encontra no arquivo app.py.

### Passo a passo

- Instalar dependencias projeto:

```
pip install -r requirements.txt
cp .env-template .env

```

- Executar código:

```
python3 app.py

```
