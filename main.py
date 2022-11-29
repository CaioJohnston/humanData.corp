from flask import Flask, render_template, request
from autenticador import cadastrar as cd, login as lg
from simulador import calcIDH
from bancodedados import consultarSimu, cadastrarSimu
from time import sleep

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('main.html')


@app.route('/logar')
def iniciarL():
    return render_template('logar.html')


@app.route('/login', methods=["POST"])
def logar():
    if lg(request.form['email'], request.form['senha']) == 'true':
        return render_template('main.html')
    else:
        return render_template('logar.html', res='Email e(ou) Senha Incorretos.')



@app.route('/cadastrar')
def iniciarC():
    return render_template('cadastrar.html')


@app.route('/cadastro', methods=["POST"])
def cadastrar():
    if cd(request.form['nome'], request.form['email'], request.form['senha']) == 'true':
        return render_template('main.html')
    else:
        return render_template('cadastrar.html', res='Email ja Cadastrado.')


app.run()
