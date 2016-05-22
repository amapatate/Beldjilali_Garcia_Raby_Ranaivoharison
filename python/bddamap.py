import mysql.connector

config = {
    'user': 'admin',
    'password': 'admin',
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


# insertion dans la table commentaires
def insertAccount(civilite='', nom='', prenom='', telephone='', email='', adresse='', mdp=''):
    cnx = connect_BD()
    query = (
    "INSERT INTO `IENAC15_beldjilali_garcia_raby_ranaivoharison`.`client` (civilite, nom, prenom, telephone, email, adresse, mdp) VALUES (%s, %s, %s, %s, %s, %s, %s);")
    param = (civilite, nom, prenom, telephone, email, adresse, mdp)
    try:
        cursor = cnx.cursor()
        cursor.execute(query, param)
        cnx.commit()
    except:
        cnx.rollback()
    close_BD(cursor, cnx)


# Affichage de la table commentaires
def afficheComment():
    cnx = connect_BD()
    cursor = cnx.cursor()
    query = ("SELECT id, nom, comment, email FROM `IENAC15_beldjilali_garcia_raby_ranaivoharison`.`Commentaires` ")
    cursor.execute(query)
    liste = list(cursor)
    close_BD(cursor, cnx)
    return liste


def selectProduit():
    cnx = connect_BD()
    cursor = cnx.cursor()
    query = ("SELECT id,nom,type,variete,description,prix_kg,photo FROM produit")
    cursor.execute(query)  # envoi de la requete
    rows = cursor.fetchall()  # réception des données sous forme de liste
    close_BD(cursor, cnx)
    return rows



def gestionLoginClient(login,pwd):
    '''
    :param login: vient de l'attribut du formulaire : c'est l'email
    :param pwd: password
    :return: KO si le user n'est pas reconnu
             client si le user est un client
             agriculteur si ...
    '''
    cnx = connect_BD()
    cursor = cnx.cursor()
    query = ("SELECT id,nom,prenom,telephone,email FROM `IENAC15_beldjilali_garcia_raby_ranaivoharison`.`client` WHERE email=%s AND mdp=%s LIMIT 1")
    param=(login,pwd)
    cursor.execute(query,param)  # envoi de la requete
    response = cursor.fetchone()
    if(response is None):
        close_BD(cursor, cnx)
        return "KO" # 0 si auth pas bonne
    else:
        close_BD(cursor, cnx)
        return "client" # 1 si authentification ok



def gestionLoginAgriculteur(login,pwd):
    cnx = connect_BD()
    cursor = cnx.cursor()
    query = ("SELECT id,nom,prenom,telephone,email FROM `IENAC15_beldjilali_garcia_raby_ranaivoharison`.`agriculteur` WHERE email=%s AND mdp=%s LIMIT 1")
    param=(login,pwd)
    cursor.execute(query,param)  # envoi de la requete
    response = cursor.fetchone()
    if(response is None):
        close_BD(cursor, cnx)
        return "KO" # 0 si authentif pas bonne
    else:
        close_BD(cursor, cnx)
        return "agriculteur"


def gestionLogin(login,pwd):
    rep =gestionLoginClient(login,pwd)
    if rep == "client":
        return rep
    else:
        rep =gestionLoginAgriculteur(login,pwd)
        if rep=="agriculteur":
            return rep
        else:
            return rep

