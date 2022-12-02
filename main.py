from flask import *
from autenticador import cadastrar as cd, login as lg, getUser
from simulador import calcIDH
from bancodedados import consultarSimu, cadastrarSimu

usuario = ''

app = Flask(__name__)


@app.route('/', methods=["GET"])
def main():
    return render_template('inicio.html')


@app.route('/logar')
def iniciarL():
    return render_template('logar.html')


@app.route('/login', methods=["POST"])
def logar():
    if lg(request.form['email'], request.form['senha']) == 'true':
        global usuario
        usuario = getUser(request.form['email'])
        return render_template('simulador.html', usertime=userTime())
    else:
        return render_template('logar.html', res2='Email e(ou) Senha Incorretos.')


def userTime():
    return usuario


@app.route('/cadastrar')
def iniciarC():
    return render_template('cadastrar.html')


@app.route('/cadastro', methods=["POST"])
def cadastrar():
    if request.form['nome'] == '' or request.form['email'] == '' or request.form['senha'] == '':
        return render_template('cadastrar.html', res='Um ou mais campos vazios.')
    elif cd(request.form['nome'], request.form['email'], request.form['senha']) == 'true':
        return render_template('logar.html', res='Cadastro Realizado com Sucesso')
    else:
        return render_template('cadastrar.html', res='Email já Cadastrado.')


@app.route('/simulacao', methods=["GET", "POST"])
def simular():
    if request.method == 'GET':
        return render_template('simulador.html', usertime=userTime())
    elif request.method == 'POST':
        if request.form['EV'] == '' or request.form['AME'] == '' or request.form['AEE'] == '' or request.form['PIBpc'] == '':
            return render_template('simulador.html', res='Um ou mais campos vazios.')
        else:
            idh = calcIDH(request.form['EV'], request.form['AME'], request.form['AEE'], request.form['PIBpc'])[0]
            iev = calcIDH(request.form['EV'], request.form['AME'], request.form['AEE'], request.form['PIBpc'])[1]
            ie = calcIDH(request.form['EV'], request.form['AME'], request.form['AEE'], request.form['PIBpc'])[2]
            ir = calcIDH(request.form['EV'], request.form['AME'], request.form['AEE'], request.form['PIBpc'])[3]
            nomeSimu = request.form['nomeSimulacao']
            cadastrarSimu(userTime(), nomeSimu, str(idh), str(iev), str(ie), str(ir))
            return render_template('simulador.html', res2='Simulacao Finalizada!', idh=idh, iev=iev, ie=ie, ir=ir)


@app.route('/resultados', methods=["GET"])
def exibir():
    dados = consultarSimu()
    return render_template('resultados.html', usertime=userTime(), dados=dados)


app.run()
