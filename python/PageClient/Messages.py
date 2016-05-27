template = Import('/IENAC15/beldjilali_garcia_raby_ranaivoharison/python/template.py')


def Mes():
    Mes = '''
    <div class="col-md-12">
        <p> Créer un protocole d'envoie automatique d'Email</p>
    </div>'''
    return Mes


def Messages():
    result = template.head()
    result += template.nav()
    result += template.header()
    result += Mes()
    result += template.footer()

    return result
