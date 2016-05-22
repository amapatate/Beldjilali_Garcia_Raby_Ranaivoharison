$(document).ready(function){
	$("form#auth").on("submit",function(event){
		// l'evt se déclenche lors de la soumission du formulaire
		event.preventDefault();//arrete l'envoi standard du formulaire

$.ajax({//requete ajax

	url:'/IENAC15/beldjilali_garcia_raby_ranaivoharison/python/login.py',
	type:'POST',
	data:$(this).serialize(),
	dataType:'html',
	success:function(resultat){ // en cas de succes
// erreur d'authentification, affichage du message renvoyé par login.py ds la div id=msg

	if(resultat==0)
		{$('#msg').html("erreur d'authentification");}
	else
		{location.href="/IENAC15/beldjilali_garcia_raby_ranaivoharison/python/prive.py/index";}
	},
	error:function(donnee,statut,erreur){alert('erreur');},
	});//fin du $.ajax
      });//fin du $(p.login button").click(function)
   });// fin du $-document).ready(function)define('nom_bd','bd_tsa')
