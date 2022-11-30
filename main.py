from flask import *
from autenticador import cadastrar as cd, login as lg, getUser
from simulador import calcIDH
from bancodedados import consultarSimu, cadastrarSimu

usuario = ''

app = Flask(__name__)


@app.route('/', methods=["GET"])
def main():
    return render_template('inicio.html')


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/logar')
def iniciarL():
    return render_template('logar.html')


@app.route('/login', methods=["POST"])
def logar():
    if lg(request.form['email'], request.form['senha']) == 'true':
        global usuario
        usuario = getUser(request.form['email'])
        return render_template('home.html')
    else:
        return render_template('logar.html', res='Email e(ou) Senha Incorretos.')


def userTime():
    return usuario


@app.route('/cadastrar')
def iniciarC():
    return render_template('cadastrar.html')


@app.route('/cadastro', methods=["POST"])
def cadastrar():
    if cd(request.form['nome'], request.form['email'], request.form['senha']) == 'true':
        return render_template('logar.html', res='Cadastro Realizado com Sucesso')
    else:
        return render_template('cadastrar.html', res='Email ja Cadastrado.')


@app.route('/simulacao', methods=["GET", "POST"])
def simular():
    if request.method == 'GET':
        return render_template('simulador.html', usertime=userTime())
    elif request.method == 'POST':
        idh = calcIDH(request.form['EV'], request.form['AME'], request.form['AEE'], request.form['PIBpc'])
        nomeSimu = request.form['nomeSimulacao']
        cadastrarSimu(userTime(), nomeSimu, str(idh))
        return render_template('simulador.html', res=idh, rescad='Simulacao Finalizada e Compartilhada com Sucesso')


@app.route('/resultados', methods=["GET"])
def exibir():
    return render_template('resultados.html', res=consultarSimu())


app.run()
