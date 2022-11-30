from bancodedados import consultarDB, cadastrarDB

class Users:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


def cadastrar(nome, email, senha):
    for usuario in consultarDB():
        if usuario[1] == email:
            return 'false'
            break
    cadastrarDB(nome, email, senha)
    return 'true'


def login(email, senha):
    for usuario in consultarDB():
        if usuario[1] == email and usuario[2] == senha:
            return 'true'
            break
    return 'false'


def getUser(email):
    for usuario in consultarDB():
        if usuario[1] == email:
            return usuario[0]
            break