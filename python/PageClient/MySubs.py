template = Import('/IENAC15/beldjilali_garcia_raby_ranaivoharison/python/template.py')
bdd = Import('/IENAC15/beldjilali_garcia_raby_ranaivoharison/python/bddamap.py')


def Abo():
    paniers = bdd.selectPanierType()
    abo = '''
    <section class"container">
    <form id="form2" name="" method="post" action="" enctype="multipart/form-data">
    	<div class=" col-md-6">'''
    for panier in paniers:
        abo += '''
      <center>
      <div class=" col-md-4">
            <style>
                table{border-collapse:separate ;border-spacing:10px;text-align:center;color:white;margin-bottom:10px}
                tr,th{border:0; padding:10px; }
                td{border:1px;border-radius:10px;background-color:#44B78B;padding:10px}
                table {border:1px;border-radius:30px; background-color:1b4837}
            </style>
            <section id="prod">
        <div class="row">
        <center>
        <table data-toggle="table" data-search="true" data-pagination="true" data-page-size="3">
            <thead>
            	<tr>
            		<th data-field="nom" data-sortable="true">Appartient à : </th>
            		<th data-field="nom" data-sortable="true">''' + str(
            bdd.getNomPrenomAgriFromId(panier[1])[0]) + ' ' + bdd.getNomPrenomAgriFromId(panier[1])[1] + '''</th>
               </tr>
            </thead>
            <tbody>'''
        produits = bdd.selectProduitPanier(panier[0])
        for produit in produits:
            abo += '''<tr>'''
            abo += '''<td>''' + str(produit[0]) + '''</td>'''
            abo += '''<td>''' + str(produit[1]) + '''</td>'''
            abo += '''</tr>'''
        abo += '''
            </tbody>
         </table>
         </center>
         </div>
         </section>
         </div>
         <div class="abo col-md-2" style="text-align:center;">
          	<a href="/IENAC15/beldjilali_garcia_raby_ranaivoharison/python/PageClient/MySubs.py/insertSubs?id_client=''' + str(
            Session()["id"]) + ''';id_panier=''' + str(panier[0]) + '''"> S'Abonner </a>
          </div>
          </center>
          '''

    paniers_client = bdd.selectPanierClient(Session()["id"])
    abo += '''
			</div>
          <div class=" col-md-6">
          <h2> Vous êtes abonné aux paniers:</h2>'''
    for panier in paniers_client:
        agri = bdd.getNomPrenomAgriFromId(panier[1])
        abo += '''
              
              <section id="prod">
                <div class="row  ">
                <center>
                   <table class="table "
                   data-toggle="table" data-search="true" data-pagination="true" data-page-size="3">
                       <thead>
                          <th data-field="nom" data-sortable="true">''' + str(agri[0]) + ' ' + str(agri[1]) + '''</th>
                          <th class="delete" data-field="nom" data-sortable="true"> <a href="/IENAC15/beldjilali_garcia_raby_ranaivoharison/python/PageClient/MySubs.py/deleteSubs?id=''' + str(
            panier[2]) + '''"> X </a></th>
                        </thead>
                   </table>
                 </center>
                 </div>
               </section>'''
    abo += '''
          </div>
        </section>
		  '''
    return abo


def MySubs():
    result = template.head()
    result += template.nav()
    result += template.header()
    result += Abo()
    result += template.footer()
    return result


def insertSubs(id_client, id_panier):
    cnx = bdd.connect_BD()
    query = (
    "INSERT INTO `IENAC15_beldjilali_garcia_raby_ranaivoharison`.`abonne` (id_client, id_panier_type) VALUES (%s, %s);")
    param = (id_client, id_panier)
    # try:
    cursor = cnx.cursor()
    cursor.execute(query, param)
    cnx.commit()
    # except:
    #    cnx.rollback()
    bdd.close_BD(cursor, cnx)
    return MySubs()


def deleteSubs(id):
    cnx = bdd.connect_BD()
    cursor = cnx.cursor()
    query = ("DELETE FROM `IENAC15_beldjilali_garcia_raby_ranaivoharison`.`abonne` WHERE id = '" + str(id) + "'")
    cursor.execute(query)
    cnx.commit()
    bdd.close_BD(cursor, cnx)
    return MySubs()
