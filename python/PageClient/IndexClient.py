template=Import('/IENAC15/beldjilali_garcia_raby_ranaivoharison/python/template.py')

def intro():
    intro='''
<div class="container">
    <section class="present row">
      <h2>Présentation Générale</h2>
      <article  class="what col-md-12" >
      	 <div class=" col-md-6 col-xs-12">
            <a href="#"><h3>Qu'est-ce qu'une AMAP ?</h3></a>
          	<a href="#">
                <img src="/IENAC15/beldjilali_garcia_raby_ranaivoharison/images/patate.jpg" alt="PATATE" titre="qu'est ce qu'une amap"/>
            </a>
         </div>
         <div class="site col-md-6 col-xs-12" >
          		<h3>Présentation du site</h3>
          		<p></p>
        </div>
      </article>
    </section>
</div>'''
    return intro

def IndexClient():
    result= template.head()
    result+= template.navClient()
    result+= template.headerClient()
    result+= intro()
    result+= template.footer()
    return result
