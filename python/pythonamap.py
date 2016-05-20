bdd = Import('/IENAC15/beldjilali_garcia_raby_ranaivoharison/python/bddamap.py')
template = Import('/IENAC15/beldjilali_garcia_raby_ranaivoharison/python/template.py')


def  creerCompte(civilite='', nom='', prenom='', email='', adresse='', mdp='', cmdp=''):
    result = template.head()
    result += template.nav()
    result += template.header()
    result+=afficherCompte(civilite, nom, prenom, email, adresse, mdp)
    result += template.footer()
    bdd.insertAccount(civilite, nom, prenom, email, adresse, mdp)
    #Session()["mail"]=email
    return result
    
    
def afficherCompte(civilite='', nom='', prenom='', email='', adresse='', mdp=''):
    result = ''
    result += "les données envoyées sont:<br /> nom:"+nom
    result += " <br /> civilité:"+ civilite
    result += " <br /> Prénom:"+ prenom
    result += " <br /> email:"+email
    result += " <br /> adresse:"+adresse

    return result





def  saisirPanierType(select='', name='', surname='', email='', adresse=''):
    result = template.head()
    result += template.nav()
    result += template.header()
    result+=afficherCompte(name, surname, email, adresse)
    result += template.footer()
    bdd.insertClient(name, surname, email, adresse)
    #Session()["mail"]=email
    return result






        