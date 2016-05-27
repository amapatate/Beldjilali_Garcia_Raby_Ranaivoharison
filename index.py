template = Import('/IENAC15/beldjilali_garcia_raby_ranaivoharison/python/template.py')


def index():
    result = template.head()
    result += template.nav()
    result += template.header()
    result += presentation()
    result += template.footer()
    return result


def presentation():
    presentation = '''
<div class="container">
	<div class="present row">

  <article  class="what col-md-12" >
  	 <div class=" col-md-6 ">
        <h3>Qu'est ce qu'une AMAP</h3>
        <iframe width="560" height="360" src="https://www.youtube.com/embed/Pa3hXIRveYI" frameborder="0" allowfullscreen></iframe>    
		  </br>
		  </br>    
        <p>
            Une AMAP, ou association pour le maintien d'une agriculture paysanne, est caractérisé par un partenariat
       		entre des producteurs locaux et des consommateurs. Elle permet de mettre en place une nouvelle forme de
       		consommation ayant pour socle une confiance entre agriculteurs et clients. De plus, en suprimant bon nombre
       		d'intermédiaires elles permettent d'être plus juste pour les agriculteurs.
        </p>
        </br>
		  </br>
        <img titre="qu'est ce qu'une amap" alt="PATATE" src="/IENAC15/beldjilali_garcia_raby_ranaivoharison/images/Schema.jpg" />
        </br>
		  </br>
        <p>
        		L'interaction entre agiculteur et client se fait par l'intermédiaire d'un panier. En effet, un agriculteur
        		va proposer un panier constitué de différents fruits et légumes à ses clients en fonction de ce qu'il compte
        		produir. Pour le client, ce dernier va choisir un panier et payer à l'avance l'agriculeur pour ce panier qu'il
        		recevra une fois que les produits sont près à la consommation.
    		</p>
    		
    </div>
    <div class="site col-md-6 " >
      	<h3>Présentation du site</h3>            
    </div>
  </article>
</div>
</div>
'''
    return presentation
