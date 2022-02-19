import os
from flask import Flask, abort, render_template, request

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('calculadora.html')

@app.route('/calculadora', methods=['POST', 'GET'])
def calculadora():
    digito1 = request.form['d1']
    digito2 = request.form['d2']
    resultado = request.form['resultado']

    digito1 = int(digito1)

    digito2 = int(digito2)

    if(resultado == 'mais'):
        operacaoCalculada = digito1 + digito2
    elif(resultado == 'menos'):
        operacaoCalculada = digito1 - digito2
    elif(resultado == 'dividir'):
        if(digito2 ==0):
            abort(422)
        else:
            operacaoCalculada = digito1 / digito2
    elif(resultado == 'multiplicar'):
        operacaoCalculada = digito1 * digito2
    else:
        abort(404)

    return str(operacaoCalculada)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5005))
    app.run(host='127.0.0.1', port=port)