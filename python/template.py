def head():
    head = '''
<html xml:lang="fr">

<head>
  <title>AMAP'ATATE</title>
  <meta charset="utf-8"/>
    <link rel="stylesheet" type="text/css" href="/IENAC15/beldjilali_garcia_raby_ranaivoharison/css/style.css">
    <link rel="stylesheet" type="text/css" href="/IENAC15/beldjilali_garcia_raby_ranaivoharison/css/bootstrap-grid.css" />
</head>
<body>'''
    return head


def nav():
    if not ("prenom" in Session()):
        # On n'est pas connecte
        nav = '''
  <nav class="header container main ">
      <div class="col-md-1"><a href="/IENAC15/beldjilali_garcia_raby_ranaivoharison/index.py/index"><img titre="logo" alt="logo" style="width:80px;height:80px;" src="/IENAC15/beldjilali_garcia_raby_ranaivoharison/images/logo.png" /></a></div>
      <ul class="col-md-5">
        <li><a href="/IENAC15/beldjilali_garcia_raby_ranaivoharison/python/produit.py/index">Nos Produits</a></li>
      </ul>
      <div class= "login col-md-6">
        <ul>
          <li><a href="/IENAC15/beldjilali_garcia_raby_ranaivoharison/python/newAccount.py/newAccount?mode=1">Créer un compte</a></li>
          <li><a href="/IENAC15/beldjilali_garcia_raby_ranaivoharison/python/connexion.py/connexion?mode=1">Se connecter</a></li>
        </ul>
      </div>
  </nav>'''
        return nav
    elif Session()["type"] == 'client':
        nav = '''
    <nav class="header container main ">
      <div class="col-md-1"><a href="/IENAC15/beldjilali_garcia_raby_ranaivoharison/python/PageClient/IndexClient.py/IndexClient"><img titre="logo" alt="logo" style="width:80px;height:80px;" src="/IENAC15/beldjilali_garcia_raby_ranaivoharison/images/logo.png" /></a></div>
      <ul class="col-md-7">
      	<li><a href="/IENAC15/beldjilali_garcia_raby_ranaivoharison/python/produit.py/index">Nos Produits</a></li>
        <li><a href="/IENAC15/beldjilali_garcia_raby_ranaivoharison/python/PageClient/MySubs.py/MySubs">Mes Abonnements</a></li>
        <li><a href="/IENAC15/beldjilali_garcia_raby_ranaivoharison/python/PageClient/Messages.py/Messages">Messages</a></li>
        <li><a href="/IENAC15/beldjilali_garcia_raby_ranaivoharison/python/PageClient/FindFarmer.py/FindFarmer">Trouver un Agriculteur</a></li>
      </ul>
      <div class= "login col-md-4">
        <ul>
          <li><a href="/IENAC15/beldjilali_garcia_raby_ranaivoharison/python/PageClient/MyAcount.py/MyAcount">''' + \
              Session()["prenom"] + '''</a></li>
          <li><a href="/IENAC15/beldjilali_garcia_raby_ranaivoharison/python/prive.py/deconnect">Se Déconnecter</a></li>
        </ul>
      </div>
  </nav>'''
        return nav
    else:
        nav = '''
    <nav class="header container main ">
      <div class="col-md-1"><a href="/IENAC15/beldjilali_garcia_raby_ranaivoharison/python/PageAgriculteur/IndexAgri.py/index"><img titre="logo" alt="logo" style="width:80px;height:80px;" src="/IENAC15/beldjilali_garcia_raby_ranaivoharison/images/logo.png" /></a></div>
      <ul class="col-md-7">
        <li><a href="/IENAC15/beldjilali_garcia_raby_ranaivoharison/python/PageAgriculteur/NewProduct.py/NewProduct">Ajouter Un Nouveau Produit</a></li>
        <li><a href="/IENAC15/beldjilali_garcia_raby_ranaivoharison/python/PageAgriculteur/CreatPanier.py/CreatPanier">Mon Panier</a></li>
        <li><a href="/IENAC15/beldjilali_garcia_raby_ranaivoharison/python/PageAgriculteur/MyClient.py/MyClient">Mes Clients</a></li>
      </ul>
      <div class= "login col-md-4">
        <ul>
          <li><a href="/IENAC15/beldjilali_garcia_raby_ranaivoharison/python/PageAgriculteur/MyAcountAgri.py/MyAcountAgri">''' + \
              Session()["prenom"] + '''</a></li>
          <li><a href="/IENAC15/beldjilali_garcia_raby_ranaivoharison/python/prive.py/deconnect">Se Déconnecter</a></li>
        </ul>
      </div>
  </nav>'''
        return nav


def header():
    if not ("prenom" in Session()):
        header = '''
  <header class="col-md-12 col-xs-12">
    <section class="row">
      <img titre="logo" alt="logo" style="width:100% ; height:400px;" src="/IENAC15/beldjilali_garcia_raby_ranaivoharison/images/baniere.png" />
    </section>
  </header>'''
        return header
    else:
        # On part du fait que si Session n'est pas vide, quelqu'un est connecte
        header = '''
    <header class="col-md-12 col-xs-12">
    <section class="row entete">
    	<img titre="logo" alt="logo" style="width:100%;height:400px;" src="/IENAC15/beldjilali_garcia_raby_ranaivoharison/images/baniere.png" />
    </section>
  </header>'''
        return header


def footer():
    footer = '''
  <footer class="clearfix container col-md-12">
    <div class="info">
      <ul>
        <li class="col-md-6 col-xs-6"> <a href="http://chefpatate.fr/" target="_blank">Les recettes du Chef Patate </a></li>
        <li class="col-md-6 col-xs-6"> <a href="/IENAC15/beldjilali_garcia_raby_ranaivoharison/python/webmaster.py/index">Webmasters </a> </li>
      </ul>
      <h3 class="col-md-12 col-xs-12">&copy All potatoes reserved Amap'atate</h3>
    </div>
  </footer>
</body>
</html>'''
    return footer
