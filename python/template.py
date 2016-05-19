def head():
    head='''
<html xml:lang="fr">

<head>
  <title>AMAP'ATATE</title>
  <meta charset="utf-8"/>
    <link rel="stylesheet" type="text/css" href="/IENAC15/Beldjilali_Garcia_Raby_Ranaivoharison/css/style.css">
    <link rel="stylesheet" type="text/css" href="/IENAC15/Beldjilali_Garcia_Raby_Ranaivoharison/css/bootstrap-grid.css" />
</head>
<body>'''
    return head
def nav():
    nav='''
  <nav class="header container main ">
      <div id="logo" class="col-md-1"><a href="/IENAC15/Beldjilali_Garcia_Raby_Ranaivoharison/index.py/index"></a></div>
      <ul class="col-md-5">
        <li><a href="./PageClient.html">Fruits</a></li>
        <li><a href="#">Legumes</a></li>
        <li><a href="#">Viandes</a></li>
        <li><a href="#">Poissons</a></li>
      </ul>
      <div class= "login col-md-6">
        <ul>
          <li><a href="/IENAC15/Beldjilali_Garcia_Raby_Ranaivoharison/python/NewAcount.py/NewAcount">Créer un compte</a></li>
          <li><a href="/IENAC15/Beldjilali_Garcia_Raby_Ranaivoharison/python/PageClient/IndexClient.py/IndexClient">Se connecter</a></li>
        </ul>
      </div>
  </nav>'''
    return nav
def navClient():
    nav='''
    <nav class="header container main ">
      <div id="logo" class="col-md-1"><a href="/IENAC15/Beldjilali_Garcia_Raby_Ranaivoharison/python/PageClient/IndexClient.py/IndexClient"></a></div>
      <ul class="col-md-5">
        <li><a href="/IENAC15/Beldjilali_Garcia_Raby_Ranaivoharison/python/PageClient/MySubs.py/MySubs">Mes Abonnements</a></li>
        <li><a href="/IENAC15/Beldjilali_Garcia_Raby_Ranaivoharison/python/PageClient/Messages.py/Messages">Messages</a></li>
        <li><a href="/IENAC15/Beldjilali_Garcia_Raby_Ranaivoharison/python/PageClient/FindFarmer.py/FindFarmer">Trouver un Agriculteur</a></li>
      </ul>
      <div class= "login col-md-6">
        <ul>
          <li><a href="/IENAC15/Beldjilali_Garcia_Raby_Ranaivoharison/python/PageClient/MyAcount.py/MyAcount">"NomClient"</a></li>
          <li><a href="/IENAC15/Beldjilali_Garcia_Raby_Ranaivoharison/index.py/index">Se Déconnecter</a></li>
        </ul>
      </div>
  </nav>'''
    return nav

def header():
    header='''
  <header class="container">
    <section class="hero row">
      <h1>Bienvenue à l'Amap'atate</h1>
      <p></p>
    </section>
  </header>'''
    return header
def headerClient():
    header='''
    <header class="container">
    <section class="hero row">
      <h1>Bonjour "nomClient"</h1>
      <p></p>
    </section>
  </header>'''
    return header
def footer():
    footer='''
  <footer class="clearfix container">
    <div class="info">
      <ul>
        <li class="col-md-6 col-xs-6"> <a href="http://www.enac.fr/" target="_blank">Site de l'ENAC </a></li>
        <li class="col-md-6 col-xs-6"> <a href="#">Les développeurs </a> </li>
      </ul>
      <h3 class="col-md-12 col-xs-12">&copy All right reserved ENAC</h3>
    </div>
  </footer>
</body>
</html>'''
    return footer
