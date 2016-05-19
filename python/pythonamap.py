bdd = Import('/IENAC15/AMAP/python/bddamap.py')
template = Import('template.py')

def  creercompte(role='', nom='', prenom='', email='', adresse='', mdp='', cmdp=''):
    result = template.head()
    result += template.nav()
    result += template.header()
    result+=afficheCompte(nom, prenom, email, adresse)
    result += template.footer()
    bdd.insertAccount(nom, prenom, email, adresse, mdp)
    #Session()["mail"]=email
    return result
    
    
def afficheCompte(name='', surname='', email='', adresse=''):
    result = ''
    result += "les données envoyées sont:<br /> nom:"+name
    result += " <br /> Prénom:"+surname
    result += " <br /> email:"+email
    result += " <br /> adresse:"+adresse

    return result
