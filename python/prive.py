

def index():
    if "id" in Session() and Session()["id"] != '':
        msg="Bienvenue sur votre page privée "+Session()["prenom"]+ " "+Session()["nom"]
        msg+="<br /><a href='/IENAC15/beldjilali_garcia_raby_ranaivoharison/python/prive.py/deconnect'>Se déconnecter</a>"
    else:
        raise HTTP_REDIRECTION('/IENAC15/beldjilali_garcia_raby_ranaivoharison/index.py/index')
    return msg

def deconnect():
    if "id" in Session() and Session()["id"] !='':# si la session existe on la supprime
        del Session()["nom"]
        del Session()["prenom"]
        del Session()["id"]
    raise HTTP_REDIRECTION('/IENAC15/beldjilali_garcia_raby_ranaivoharison/index.py/index')
    return

