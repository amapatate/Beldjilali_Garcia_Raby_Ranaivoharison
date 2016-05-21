template = Import('/IENAC15/beldjilali_garcia_raby_ranaivoharison/python/template.py')


def NewAcount():
    result = template.head()
    result += template.header()
    result += template.nav()
    result += formulaire()
    result += template.footer()
    return result


def formulaire():
    formulaire = '''
<div class="container form">
    <h2 class="col-md-12">Inscription</h2>
    <form id="form1" name="inscription " method="post" action="/IENAC15/beldjilali_garcia_raby_ranaivoharison/python/pythonamap.py/creerCompte" enctype="multipart/form-data">
       <div class="col-md-12">
        <label class="col-md-6"> Civilité:</label>
        <section class="col-md-6">
          <select name="civilite">
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
        <section class="col-md-6">
          <input type="text" name="nom"  required/>
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
          <button type="submit">Envoyer</button>
      </div>
  </div>'''
    return formulaire
