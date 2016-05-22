template = Import('/IENAC15/beldjilali_garcia_raby_ranaivoharison/python/template.py')


def connexion():
    result = template.head()
    result += template.header()
    result += template.nav()
    result += formulaire()
    result += template.footer()
    return result


def formulaire():
    formulaire = '''
<div class="container form">
    <h2 class="col-md-12">Connexion</h2>
    <form id="auth" >

      <div class="col-md-12">
        <label class="col-md-6">Adresse mail:</label>
        <section class="col-md-6">
          <input type="email" name="email" required/>
        </section>
      </div>

      <div class="col-md-12">
        <label class="col-md-6">Mot de passe:</label>
        <section class="col-md-6">
          <input type="password" name="mdp" required/>
        </section>
      </div>

      <div class="col-md-12">
          <button type="submit">Envoyer</button>
      </div>

      </form>
</div>'''
    return formulaire
