bdd = Import('/IENAC15/beldjilali_garcia_raby_ranaivoharison/python/bddamap.py')
template = Import('/IENAC15/beldjilali_garcia_raby_ranaivoharison/python/template.py')




def index():
    result= template.head()
    result+= template.header()
    result+= template.nav()
    result+= listeProduit()
    result+= template.footer()
    return result


def listeProduit():
    tab_produit = bdd.selectProduit()
    # affichage du tableau
    liste='''
    <section class="row">

        <div class="container">
    <caption>
        <h3>Nos produits</h3>
    </caption>
    <section class="table-responsive">
        <table class="table table-bordered table-striped table-condensed">
         <thead>
         <th>Id</th>
         <th>Nom</th>
         <th>Type</th>
         <th>Variété</th>
         <th>Description</th>
         <th>Prix au kg</th>
         <th>Photo</th>
        <thead>
        <tbody>
    '''
    for row in tab_produit:
        liste+='<tr>'
        liste+='<td>'+str(row[0])+'</td>'
        liste+='<td>'+str(row[1])+'</td>'
        liste+='<td>'+str(row[2])+'</td>'
        liste+='<td>'+str(row[3])+'</td>'
        liste+='<td>'+str(row[4])+'</td>'
        liste+='<td>'+str(row[5])+'</td>'
        liste+='<td>'+str(row[6])+'</td>'
        liste+='</tr>'

    liste+='''
    </tbody>
    </table>
    </section>
    </section>
     </div>



    '''
    return liste

