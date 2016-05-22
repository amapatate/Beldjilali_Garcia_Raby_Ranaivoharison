bdd = Import('/IENAC15/beldjilali_garcia_raby_ranaivoharison/python/bddamap.py')
template = Import('/IENAC15/beldjilali_garcia_raby_ranaivoharison/python/template.py')


def index():
    result = template.head()
    result += template.header()
    result += template.nav()
    #result+= club()
    result += listeProduit()
    result += template.footer()
    return result

def listeProduit():
    tab_produit = bdd.selectProduit()
    # affichage du tableau
    liste = '''
        <section id="prod">
    <div class="container">

        <div class="row">
            <caption>
                <h3>Nos produits</h3>
            </caption>
        </div>

    <div class="row">
    <table class="table table-responsive table-bordered table-striped table-condensed"
    data-toggle="table" data-search="true" data-pagination="true" data-page-size="3">
         <thead>
         <th data-field="id" data-sortable="true">Id</th>
         <th data-field="nom" data-sortable="true">Nom</th>
         <th data-field="type" data-sortable="true">Type</th>
         <th data-field="variete" data-sortable="true">Variété</th>
         <th data-field="description" data-sortable="true">Description</th>
         <th data-field="prix" data-sortable="true">Prix au kg</th>
         <th data-field="photo" data-sortable="true">Photo</th>
        <thead>
        <tbody>
    '''
    for row in tab_produit:
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

     </div>
     </div>
    </section>
    '''
    return liste

def listeProduit1():
    tab_produit = bdd.selectProduit()
    # affichage du tableau
    liste = '''
    <div class="container">

        <div class="row">
            <caption>
                <h3>Nos produits</h3>
            </caption>
        </div>

    <div class="row">
    <table class="table table-responsive table-bordered table-striped table-condensed" data-toggle="table" data-search="true" data-pagination="true" data-page-size="3">
         <thead>
         <th data-field="col0" data-sortable="true">Id</th>
         <th data-field="col1" data-sortable="true">Nom</th>
         <th data-field="col2" data-sortable="true">Type</th>
         <th data-field="col3" data-sortable="true">Variété</th>
         <th data-field="col4" data-sortable="true">Description</th>
         <th data-field="col5" data-sortable="true">Prix au kg</th>
         <th data-field="col6" data-sortable="true">Photo</th>
        <thead>
        <tbody>
    '''
    for row in tab_produit:
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

     </div>
     </div>

    '''
    return liste

def club():
    club='''
           <section id="clubs">
               <h2>Liste des clubs sportifs à l'ENAC</h2>

                   <table class="table" data-toggle="table" data-search="true" data-pagination="true" data-page-size="3">
                       <thead>
                             <tr>
                             	 <th data-field="colX" data-sortable="true">Club</th>
                             	 <th data-field="colX" data-sortable="true">Responsable</th>
                             </tr>

                        </thead>
                        <tbody>
                              <tr>
                             		<td>Foot</td>
                             		<td>M. Potogoal - IENAC 12S</td>
                               </tr>
                               <tr>
                             		<td>Tennis</td>
                             		<td>Melle Baballe - IESSA 13</td>
                             	</tr>
                             		 <td>Rugby</td>
                             		 <td>M. Ovale - TSA 13B</td>
                             	</tr>
                             	<tr>
                             		<td>Ski</td>
                             		<td>Melle Piquet - EPL 15</td>
                             	</tr>

                         </tbody>

                    </table>
             </section>
             '''
    return club