template = Import('/IENAC15/beldjilali_garcia_raby_ranaivoharison/python/template.py')


def connexion(mode):
    result = template.head()
    result += template.nav()
    result += template.header()
    result += formulaire(mode)
    result += template.footer()
    return result


def formulaire(mode):
    """mode = 0 -> email/mdp incorrect
    mode = 1 -> formulaire de base"""
    if mode == '1' :
        formulaire = '''
        
<div class="container form">
    <h2 class="col-md-12">Connexion</h2>
    <div id="msg"></div>
<form class="entre" id="auth" enctype="multipart/form-data" action="/IENAC15/beldjilali_garcia_raby_ranaivoharison/python/login.py/index">
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
          <button class="bouton" type="submit">Envoyer</button>
      </div>

      </form>
</div>'''
    elif mode == '0':
        formulaire ='''

<div class="container form">
    <h2 class="col-md-12" style="color:#FF0000;">Votre Adresse mail ou votre mot de passe est incorrect</h2>      
<form  class="entre" id="auth" enctype="multipart/form-data" action="/IENAC15/beldjilali_garcia_raby_ranaivoharison/python/login.py/index">
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
          <button class="bouton" type="submit">Envoyer</button>
      </div>
      </form>
</div>'''
    return formulaire