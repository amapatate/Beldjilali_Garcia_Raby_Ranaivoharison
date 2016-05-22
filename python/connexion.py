template = Import('/IENAC15/beldjilali_garcia_raby_ranaivoharison/python/template.py')
# lg = Import('/IENAC15/beldjilali_garcia_raby_ranaivoharison/python/login.py')
bdd = Import('/IENAC15/beldjilali_garcia_raby_ranaivoharison/python/bddamap.py')
def connexion():
    result = template.head()
    result += template.header()
    result += template.nav()
    # result+= verifierCompte(login='', pwd='')
    result += formulaire()
    result += template.footer()
    return result





def formulaire():
    formulaire = '''

<div class="container form">
    <h2 class="col-md-12">Connexion</h2>
 <!--<form id="auth" name="connexion" method="post" action="verifierCompte" enctype="multipart/form-data">-->
    <div id="msg"></div>
<form id="auth" enctype="multipart/form-data" action="verifierCompte">
      <div class="col-md-12">
        <label class="col-md-6">Adresse mail:</label>
        <section class="col-md-6">
          <input type="text" name="login" required/>
        </section>
      </div>

      <div class="col-md-12">
        <label class="col-md-6">Mot de passe:</label>
        <section class="col-md-6">
          <input type="password" name="pwd" required/>
        </section>
      </div>

      <div class="col-md-12">
          <button type="submit">Envoyer</button>
      </div>

      </form>
</div>'''
    return formulaire


def verifierCompte(login='', pwd=''):
    result = ''
    result += "les données envoyées sont:<br /> email:" + login
    result += " <br /> mdp:" + pwd
    result += " <br /> l'authentification est OK si on a 1 :" + str(bdd.gestionLogin(login,pwd))
    return result

