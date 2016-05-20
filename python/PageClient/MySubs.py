template=Import('/IENAC15/beldjilali_garcia_raby_ranaivoharison/python/template.py')

def Abo():
    Abo='''
    <div class="col-md-12">
        <p> Obtenir les différents abonnements du client en question</p>
    </div>'''
    return Abo

def MySubs():
    result= template.head()
    result+= template.navClient()
    result+= template.headerClient()
    result+= Abo()
    result+= template.footer()

    return result
