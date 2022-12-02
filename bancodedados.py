from psycopg2 import *


def consultarDB():
    db = connect('postgres://cobbspuz:hTcSn-CvfzonT34s_uftcX_7ZeDTl7Zb@tuffi.db.elephantsql.com/cobbspuz')
    with db.cursor() as cursor:
        cursor.execute("SELECT * FROM usuarios;")
        return cursor.fetchall()
    db.close()


def cadastrarDB(nome, email, senha):
    db = connect('postgres://cobbspuz:hTcSn-CvfzonT34s_uftcX_7ZeDTl7Zb@tuffi.db.elephantsql.com/cobbspuz')
    with db.cursor() as cursor:
        cursor.execute("INSERT INTO usuarios (nome, email, senha) VALUES (%s, %s, %s) ;", (nome, email, senha,))
        db.commit()
    db.close()


def consultarSimu():
    db = connect('postgres://cobbspuz:hTcSn-CvfzonT34s_uftcX_7ZeDTl7Zb@tuffi.db.elephantsql.com/cobbspuz')
    with db.cursor() as cursor:
        cursor.execute("SELECT * FROM simulacoes;")
        return cursor.fetchall()
    db.close()


def cadastrarSimu(userres, nomesimu, idh, iev, ie, ir):
    db = connect('postgres://cobbspuz:hTcSn-CvfzonT34s_uftcX_7ZeDTl7Zb@tuffi.db.elephantsql.com/cobbspuz')
    with db.cursor() as cursor:
        cursor.execute("INSERT INTO simulacoes (userres, nomesimu, ressimu, iev, ie, ir) VALUES (%s, %s, %s, %s, %s, %s) ;", (userres, nomesimu, idh, iev, ie, ir))
        db.commit()
    db.close()
