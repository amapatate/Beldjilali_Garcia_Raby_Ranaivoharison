drop database  if exists  bdd_amapatate_v2;

  CREATE DATABASE bdd_amapatate_v2;
     USE bdd_amapatate_v2;

	CREATE TABLE compte (
	tel varchar(15),
	nom VarChar(256) , 
	prenom VarChar(256) ,
	email varchar(256) ,
	mdp varchar(256) ,
	adresse text ,
	photo mediumblob ,
	PRIMARY KEY (tel)
    ) ENGINE=InnoDB CHARSET=utf8;


CREATE TABLE `compte_agriculteur` (
  `tel_agriculteur` varchar(15) ,
  `presentation` text ,
  `lieu_recup_panier` text ,
  `rib` varchar(256) ,
  `type_paiement` varchar(30) ,
  PRIMARY KEY (tel_agriculteur),
  FOREIGN KEY (tel_agriculteur) REFERENCES compte (tel) on update cascade on delete cascade
) ENGINE=InnoDB CHARSET=utf8;


CREATE TABLE `compte_client` (
  `tel_client` varchar(15) ,
   PRIMARY KEY (tel_client),
  FOREIGN KEY (tel_client) REFERENCES compte (tel) on update cascade on delete cascade
) ENGINE=InnoDB CHARSET=utf8;

CREATE TABLE panier (
       id_panier int AUTO_INCREMENT,
       tel_agriculteur varchar(15) ,
	date_validite date,
	PRIMARY KEY(id_panier),
  FOREIGN KEY (tel_agriculteur) REFERENCES compte_agriculteur(tel_agriculteur)
) ENGINE=InnoDB CHARSET=utf8;

CREATE TABLE panier_client (
   id_panier_client int,
   tel_client varchar(15),
   prix float,
   masse_panier_kg float,
   PRIMARY KEY (id_panier_client),
  FOREIGN KEY (id_panier_client) REFERENCES panier (id_panier),
  FOREIGN KEY (tel_client) REFERENCES compte_client  (tel_client) 
) ENGINE=InnoDB CHARSET=utf8;

CREATE TABLE produit (
  `id_produit` int AUTO_INCREMENT,
  `nom` varchar(256),
  `description` text,
  `variete` varchar(256),
  `prix_kg` float,
  `photo` mediumblob,
  PRIMARY KEY (id_produit)
) ENGINE=InnoDB CHARSET=utf8;

CREATE TABLE produit_agriculteur (
   id_produit_agriculteur int,
   tel_agriculteur varchar(15),
   id_produit int,
   qte_dispo float,
   PRIMARY KEY (id_produit_agriculteur),
  FOREIGN KEY (id_produit) REFERENCES produit(id_produit),
  FOREIGN KEY (tel_agriculteur) REFERENCES compte_agriculteur(tel_agriculteur)
) ENGINE=InnoDB CHARSET=utf8;

CREATE TABLE compose (
   id_compose int,
   id_panier int,
   id_produit_agriculteur int,
   qte_panier float,
   PRIMARY KEY (id_compose),
  FOREIGN KEY (id_produit_agriculteur) REFERENCES produit_agriculteur (id_produit_agriculteur),
  FOREIGN KEY (id_panier) REFERENCES panier(id_panier)
) ENGINE=InnoDB CHARSET=utf8;


INSERT INTO produit (nom) VALUES 
('pomme de terre'),('chou'),('navet'), ('oignon');

INSERT INTO compte (tel, nom, prenom,email,mdp) VALUES 
('01231456789','Nerve','Germaine','nerve@free.fr','patate');

INSERT INTO compte_client(tel_client) VALUES
('01231456789');

INSERT INTO compte (tel,nom, prenom,email,mdp) VALUES 
('01231450000','Ate','Patrick','ate@free.fr','patate');
INSERT INTO compte_agriculteur (tel_agriculteur,presentation) VALUES
('01231450000','agriculteur spécialisé dans la Pat Ate');

