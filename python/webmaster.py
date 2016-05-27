template = Import('/IENAC15/beldjilali_garcia_raby_ranaivoharison/python/template.py')




def index():
    result = template.head()
    result += template.nav()
    result += template.header()
    result += cv()
    result += template.footer()
    return result

def cv():
    cv = '''

    <div class="present row">

  <article  class="what col-md-12" >
  <h2><a href="/IENAC15/beldjilali_garcia_raby_ranaivoharison/data/contrat.pdf">Contrat-type AMAP'ATATE</a> </h2>
  <h2><a href="/IENAC15/beldjilali_garcia_raby_ranaivoharison/data/charte.pdf">Charte AMAP mars 2014</a> </h2>
    <h2><a href="/IENAC15/beldjilali_garcia_raby_ranaivoharison/data/cv_raby.pdf">CV Raby</a> </h2>
    <h2><a href="/IENAC15/beldjilali_garcia_raby_ranaivoharison/data/cv_ryan.pdf">CV Ryan</a> </h2>
    <h2><a href="/IENAC15/beldjilali_garcia_raby_ranaivoharison/data/cv_garcia.pdf">CV Garcia</a>  </h2>
    <h2><a href="/IENAC15/beldjilali_garcia_raby_ranaivoharison/data/cv_beldjilali.pdf">CV BELDJILALI Abdelkader</a> </h2>
      </article>


</div>

<br /><br /><br />


    '''
    return cv


