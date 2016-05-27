template = Import('/IENAC15/beldjilali_garcia_raby_ranaivoharison/python/template.py')
bdd = Import('/IENAC15/beldjilali_garcia_raby_ranaivoharison/python/bddamap.py')


def formulaire():
    """renvoie le code html d'une ligne du formulaire de création de panier"""
    tab_produit = bdd.selectProduitsAgriculteur(Session()["id"])
    # tab_produit = bdd.selectProduit()
    formulaire = '''
    <form id="form2" name="newpanier" method="post" action="/IENAC15/beldjilali_garcia_raby_ranaivoharison/python/PageAgriculteur/CreatPanier.py/envoyerProduit_Panier" enctype="multipart/form-data">
        <input type="text" name="date" value="Entrer date de validité"/>
    <div class="container col-md-12">

         <div class=" col-md-6">
            <style>
                table{border-collapse:collapse;}
                table,td,tr,th{border:1px solid black; padding:10px; }
              </style>
            <section id="prod">
        <div class="row  ">
        <table class="table "
        data-toggle="table" data-search="true" data-pagination="true" data-page-size="3">
             <thead>
                 	
                 <th data-field="type" data-sortable="true">Type</th>
                 <th data-field="variete" data-sortable="true">Variété</th>
                 <th data-field="description" data-sortable="true">Description</th>
                 <th data-field="prix" data-sortable="true">Prix au kg</th>
                 <th data-field="photo" data-sortable="true">Photo</th>
            </thead>
            <tbody>'''

    for row in tab_produit:
        formulaire += '<tr>'

        formulaire += '<td>' + str(row[1]) + '</td>'
        formulaire += '<td>' + str(row[2]) + '</td>'
        formulaire += '<td>' + str(row[3]) + '</td>'
        formulaire += '<td>' + str(row[4]) + '</td>'
        formulaire += '<td>' + str(row[5]) + '</td>'
        formulaire += '<td>' + str(row[6]) + '</td>'
        formulaire += '</tr>'

    formulaire += '''
        </tbody>
    </table>
     </div>
     </section>
     </div>



    <div class="container col-md-6">

            <select name="nom_produit">
                <optgroup label="Produit">'''
    for rows in tab_produit:
        formulaire += '''<option value="''' + str(rows[1]) + '''">''' + str(rows[1]) + '''</option>'''
    formulaire += '''
                </optgroup>
            </select>
            <input type="int" name="qte" value="Entrer quantité"/>
            <button type="submit"  > >
        </form>
    </div>

    <style>
                table{border-collapse:collapse;}
                table,td,tr,th{border:1px solid black; padding:10px; }
              </style>
            <section id="prod">
        <div class="row  ">
        <table class="table "
        data-toggle="table" data-search="true" data-pagination="true" data-page-size="3">
             <thead>
                 <th data-field="nom" data-sortable="true">Nom</th>
                 <th data-field="type" data-sortable="true">Quantité</th>
                 <th data-field="variete" data-sortable="true">Supprimer du panier</th>
            </thead>
            <tbody>'''
    panier_agri = bdd.selectPanierAgriculteur(Session()["id"])  # Pb si pas encore de panier

    id_panier = panier_agri[0]
    produits_qte = bdd.selectProduitPanier(id_panier)
    for i in range(len(produits_qte)):
        id_produit = bdd.getIdProduitFromNomProduit(produits_qte[i][0])[0]
        formulaire += '''<tr>'''
        formulaire += '''<td>''' + str(produits_qte[i][0]) + '''</td>'''
        formulaire += '''<td>''' + str(produits_qte[i][1]) + '''</td>'''
        formulaire += '''<td><a href="/IENAC15/beldjilali_garcia_raby_ranaivoharison/python/PageAgriculteur/CreatPanier.py/deleteProduitPanier?id_panier=''' + str(
            id_panier) + ''';id_produit=''' + str(id_produit) + '''"> X </a></td>'''
        formulaire += '''</tr>'''
    formulaire += '''
            </tbody>
    </table>
     </div>
     </section>

    </div>
		  '''
    return formulaire


def CreatPanier():
    result = template.head()
    result += template.nav()
    result += template.header()
    result += formulaire()
    result += template.footer()
    return result


def envoyerProduit_Panier(qte='', date='', prix='0.0', nom_produit=''):
    """Envoie qte produit nom_produit dans le panier de l'agriculteur qui est connecté"""
    panier_agri = bdd.selectPanierAgriculteur(Session()["id"])  # Un panier par agriculteur
    id_produit = bdd.id_produitFromNom_Produit(nom_produit)[0]
    bdd.insertDetailPanier(qte, panier_agri[0], id_produit)
    return CreatPanier()


def deleteProduitPanier(id_panier, id_produit):
    """Supprime le produit id_produit du panier id_panier"""
    cnx = bdd.connect_BD()
    cursor = cnx.cursor()
    query = (
    "DELETE FROM `IENAC15_beldjilali_garcia_raby_ranaivoharison`.`detail_panier_type` WHERE (id_panier_type = '" + str(
        id_panier) + "') and (id_produit = '" + str(id_produit) + "')")
    cursor.execute(query)
    cnx.commit()
    bdd.close_BD(cursor, cnx)
    return CreatPanier()
