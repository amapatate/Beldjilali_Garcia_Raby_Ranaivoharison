def head():
    head = '''
<html xml:lang="fr">

<head>
  <title>AMAP'ATATE</title>
  <meta charset="utf-8"/>
    <link rel="stylesheet" type="text/css" href="/IENAC15/beldjilali_garcia_raby_ranaivoharison/css/style.css">
    <link rel="stylesheet" type="text/css" href="/IENAC15/beldjilali_garcia_raby_ranaivoharison/css/bootstrap.min.css" />
    <link rel="stylesheet" type="text/css" href="/IENAC15/beldjilali_garcia_raby_ranaivoharison/css/bootstrap-grid.css" />
    <script type="text/javascript" src="js/jquery-2.2.0.min.js"></script>
    <script type="text/javascript" src="js/bootstrap-grid.js"></script>

</head>
<body>'''
    return head


def nav():
    nav = '''
  <nav class="header container main">

      <div id="logo" class="col-md-1"><a href="/IENAC15/beldjilali_garcia_raby_ranaivoharison/index.py/index"></a></div>
      <ul class="col-md-5">
       <li><a href="/IENAC15/beldjilali_garcia_raby_ranaivoharison/index.py/index">Accueil</a></div>
        <li><a href="/IENAC15/beldjilali_garcia_raby_ranaivoharison/python/produit.py/index">Produits</a></li>
        <li><a href="./PageClient.html">Fruits</a></li>
        <li><a href="#">Legumes</a></li>
        <li><a href="#">Viandes</a></li>
        <li><a href="#">Poissons</a></li>
      </ul>
      <div class= "login col-md-6">
        <ul>
          <li><a href="/IENAC15/beldjilali_garcia_raby_ranaivoharison/python/NewAcount.py/NewAcount">Créer un compte</a></li>
          <li><a href="/IENAC15/beldjilali_garcia_raby_ranaivoharison/python/PageClient/IndexClient.py/IndexClient">Se connecter</a></li>
        </ul>
      </div>
  </nav>'''
    return nav


def navClient():
    nav = '''
    <nav class="header container main ">
      <div id="logo" class="col-md-1"><a href="/IENAC15/beldjilali_garcia_raby_ranaivoharison/python/PageClient/IndexClient.py/IndexClient"></a></div>
      <ul class="col-md-5">
        <li><a href="/IENAC15/beldjilali_garcia_raby_ranaivoharison/python/PageClient/MySubs.py/MySubs">Mes Abonnements</a></li>
        <li><a href="/IENAC15/beldjilali_garcia_raby_ranaivoharison/python/PageClient/Messages.py/Messages">Messages</a></li>
        <li><a href="/IENAC15/beldjilali_garcia_raby_ranaivoharison/python/PageClient/FindFarmer.py/FindFarmer">Trouver un Agriculteur</a></li>
      </ul>
      <div class= "login col-md-6">
        <ul>
          <li><a href="/IENAC15/beldjilali_garcia_raby_ranaivoharison/python/PageClient/MyAcount.py/MyAcount">"NomClient"</a></li>
          <li><a href="/IENAC15/beldjilali_garcia_raby_ranaivoharison/index.py/index">Se Déconnecter</a></li>
        </ul>
      </div>
  </nav>'''
    return nav


def header():
    header = '''
  <header class="row">
  <div class="container>
     <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">
        <img   width="100%" src="/IENAC15/beldjilali_garcia_raby_ranaivoharison/images/banniere.jpg" alt="banniere" title="AMAP'ATATE" />
    </div>
 </div>
  </header>'''
    return header



def headerClient():
    header = '''
    <header class="container">
    <section class="hero row">
      <h1>Bonjour "nomClient"</h1>
      <p></p>
    </section>
  </header>'''
    return header


def footer():
    footer = '''
  <footer class="clearfix container">
    <div class="info row">
      <ul>
        <li class="col-md-3" > <a href="http://www.enac.fr/" target="_blank">Site de l'ENAC </a></li>
        <li class="col-md-3" > <a href="#">Les développeurs </a> </li>
      </ul>
    </div>
  </footer>
</body>
</html>'''
    return footer
