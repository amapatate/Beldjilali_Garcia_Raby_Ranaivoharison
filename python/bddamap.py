import mysql.connector

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


# insertion dans la bdd
def insertAccount(civilite='', nom='', prenom='', telephone='', email='', adresse='', mdp=''):
    """Insère un compte s'il n'existe pas déjà
    Renvoie 1 si action effectuée, 0 sinon"""
    liste_clients = selectClient()
    compteExistant = False  # booléen indiquant si le compte existe ou pas
    for client in liste_clients:
        if (email in client):
            compteExistant = True
    if compteExistant:
        return 0
    else:
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
        return 1


def insertPanierType(id_agri, date, prix_mensuel):
    cnx = connect_BD()
    query = (
    "INSERT INTO `IENAC15_beldjilali_garcia_raby_ranaivoharison`.`panier_type` (id_agriculteur, date_validite, prix_abo_mensuel) VALUES (%s, %s, %s);")
    param = (id_agri, date, prix_mensuel)
    # try:
    cursor = cnx.cursor()
    cursor.execute(query, param)
    cnx.commit()
    # except:
    #    cnx.rollback()
    close_BD(cursor, cnx)


def insertDetailPanier(qte_produit, id_panier, id_produit):
    """Insère un detail_panier_type en prenant en compte le fait qu'un produit y soit déjà ou pas"""
    nom_produit = nom_produitFromId_Produit(id_produit)[0]
    produits_qte = selectProduitPanier(id_panier)
    produitDsPanier = False
    for (nom, _) in produits_qte:
        if nom == nom_produit:
            produitDsPanier = True
    if produitDsPanier:
        cnx = connect_BD()
        query = (
        "UPDATE `IENAC15_beldjilali_garcia_raby_ranaivoharison`.`detail_panier_type` SET qte_produit = '" + str(
            qte_produit) + "' WHERE id_produit = '" + str(id_produit) + "'")
        cursor = cnx.cursor()
        cursor.execute(query)
        cnx.commit()
        close_BD(cursor, cnx)
    else:
        cnx = connect_BD()
        query = (
        "INSERT INTO `IENAC15_beldjilali_garcia_raby_ranaivoharison`.`detail_panier_type` (qte_produit, id_panier_type, id_produit) VALUES (%s, %s, %s);")
        param = (qte_produit, id_panier, id_produit)
        cursor = cnx.cursor()
        cursor.execute(query, param)
        cnx.commit()
        close_BD(cursor, cnx)


def insertProduit(nom='', type='', variete='', description='', prix_kg='', id_agriculteur=''):
    cnx = connect_BD()
    query = (
        "INSERT INTO `IENAC15_beldjilali_garcia_raby_ranaivoharison`.`produit` (nom, type, variete, description, prix_kg, id_agriculteur) VALUES (%s, %s, %s, %s, %s, %s);")
    param = (nom, type, variete, description, prix_kg, id_agriculteur)
    try:
        cursor = cnx.cursor()
        cursor.execute(query, param)
        cnx.commit()
    except:
        cnx.rollback()
    close_BD(cursor, cnx)


def insertSubs(id_client, id_panier):
    cnx = connect_BD()
    query = (
    "INSERT INTO `IENAC15_beldjilali_garcia_raby_ranaivoharison`.`abonne` (id_client, id_panier_type) VALUES (%s, %s);")
    param = (id_client, id_panier)
    # try:
    cursor = cnx.cursor()
    cursor.execute(query, param)
    cnx.commit()
    # except:
    #    cnx.rollback()
    close_BD(cursor, cnx)





    # Obtention des données de la bdd


def selectClient():
    cnx = connect_BD()
    cursor = cnx.cursor()
    query = ("SELECT  * FROM `IENAC15_beldjilali_garcia_raby_ranaivoharison`.`client`")
    cursor.execute(query)
    rows = cursor.fetchall()
    close_BD(cursor, cnx)
    return rows


def selectProduit():
    cnx = connect_BD()
    cursor = cnx.cursor()
    query = (
    "SELECT produit.id,produit.nom,type,variete,description,prix_kg,agriculteur.prenom,agriculteur.nom,produit.photo FROM produit INNER JOIN agriculteur ON id_agriculteur=agriculteur.id")
    cursor.execute(query)  # envoi de la requete
    rows = cursor.fetchall()  # réception des données sous forme de liste
    close_BD(cursor, cnx)
    return rows


def selectAgri():
    cnx = connect_BD()
    cursor = cnx.cursor()
    query = ("SELECT nom,prenom,telephone,email,adresse,presentation,photo FROM agriculteur")
    cursor.execute(query)  # envoi de la requete
    rows = cursor.fetchall()  # réception des données sous forme de liste
    close_BD(cursor, cnx)
    return rows


def selectPanierType():
    cnx = connect_BD()
    cursor = cnx.cursor()
    query = ("SELECT * FROM `IENAC15_beldjilali_garcia_raby_ranaivoharison`.`panier_type`")
    cursor.execute(query)
    rows = cursor.fetchall()
    close_BD(cursor, cnx)
    return rows


def selectPanierAgriculteur(id_agri):
    """renvoie LE panier de l'agriculteur identifie par id_agri"""
    cnx = connect_BD()
    cursor = cnx.cursor()
    query = (
    "SELECT * FROM `IENAC15_beldjilali_garcia_raby_ranaivoharison`.`panier_type` WHERE id_agriculteur = '" + str(
        id_agri) + "'")
    cursor.execute(query)
    panier = cursor.fetchone()  # tuple (1, id_agri, ...)
    close_BD(cursor, cnx)
    return panier


def selectProduitsAgriculteur(id_agri):
    """Renvoie la liste des produits dont l'id_agriculteur correspon à l'id de l'agriculteur connecte"""
    cnx = connect_BD()
    cursor = cnx.cursor()
    query = (
    "SELECT id,nom,type,variete,description,prix_kg,photo FROM produit WHERE id_agriculteur = '" + str(id_agri) + "'")
    cursor.execute(query)  # envoi de la requete
    rows = cursor.fetchall()  # réception des données sous forme de liste
    close_BD(cursor, cnx)
    return rows


def getNomPrenomAgriFromId(id_agri):
    """Renvoie nom et prénom de l'agriculteur id_agri"""
    cnx = connect_BD()
    cursor = cnx.cursor()
    query = ("SELECT nom, prenom FROM `IENAC15_beldjilali_garcia_raby_ranaivoharison`.`agriculteur` WHERE id = '" + str(
        id_agri) + "'")
    cursor.execute(query)
    nom_prenom = cursor.fetchone()
    close_BD(cursor, cnx)
    return nom_prenom


def selectPanierClient(id_client):
    """Renvoie la liste des paniers (id, id_agri, id_abonne) auxquels le client est abonné"""
    cnx = connect_BD()
    cursor = cnx.cursor()
    query = (
    "SELECT panier.id, id_agriculteur, abonne.id FROM (`IENAC15_beldjilali_garcia_raby_ranaivoharison`.`abonne` as abonne JOIN `IENAC15_beldjilali_garcia_raby_ranaivoharison`.`panier_type` as panier ON id_panier_type = panier.id) WHERE id_client = '" + str(
        id_client) + "'")
    cursor.execute(query)
    list_panier = cursor.fetchall()
    close_BD(cursor, cnx)
    return list_panier


def selectClientsAgri(id_agri):
    """Renvoie la liste des clients d'id_agri"""
    cnx = connect_BD()
    cursor = cnx.cursor()
    query = ("SELECT client.nom, client.prenom, client.telephone, client.email, client.adresse FROM "
             "((`IENAC15_beldjilali_garcia_raby_ranaivoharison`.`client` as client INNER JOIN  "
             "`IENAC15_beldjilali_garcia_raby_ranaivoharison`.`abonne` as abonne ON client.id = abonne.id_client) INNER JOIN "
             "`IENAC15_beldjilali_garcia_raby_ranaivoharison`.`panier_type` as panier ON abonne.id_panier_type = panier.id) INNER JOIN"
             "`IENAC15_beldjilali_garcia_raby_ranaivoharison`.`agriculteur` as agri ON agri.id = panier.id_agriculteur WHERE agri.id = '" + str(
        id_agri) + "'")
    cursor.execute(query)
    list_clients = cursor.fetchall()
    close_BD(cursor, cnx)
    return list_clients


def id_produitFromNom_Produit(nom_produit):
    """Renvoie l'id_produit à partir du nom_produit"""
    cnx = connect_BD()
    cursor = cnx.cursor()
    query = (
    "SELECT id FROM `IENAC15_beldjilali_garcia_raby_ranaivoharison`.`produit` WHERE nom = '" + nom_produit + "' LIMIT 1")
    cursor.execute(query)
    id_produit = cursor.fetchone()
    close_BD(cursor, cnx)
    return id_produit


def nom_produitFromId_Produit(id_produit):
    """Renvoie le nom_produit à partir de l'id_produit"""
    cnx = connect_BD()
    cursor = cnx.cursor()
    query = ("SELECT nom FROM `IENAC15_beldjilali_garcia_raby_ranaivoharison`.`produit` WHERE id = '" + str(
        id_produit) + "' LIMIT 1")
    cursor.execute(query)
    id_produit = cursor.fetchone()
    close_BD(cursor, cnx)
    return id_produit


def selectProduitPanier(id_panier):
    """Renvoie les (nom, qte) des produits présents dans le panier id_panier"""
    cnx = connect_BD()
    cursor = cnx.cursor()
    query = (
    "SELECT nom, qte_produit FROM (`IENAC15_beldjilali_garcia_raby_ranaivoharison`.`produit` as produit JOIN `IENAC15_beldjilali_garcia_raby_ranaivoharison`.`detail_panier_type` as detail_panier_type ON produit.id = id_produit) JOIN `IENAC15_beldjilali_garcia_raby_ranaivoharison`.`panier_type` as panier_type ON id_panier_type = panier_type.id WHERE id_panier_type = '" + str(
        id_panier) + "'")
    cursor.execute(query)
    produits_qte = cursor.fetchall()
    close_BD(cursor, cnx)
    return produits_qte


def getIdProduitFromNomProduit(nom_produit):
    """Renvoie l'id du produit à partir de son nom"""
    cnx = connect_BD()
    cursor = cnx.cursor()
    query = (
    "SELECT id FROM `IENAC15_beldjilali_garcia_raby_ranaivoharison`.`produit` WHERE nom = '" + str(nom_produit) + "'")
    cursor.execute(query)
    id_produit = cursor.fetchone()
    close_BD(cursor, cnx)
    return id_produit
