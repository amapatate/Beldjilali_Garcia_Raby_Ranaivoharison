import mysql.connector
print("Content-type:text/html\n\n")
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
      #  cnx.autocommit = False
        print("connexion ok")
    except:
        print("Something is wrong with your user name or password")
    return cnx


def close_BD(cursor, cnx):
    cursor.close()
    cnx.close()

cnx = connect_BD()
cursor = cnx.cursor()

def index(email='',mdp=''):
    resultat=0
    query = ("SELECT id,nom,prenom,telephone,email FROM client WHERE email=%s AND mdp=%s LIMIT 1")
    param=(email,mdp)
    cursor.execute(query,param)  # envoi de la requete
    response = cursor.fetchone()
    if(response is None):
        return 0 # 0 si auth pas bonne
    else:
        for (id,nom,prenom) in cursor:
            Session()["nom"]=nom
            Session()["prenom"]=prenom
            Session()["id"]=id
        close_BD(cursor, cnx)
    return 1 # 1 si authentification ok
