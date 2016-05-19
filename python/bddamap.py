import mysql.connector

config = {
  'user': 'root',
  'password': 'mysql',
  'host': 'localhost',
  'database': 'bdd_amapatate',
  'raise_on_warnings': True
    }

#connexion à la base de données
def connect_BD():
    try:
        cnx = mysql.connector.connect(**config)
        cnx.autocommit=False
        print("connexion ok")
    except:
        print("Something is wrong with your user name or password")
    return cnx


def close_BD(cursor,cnx):
    cursor.close()
    cnx.close()

#insertion dans la table commentaires
def insertAccount(nom='', prenom='', email='', adresse='', mdp=''):
    cnx=connect_BD()
    query = ("INSERT INTO `bdd_amapatate`.`Compte` (mail, nom, prénom, adresse, mdp) VALUES (%s, %s, %s, %s, %s);")
    param=(email, mdp, nom, prenom, adresse)
    try:
        cursor = cnx.cursor()
        cursor.execute(query, param)
        cnx.commit()
    except:
        cnx.rollback()
    close_BD(cursor,cnx)

#Affichage de la table commentaires
def affichComment():
    cnx=connect_BD()
    cursor = cnx.cursor()
    query = ("SELECT id, nom, comment, email FROM `bd_ienac_gr11`.`Commentaires` ")
    cursor.execute(query)
    liste=list(cursor)
    close_BD(cursor,cnx)
    return liste
