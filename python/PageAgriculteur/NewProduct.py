template = Import('../template.py')
bdd = Import('/IENAC15/beldjilali_garcia_raby_ranaivoharison/python/bddamap.py')


def formulaire():
    formulaire = '''
<div class="container form">
    <h2 class="col-md-12">Qu'avez-vous de bon à nous proposer ?</h2>
    <form class="entre" id="form1" name="inscription " method="post" action="/IENAC15/beldjilali_garcia_raby_ranaivoharison/python/PageAgriculteur/NewProduct.py/ajouterProduit" enctype="multipart/form-data">
      <div class="col-md-12">
        <label class="col-md-6"> Type:</label>
        <section class="col-md-6">
          <select class="roll" name="type">
            <optgroup label= "Type">
                <option value="legume">Légume</option>
                <option value="fruit">Fruit</option>
                <option value="feculent">Féculent</option>
            </optgroup>
          </select>
        </section>
      </div>
      <div class="col-md-12">
        <label class="col-md-6">Nom:</label>
        <section class="col-md-6">
          <input type="text" name="nom" placeholder="Ex:Patate"  required/>
        </section>
      </div>
      <div class="col-md-12">
        <label class="col-md-6">Variété:</label>
        <section class="col-md-6">
          <input type="text"placeholder="Ex:Carlita" name="variete" required/>
        </section>
      </div>
      <div class="col-md-12">
        <label class="col-md-6">Déscription:</label>
        <section class="col-md-6">
          <input type="text" placeholder="Ex: Pour les raclettes" name="description" required/>
        </section>
      </div>
      <div class="col-md-12">
        <label class="col-md-6">Prix/kg:</label>
        <section class="col-md-6">
          <input type="float" placeholder="Ex:4" name="prix_kg" required/>
        </section>
      </div>
      <div class="col-md-12">
          <button class="bouton" type="submit">Envoyer</button>
      </div>
  </div>'''
    return formulaire


def NewProduct():
    result = template.head()
    result += template.nav()
    result += template.header()
    result += formulaire()
    result += template.footer()
    return result


def ajouterProduit(type='', nom='', variete='', description='', prix_kg=''):
    result = template.head()
    result += template.nav()
    result += template.header()
    result += 'produit ajouté'
    result += template.footer()
    bdd.insertProduit(nom, type, variete, description, prix_kg, Session()["id"])
    return result
