template=Import('/IENAC15/beldjilali_garcia_raby_ranaivoharison/python/template.py')

def Info():
    Info='''
    <div class="col-md-12">
        <p> Obtenir les informations du client et lui donner la possibilité de les modifier</p>
    </div>'''
    return Info

def MyAcount():
    result= template.head()
    result+= template.navClient()
    result+= template.headerClient()
    result+= Info()
    result+= template.footer()
    return result
