# fichier pour mise en place des sessions
# cf fin poly papier page 35
# mais problème de login non reconnu

import mysql.connector

Index = Import('/IENAC15/beldjilali_garcia_raby_ranaivoharison/index.py')
connexion = Import('/IENAC15/beldjilali_garcia_raby_ranaivoharison/python/connexion.py')
print("Content-type:text/html\n\n")

config = {
    'user': 'root',
    'password': 'mysql',
    'host': 'localhost',
    'database': 'IENAC15_beldjilali_garcia_raby_ranaivoharison',
    'raise_on_warnings': True
}


# connexion à la base de données
def connect_BD():
    try:
        cnx = mysql.connector.connect(**config)
        cnx.autocommit = False
        print("connexion ok")
    except:
        print("Something is wrong with your user name or password")
    return cnx


def close_BD(cursor, cnx):
    cursor.close()
    cnx.close()


def index(login, pwd):
    cnx = connect_BD()
    cursor = cnx.cursor()
    query = ("SELECT id,nom,prenom,telephone,email FROM client WHERE email=%s AND mdp=%s LIMIT 1")
    param = (login, pwd)
    cursor.execute(query, param)  # envoi de la requete
    response = cursor.fetchone()
    if (response is None):
        # Si None, on a peut-etre un agriculteur
        query = ("SELECT id,nom,prenom,telephone,email FROM agriculteur WHERE email=%s AND mdp=%s LIMIT 1")
        cursor.execute(query, param)
        response = cursor.fetchone()
        if (response is None):
            return connexion.connexion('0')  # Ni agriculteur, ni client
        else:
            # On a un agriculteur
            Session()["nom"] = response[1]
            Session()["prenom"] = response[2]
            Session()["id"] = response[0]
            Session()["telephone"] = response[3]
            Session()["email"] = response[4]
            Session()["type"] = 'agriculteur'
            close_BD(cursor, cnx)
            return Index.index()
    else:
        # On a un client
        Session()["nom"] = response[1]
        Session()["prenom"] = response[2]
        Session()["id"] = response[0]
        Session()["telephone"] = response[3]
        Session()["email"] = response[4]
        Session()["type"] = 'client'
        close_BD(cursor, cnx)
        return Index.index()  # 1 si authentification ok
