def head():
    head = '''
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
    <html xmlns="http://www.w3.org/1999/xhtml">
    <html xml:lang="fr">
<head>
  <title>AMAP'ATATE</title>
  <meta charset="utf-8"/>
  <link rel="icon" type="image/png" href="/IENAC15/beldjilali_garcia_raby_ranaivoharison/images/logo.png" />
    <link rel="stylesheet" type="text/css" href="/IENAC15/beldjilali_garcia_raby_ranaivoharison/css/menu.css">
    <link rel="stylesheet" type="text/css" href="/IENAC15/beldjilali_garcia_raby_ranaivoharison/css/style.css">
    <link rel="stylesheet" type="text/css" href="/IENAC15/beldjilali_garcia_raby_ranaivoharison/css/bootstrap.min.css" />
    <script type="text/javascript" src="/IENAC15/beldjilali_garcia_raby_ranaivoharison/js/jquery-2.2.0.min.js"></script>
    <script type="text/javascript" src="/IENAC15/beldjilali_garcia_raby_ranaivoharison/js/menu.js"></script>
</head>
<body>'''
    return head


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


def navAdmin():
    nav = '''
 <nav class="header container main">
 <div class="row">
  <ul id="menu" class="col-md-12 col-lg-12 ">

        <li><a  href="/IENAC15/beldjilali_garcia_raby_ranaivoharison/index.py/index">accueil</a></li>

        <li><a href="#">Produits</a>
        <ul><li><a href="/IENAC15/beldjilali_garcia_raby_ranaivoharison/python/produit.py/index">Consulter</a></li>
            <li><a href="/IENAC15/beldjilali_garcia_raby_ranaivoharison/python/produit.py/index">Ajouter</a></li>
            <li><a href="/IENAC15/beldjilali_garcia_raby_ranaivoharison/python/produit.py/index">Modifier</a></li>
            <li><a href="/IENAC15/beldjilali_garcia_raby_ranaivoharison/python/produit.py/index">Supprimer</a></li></ul>
        </li>

        <li><a href="#">Panier-Type</a>
        <ul><li><a href="/IENAC15/beldjilali_garcia_raby_ranaivoharison/python/produit.py/index">Consulter</a></li>
            <li><a href="/IENAC15/beldjilali_garcia_raby_ranaivoharison/python/produit.py/index">Ajouter</a></li>
            <li><a href="/IENAC15/beldjilali_garcia_raby_ranaivoharison/python/produit.py/index">Modifier</a></li>
            <li><a href="/IENAC15/beldjilali_garcia_raby_ranaivoharison/python/produit.py/index">Supprimer</a></li></ul>
        </li>

        <li><a href="#">Abriculteurs</a>
        <ul><li><a href="/IENAC15/beldjilali_garcia_raby_ranaivoharison/python/produit.py/index">Consulter</a></li>
            <li><a href="/IENAC15/beldjilali_garcia_raby_ranaivoharison/python/produit.py/index">Ajouter</a></li>
            <li><a href="/IENAC15/beldjilali_garcia_raby_ranaivoharison/python/produit.py/index">Modifier</a></li>
            <li><a href="/IENAC15/beldjilali_garcia_raby_ranaivoharison/python/produit.py/index">Supprimer</a></li></ul>
        </li>

        <li><a href="#">Clients</a>
        <ul><li><a href="/IENAC15/beldjilali_garcia_raby_ranaivoharison/python/produit.py/index">Consulter</a></li>
            <li><a href="/IENAC15/beldjilali_garcia_raby_ranaivoharison/python/produit.py/index">Ajouter</a></li>
            <li><a href="/IENAC15/beldjilali_garcia_raby_ranaivoharison/python/produit.py/index">Modifier</a></li>
            <li><a href="/IENAC15/beldjilali_garcia_raby_ranaivoharison/python/produit.py/index">Supprimer</a></li></ul>
        </li>

        <li><a href="#">plus</a>
                <ul><li><a href="#">forum</a></li>
                    <li><a href="#">liens</a></li>
                    <li><a href="#">nous contacter</a></li>
                    <li><a href="#">team</a></li>
                    <li><a href="#">recherche</a></li></ul>
        </li>
        <li><a href="#">membres</a>
            <ul><li><a href="#">connexion</a></li>
                <li><a href="/IENAC15/beldjilali_garcia_raby_ranaivoharison/python/NewAcount.py/NewAcount">inscription</a></li>
            </ul>
        </li>

</ul>
</div>
</nav>
<br /><br /> <br /><br /><br /><br />


  '''
    return nav

def nav():

    # navigation pour simple visiteur mais client potentiel
    nav = '''
 <nav class="header container main">
 <div class="row">
  <ul id="menu" class="col-md-12 col-lg-12 ">

        <li><a  href="/IENAC15/beldjilali_garcia_raby_ranaivoharison/index.py/index">Accueil</a></li>

        <li><a href="#">Produits</a>
        <ul><li><a href="/IENAC15/beldjilali_garcia_raby_ranaivoharison/python/produit.py/index">Consulter</a></li></ul></li>

        <li><a href="#">Panier-Type</a>
        <ul><li><a href="/IENAC15/beldjilali_garcia_raby_ranaivoharison/python/produit.py/index">Consulter</a></li></ul></li>

        <li><a href="#">Abriculteurs</a>
        <ul><li><a href="/IENAC15/beldjilali_garcia_raby_ranaivoharison/python/produit.py/index">Consulter</a></li></ul></li>



        <li><a href="/IENAC15/beldjilali_garcia_raby_ranaivoharison/python/NewAcount.py/NewAcount">Inscription</a></li>
        <li><a href="#">Connexion</a></li>

        <li><a href="#">plus</a>
                <ul><li><a href="#">forum</a></li>
                    <li><a href="#">liens</a></li>
                    <li><a href="#">nous contacter</a></li>
                    <li><a href="#">recherche</a></li></ul>
        </li>

</ul>
</div>
</nav>
<br /><br /> <br /><br /><br /><br />


  '''
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
