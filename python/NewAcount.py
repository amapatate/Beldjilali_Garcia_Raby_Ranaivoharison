template= Import('/IENAC15/beldjilali_garcia_raby_ranaivoharison/python/template.py')

def formulaire():
    formulaire='''
<div class="container form">
    <h2 class="col-md-12">Formulaire</h2>
    <form id="form1" name="inscription " method="post" action="/IENAC15/beldjilali_garcia_raby_ranaivoharison/python/pythonamap.py/creercompte" enctype="multipart/form-data">
       <div class="col-md-12">
        <label class="col-md-6"> Type de compte:</label>
        <section class="col-md-6">
          <select name="role">
            <optgroup label= "Acteur">
                <option value="1">Agriculteur</option>
                <option value="2">Client</option>
            </optgroup>
          </select>
        </section>
      </div>
      <div class="col-md-12">
        <label class="col-md-6">Nom:</label>
        <section class="col-md-6">
          <input type="text" name="nom" />
        </section>
      </div>
      <div class="col-md-12">
        <label class="col-md-6">Prénom:</label>
        <section class="col-md-6">
          <input type="text" name="prenom"/>
        </section>
      </div>
      <div class="col-md-12">
        <label class="col-md-6">Adresse mail:</label>
        <section class="col-md-6">
          <input type="text" name="email"/>
        </section>
      </div>
      <div class="col-md-12">
        <label class="col-md-6">Adresse:</label>
        <section class="col-md-6">
          <input type="text" name="adresse"/>
        </section>
      </div>
      <div class="col-md-12">
        <label class="col-md-6">Mot de passe:</label>
        <section class="col-md-6">
          <input type="password" name="mdp"/>
        </section>
      </div>
      <div class="col-md-12">
        <label class="col-md-6">Confirmation mot de passe:</label>
        <section class="col-md-6">
          <input type="password" name="cmdp"/>
        </section>
      </div>
      <div class="col-md-12">
          <button type="submit">Envoyer</button>
      </div>
  </div>'''
    return formulaire


def NewAcount():
    result= template.head()
    result+= template.nav()
    result+= template.header()
    result+= formulaire()
    result+= template.footer()
    return result
