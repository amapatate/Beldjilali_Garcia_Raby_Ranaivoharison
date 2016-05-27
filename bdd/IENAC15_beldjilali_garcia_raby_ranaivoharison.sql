DROP DATABASE IF EXISTS  IENAC15_beldjilali_garcia_raby_ranaivoharison;

CREATE DATABASE IENAC15_beldjilali_garcia_raby_ranaivoharison;
     USE IENAC15_beldjilali_garcia_raby_ranaivoharison;

CREATE TABLE `client` (
  `id` int AUTO_INCREMENT,
  `civilite` varchar(10),
  `nom` varchar(20),
  `prenom` varchar(20),
  `telephone` varchar(30),
  `mdp` varchar(20),
  `email` varchar(30),
  `id_agriculteur` varchar(30),
  `adresse` text,
   PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

CREATE TABLE `agriculteur` (
  `id` int(11) AUTO_INCREMENT,
  `civilite` varchar(10),
  `nom` varchar(20),
  `prenom` varchar(20),
  `telephone` varchar(30),
  `mdp` varchar(20),
  `email` varchar(30),
  `adresse` text,
  `photo` mediumblob,
  `presentation` text,
  `lieu_recup_panier` text,
  `rib_agriculteur` varchar(24),
  `modalite_paiement` TEXT,
   PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------


CREATE TABLE `produit` (
  `id` int AUTO_INCREMENT,
  `nom` varchar(50),
  `type` varchar(12),
  `variete` varchar(256),
  `description` text,
  `prix_kg` DECIMAL(10,2),
  `photo` mediumblob,
  `id_agriculteur` int,
  PRIMARY KEY (id)
) ENGINE=InnoDB CHARSET=utf8;


-- --------------------------------------------------------


CREATE TABLE `panier_type` (
  `id` int(11) AUTO_INCREMENT,
  `id_agriculteur` int(11),
  `date_validite` date,
   `photo` mediumblob,
   `prix_abo_mensuel` DECIMAL(10,2),
  FOREIGN KEY (id_agriculteur) REFERENCES agriculteur(id), 
  PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

CREATE TABLE `detail_panier_type` (
  `id` int(11) AUTO_INCREMENT,
  `qte_produit` DECIMAL(10,2),
  `id_panier_type` int(11),
  `id_produit` int(11),
  FOREIGN KEY (id_produit) REFERENCES produit(id),
  FOREIGN KEY (id_panier_type) REFERENCES panier_type(id),
  PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- --------------------------------------------------------

INSERT INTO produit (nom,type, id_agriculteur) VALUES 
('pomme de terre','legume', 1),('chou','legume', 1),('navet','legume', 1), ('oignon','legume', 2),
('pomme','fruit', 1), ('poire','fruit', 2), ('fraise','fruit', 2),
('riz','feculent', 2), ('blé','feculent', 2), ('haricot sec','feculent', 1);

INSERT INTO client (telephone, nom, prenom,email,mdp) VALUES 
('01231456789','Nerve','Germaine','nerve@free.fr','patate');

INSERT INTO agriculteur (nom, prenom,telephone, email,mdp,presentation) VALUES
('Ate','Patrick','01231450000', 'pat@frite.fr','patate','agriculteur spécialisé dans la Pat Ate');

INSERT INTO agriculteur (nom, prenom,telephone, email,mdp,presentation) VALUES
('admin','admin','0123456789', 'admin','admin','compte administrateur du site');

INSERT INTO panier_type (id_agriculteur, prix_abo_mensuel) VALUES
(1, 0.00),(2, 0.00);


















