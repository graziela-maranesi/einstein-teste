import os
from dotenv import load_dotenv
from flask import Flask, request

load_dotenv(override=True)

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    username = str(request.form['username']).strip()
    password = str(request.form['password']).strip()

    if username is None or password is None:
        return "Acesso negado"

    EXPECTED_USERNAME = os.getenv('APP_USERNAME')
    EXPECTED_PASSWORD = os.getenv('APP_PASSWORD')

    print(f'EXPECTED_USERNAME {EXPECTED_USERNAME}')
    print(f'EXPECTED_PASSWORD {EXPECTED_PASSWORD}')

    if username == EXPECTED_USERNAME and password == EXPECTED_PASSWORD:
        return "Acesso concedido"

    return "Acesso negado"

if __name__ == '__main__':
    app.run(debug=True)