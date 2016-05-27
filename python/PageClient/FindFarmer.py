template = Import('/IENAC15/beldjilali_garcia_raby_ranaivoharison/python/template.py')
bdd = Import('/IENAC15/beldjilali_garcia_raby_ranaivoharison/python/bddamap.py')


def Farmer():
    tab_agri = bdd.selectAgri()
    # affichage du tableau
    liste = '''
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
                		<h2>Nos Agriculteurs</h2>
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
         				<th data-field="photo" data-sortable="true">Photo</th>
         				<th data-field="presentation" data-sortable="true">Presentation</th>
        				<thead>
        				<tbody>
    '''
    for row in tab_agri:
        liste += '<tr>'
        liste += '<td>' + str(row[0]) + '</td>'
        liste += '<td>' + str(row[1]) + '</td>'
        liste += '<td>' + str(row[2]) + '</td>'
        liste += '<td>' + str(row[3]) + '</td>'
        liste += '<td>' + str(row[4]) + '</td>'
        liste += '<td>' + str(row[5]) + '</td>'
        liste += '<td>' + str(row[6]) + '</td>'
        liste += '</tr>'

    liste += '''
   					 </tbody>
    				</table>
	 				</center>
    			 </div>
     			</div>
			</section>
    '''
    return liste


def FindFarmer():
    result = template.head()
    result += template.nav()
    result += template.header()
    result += Farmer()
    result += template.footer()
    return result
