template = Import('/IENAC15/beldjilali_garcia_raby_ranaivoharison/python/template.py')
bdd = Import('/IENAC15/beldjilali_garcia_raby_ranaivoharison/python/bddamap.py')


def clients():
    """Fonction qui renvoie le html affichant les clients de l agriculteur name"""
    liste_clients = bdd.selectClientsAgri(Session()["id"])
    if len(liste_clients) == 0:
        # Pas de client
        clients = '''
    <section>
    <div class="container">
		  <style>
    	  				table{border-collapse:separate; border-spacing:10px}
    	  				table,td,tr{border:0px; padding:10px}
    	  				table th { padding:10px; border-radius:10px; background-color:1b4837}
    	  				table thead {color:#44B78B}
    	  	</style>
        <div class="row">
            <caption>
                <h2>Vos clients</h2>
            </caption>
            <p>T'as pas de client, tu pues</p>
        </div>
        '''
    else:
        clients = '''
	<section>
    <div class="container">
		  <style>
    	  				table{border-collapse:separate; border-spacing:10px}
    	  				table,td,tr{border:0px; padding:10px}
    	  				table th { padding:10px; border-radius:10px; background-color:1b4837}
    	  				table thead {color:#44B78B}
    	  	</style>
        <div class="row">
            <caption>
                <h2>Vos clients</h2>
            </caption>
        </div>

    <div class="row">
    <center>
    <table class="table table-responsive table-bordered table-striped table-condensed"
    data-toggle="table" data-search="true" data-pagination="true" data-page-size="3">
         <thead>
         <th data-field="nom" data-sortable="true">Nom</th>
         <th data-field="prenom" data-sortable="true">Prenom</th>
         <th data-field="telephone" data-sortable="true">Telephone</th>
         <th data-field="email" data-sortable="true">Email</th>
         <th data-field="adresse" data-sortable="true">Adresse</th>
        <thead>
        <tbody>
	'''
    for row in liste_clients:
        clients += '<tr>'
        clients += '<td>' + str(row[0]) + '</td>'
        clients += '<td>' + str(row[1]) + '</td>'
        clients += '<td>' + str(row[2]) + '</td>'
        clients += '<td>' + str(row[0]) + '</td>'
        clients += '<td>' + str(row[0]) + '</td>'
        clients += '</tr>'
    clients += '''
		</tbody>
   </table>
   </center>
    

     </div>
     </div>
    </section>
   '''
    return clients


def MyClient():
    result = template.head()
    result += template.nav()
    result += template.header()
    result += clients()
    result += template.footer()
    return result
