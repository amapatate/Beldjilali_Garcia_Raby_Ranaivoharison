bdd = Import('/IENAC15/beldjilali_garcia_raby_ranaivoharison/python/bddamap.py')
template = Import('/IENAC15/beldjilali_garcia_raby_ranaivoharison/python/template.py')


def index():
    result = template.head()
    result += template.nav()
    result += template.header()
    # result+= club()
    result += listeProduit()
    result += template.footer()
    return result


def listeProduit():
    tab_produit = bdd.selectProduit()
    # affichage du tableau
    liste = '''
	 <section>
    	<div class="container" > 
    		<style>
    	  				table{border-collapse:separate; border-spacing:10px}
    	  				table,td,tr{border:0px; padding:10px}
    	  				table th { padding:10px; border-radius:10px; background-color:1b4837}
    	  				table thead {color:#44B78B}
    	  	</style>    
    	<div class="row">
    	 	<caption>
                		<h2>Nos Produits</h2>
       	</caption>
      </div>   
    	<div class="row col-md-12 ">
    	  	<center>
    		<table class="table " 
    		data-toggle="table" data-search="true" data-pagination="true" data-page-size="3">
         	<thead>
         		<tr>
         			<th data-field="nom" data-sortable="true" >Nom</th>
         			<th data-field="type" data-sortable="true">Type</th>
        				<th data-field="variete" data-sortable="true">Variété</th>
         			<th data-field="description" data-sortable="true">Description</th>
         			<th data-field="prix" data-sortable="true">Prix au kg</th>
         			<th data-field="photo" data-sortable="true">Agriculteur</th>
         			<th data-field="producteur" data-sortable="true">Producteur</th>
         		</tr>
        		</thead>
        		<tbody>
    '''
    for row in tab_produit:
        liste += '<tr>'
        liste += '<td>' + str(row[1]) + '</td>'
        liste += '<td>' + str(row[2]) + '</td>'
        liste += '<td>' + str(row[3]) + '</td>'
        liste += '<td>' + str(row[4]) + '</td>'
        liste += '<td>' + str(row[5]) + '</td>'
        liste += '<td>' + str(row[8]) + '</td>'
        liste += '<td>' + str(row[6]) + ' ' + str(row[7]) + '</td>'
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
