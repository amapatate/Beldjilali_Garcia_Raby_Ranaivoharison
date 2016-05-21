template= Import('/IENAC15/beldjilali_garcia_raby_ranaivoharison/python/template.py')



def index():
    result=template.head()
    result+= template.header()
    result+= template.navAdmin()
    result+= presentation()
    result+= template.footer()
    return result




def presentation():
    presentation='''
<div class="container">

<div class="present row">
    <div class="class="col-lg-offset-8 col-lg-10">
        <h2><a href="#">
        <img  id="logo" width="20%" src="/IENAC15/beldjilali_garcia_raby_ranaivoharison/images/logo.png" alt="logo" title="AMAP'ATATE" />
        </a>
        </h2>
    </div>
</div>

<div class="present row">
  <h2 id="amap">Bienvenue sur le site de l'Amap'atate</h2>
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
</div>

<br /><br /><br />

<section>
Une&nbsp;<strong>association
pour le maintien d'une&nbsp;<a href="http://fr.wikipedia.org/wiki/Agriculture_paysanne" target="_blank">agriculture
paysanne</a></strong>, ou&nbsp;<strong>AMAP*</strong>, est, en
France, un partenariat de proximité&nbsp;entre un groupe de
consommateurs et une exploitation locale (généralement une ferme),
débouchant sur un partage de récolte régulier (le plus souvent
hebdomadaire) composée des produits de la ferme. L'AMAP est un
contrat solidaire, basé&nbsp;sur un engagement financier des
consommateurs, qui paient&nbsp;à&nbsp;l’avance la totalité&nbsp;de
leur consommation sur une période définie. Ce système fonctionne
donc sur le principe de la confiance et de la responsabilité&nbsp;du
consommateur; il représente une forme de&nbsp;<a href="http://fr.wikipedia.org/wiki/Circuit_court">circuit
court</a>&nbsp;de distribution.<br/>
<br/>
En 2014, la Charte des
AMAP est ré-actualisée, suite&nbsp;à&nbsp;un chantier et une
réflexion participative inter-régionale coordonnée par le
Mouvement Inter-Régional des AMAP (MIRAMAP).<br/>
<br/>
<br/>
<br/>
<strong>Une&nbsp;</strong><strong><em>Amap</em></strong><strong>&nbsp;repose
sur une règle de 3x3 engagements :</strong><br/>
<br/>
Trois
engagements généraux :</p>
<ul>
	<li/>
<p style="margin-bottom: 0cm">vente directe</p>
	<li/>
<p style="margin-bottom: 0cm">proximité</p>
	<li/>
<p>convivialité</p>
</ul>
<p>Trois engagements des consomm’Acteurs :</p>
<ul>
	<li/>
<p style="margin-bottom: 0cm">préfinancement de la production</p>
	<li/>
<p style="margin-bottom: 0cm">solidarité dans les aléas
	naturels</p>
	<li/>
<p>implication dans la gestion du groupe</p>
</ul>
<p>Trois engagements du paysan :</p>
<ul>
	<li/>
<p style="margin-bottom: 0cm">production de qualité et
	diversifiée (et bio, dans notre cas)</p>
	<li/>
<p style="margin-bottom: 0cm">pédagogie</p>
	<li/>
<p>transparence technique et économique.</p>
</ul>
<p><strong>Si on résume, les engagements en&nbsp;</strong><strong><em>Amap</em></strong><strong>&nbsp;:</strong><br/>
<br/>
<strong>pour
le consomm’Acteur :</strong></p>
<ul>
	<li/>
<p style="margin-bottom: 0cm">payer d’avance 12 mois de
	légumes (et fruits) sous forme de chèques encaissés
	mensuellement,</p>
	<li/>
<p style="margin-bottom: 0cm">venir chercher son panier chaque
	semaine aux horaires indiqués,</p>
	<li/>
<p style="margin-bottom: 0cm">gérer ses absences,</p>
	<li/>
<p style="margin-bottom: 0cm">participer aux distributions, et
	participer à au moins 1 sortie à la ferme,</p>
	<li/>
<p>accepter de n’avoir que des produits de saison et locaux.</p>
</ul>
<p><strong>pour le paysan :</strong></p>
<ul>
	<li/>
<p style="margin-bottom: 0cm">proposer un panier varié toute
	l’année,</p>
	<li/>
<p style="margin-bottom: 0cm">être présent aux
	distributions,</p>
	<li/>
<p style="margin-bottom: 0cm">accueillir les comm’Acteurs
	qui souhaitent visiter la ferme, au moins 2 fois par an,</p>
	<li/>
<p style="margin-bottom: 0cm">donner régulièrement des
	nouvelles de la ferme à l’ensemble des consomm’Acteurs,</p>
	<li/>
<p>accepter de répondre aux questions des consomm’Acteurs,
	sur l’organisation et les modalités de fixation du prix.</p>
</ul>
<p><strong><em>L’Amap</em></strong>&nbsp;ne représente pas
l’association des consomm’Acteurs, mais bien le partenariat, le
lien, entre un paysan et un groupe de cosomm’Acteurs, — qu’il
soit déclaré ou non en association à la préfecture.<br/>
Ce lien
est matérialisé par le&nbsp;<em>contrat d’engagement Amap</em>.</p>
</section>

'''
    return presentation
