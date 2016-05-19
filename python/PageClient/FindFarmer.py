template=Import('../template.py')

def Farmer():
    FindFarmer='''
    <div class="col-md-12">
        <p> Sortir la liste des agriculteurs avec une possiblité de recherche et de filtres</p>
    </div>'''
    return FindFarmer

def FindFarmer():
    result= template.head()
    result+= template.navClient()
    result+= template.headerClient()
    result+= Farmer()
    result+= template.footer()
    return result
