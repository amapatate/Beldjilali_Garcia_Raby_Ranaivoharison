template = Import('/IENAC15/beldjilali_garcia_raby_ranaivoharison/python/template.py')
bdd = Import('/IENAC15/beldjilali_garcia_raby_ranaivoharison/python/bddamap.py')

def newAccount(mode):
    result = template.head()
    result += template.nav()
    result += template.header()
    result += formulaire(mode)
    result += template.footer()
    return result


def formulaire(mode):
    """formulaire d'inscription
    si mode = 1 -> formulaire de base
    si mode = 0 -> email existant"""
    if mode == '1':
        formulaire = '''
<div class="container form">
    <h2 class="col-md-12">Inscription</h2>
    <form class="entre" 	id="form1" name="inscription " method="post" action="/IENAC15/beldjilali_garcia_raby_ranaivoharison/python/newAccount.py/creerCompte" enctype="multipart/form-data">
       <div class="col-md-12">
        <label class="col-md-6"> Civilité:</label>
        <section class="col-md-6">
          <select class="roll" name="civilite">
            <optgroup label= "Civilité">
                <option value="Madame">Madame</option>
                <option value="Mademoiselle">Mademoiselle</option>
                <option value="Monsieur">Monsieur</option>
            </optgroup>
          </select>
        </section>
      </div>
      <div class="col-md-12"> 
        <label class="col-md-6">Nom:</label>
        <section class="col-md-6 " >
          <input   type="text" name="nom"  required/>
        </section>      
      </div>
      <div class="col-md-12">
        <label class="col-md-6">Prénom:</label>
        <section class="col-md-6">
          <input type="text" name="prenom" required/>
        </section>
      </div>
      <div class="col-md-12">
        <label class="col-md-6">Téléphone:</label>
        <section class="col-md-6">
          <input type="text" name="telephone" required/>
        </section>
      </div>
      <div class="col-md-12">
        <label class="col-md-6">Adresse mail:</label>
        <section class="col-md-6">
          <input type="text" name="email" required/>
        </section>
      </div>
      <div class="col-md-12">
        <label class="col-md-6">Adresse:</label>
        <section class="col-md-6">
          <input type="text" name="adresse"  required/>
        </section>
      </div>
      <div class="col-md-12">
        <label class="col-md-6">Mot de passe:</label>
        <section class="col-md-6">
          <input type="password" name="mdp" required/>
        </section>
      </div>
      <div class="col-md-12">
        <label class="col-md-6">Confirmation mot de passe:</label>
        <section class="col-md-6">
          <input type="password" name="cmdp"  required/>
        </section>
      </div>
      <div class="col-md-12">
          <button class="bouton" type="submit">Envoyer</button>
      </div>
  </div>'''
    elif mode == '0':
        formulaire = '''
<p>email déjà utilisé</p>
<div class="container form">
    <h2 class="col-md-12">Inscription</h2>
    <form class="entre" 	id="form1" name="inscription " method="post" action="/IENAC15/beldjilali_garcia_raby_ranaivoharison/python/newAccount.py/creerCompte" enctype="multipart/form-data">
       <div class="col-md-12">
        <label class="col-md-6"> Civilité:</label>
        <section class="col-md-6">
          <select class="roll" name="civilite">
            <optgroup label= "Civilité">
                <option value="Madame">Madame</option>
                <option value="Mademoiselle">Mademoiselle</option>
                <option value="Monsieur">Monsieur</option>
            </optgroup>
          </select>
        </section>
      </div>
      <div class="col-md-12">
        <label class="col-md-6">Nom:</label>
        <section class="col-md-6 " >
          <input   type="text" name="nom"  required/>
        </section>
      </div>
      <div class="col-md-12">
        <label class="col-md-6">Prénom:</label>
        <section class="col-md-6">
          <input type="text" name="prenom" required/>
        </section>
      </div>
      <div class="col-md-12">
        <label class="col-md-6">Téléphone:</label>
        <section class="col-md-6">
          <input type="text" name="telephone" required/>
        </section>
      </div>
      <div class="col-md-12">
        <label class="col-md-6">Adresse mail:</label>
        <section class="col-md-6">
          <input type="email" name="email" required/>
        </section>
      </div>
      <div class="col-md-12">
        <label class="col-md-6">Adresse:</label>
        <section class="col-md-6">
          <input type="text" name="adresse"  required/>
        </section>
      </div>
      <div class="col-md-12">
        <label class="col-md-6">Mot de passe:</label>
        <section class="col-md-6">
          <input type="password" name="mdp" required/>
        </section>
      </div>
      <div class="col-md-12">
        <label class="col-md-6">Confirmation mot de passe:</label>
        <section class="col-md-6">
          <input type="password" name="cmdp"  required/>
        </section>
      </div>
      <div class="col-md-12">
          <button class="bouton" type="submit">Envoyer</button>
      </div>
  </div>'''

    return formulaire


def creerCompte(civilite='', nom='', prenom='', telephone='', email='', adresse='', mdp='', cmdp=''):
    result = template.head()
    result += template.nav()
    result += template.header()
    result += donneesEnvoyees(str(bdd.insertAccount(civilite, nom, prenom, telephone, email, adresse, mdp)))
    result += template.footer()

    return result


def donneesEnvoyees(mode):
    """mode = 0 -> email existant
    mode = 1 -> Bienvenue"""
    if mode == '1':
        result = 'Bienvenue <br />'
        result += "les données envoyées sont:<br /> nom:" + nom
        result += " <br /> civilité:" + civilite
        result += " <br /> Prénom:" + prenom
        result += " <br /> email:" + email
        result += " <br /> adresse:" + adresse
    elif mode == '0':
        result = formulaire(mode)
    return result
