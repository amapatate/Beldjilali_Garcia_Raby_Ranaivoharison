-- phpMyAdmin SQL Dump
-- version 4.0.10deb1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: May 04, 2016 at 03:16 PM
-- Server version: 5.5.41-0ubuntu0.14.04.1
-- PHP Version: 5.5.9-1ubuntu4.5

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `bdd_amapatate`
--

-- --------------------------------------------------------

--
-- Table structure for table `Compose`
--

CREATE TABLE IF NOT EXISTS `Compose` (
  `mail` varchar(30) NOT NULL,
  `id_produit` int(11) NOT NULL,
  `id_panier` int(11) NOT NULL,
  `qté` decimal(10,0) NOT NULL,
  PRIMARY KEY (`mail`,`id_produit`,`id_panier`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `Compte`
--

CREATE TABLE IF NOT EXISTS `Compte` (
  `mail` varchar(30) NOT NULL,
  `mdp` varchar(20) NOT NULL,
  `nom` varchar(20) NOT NULL,
  `prénom` varchar(20) NOT NULL,
  `adresse` varchar(100) NOT NULL,
  `photo` text NOT NULL,
  PRIMARY KEY (`mail`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `Compte_Agriculteur`
--

CREATE TABLE IF NOT EXISTS `Compte_Agriculteur` (
  `mail` varchar(30) NOT NULL,
  `présentation` text NOT NULL,
  `lieu_récup_panier` varchar(100) NOT NULL,
  `rib_agriculteur` varchar(24) NOT NULL,
  `type_paiement` varchar(20) NOT NULL,
  PRIMARY KEY (`mail`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `Compte_Client`
--

CREATE TABLE IF NOT EXISTS `Compte_Client` (
  `mail` varchar(30) NOT NULL,
  PRIMARY KEY (`mail`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `Panier`
--

CREATE TABLE IF NOT EXISTS `Panier` (
  `id_panier` int(11) NOT NULL AUTO_INCREMENT,
  `date_validité` date NOT NULL,
  PRIMARY KEY (`id_panier`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `Panier_Client`
--

CREATE TABLE IF NOT EXISTS `Panier_Client` (
  `id_panier` int(11) NOT NULL,
  `mail` varchar(30) NOT NULL,
  `prix` decimal(10,0) NOT NULL,
  PRIMARY KEY (`id_panier`),
  KEY `mail` (`mail`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `Produit`
--

CREATE TABLE IF NOT EXISTS `Produit` (
  `id_produit` int(11) NOT NULL AUTO_INCREMENT,
  `type` varchar(20) NOT NULL,
  `nom` varchar(20) NOT NULL,
  `mail` varchar(30) NOT NULL,
  `prix_kg` decimal(11,0) NOT NULL,
  PRIMARY KEY (`id_produit`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `Produit_Agriculteur`
--

CREATE TABLE IF NOT EXISTS `Produit_Agriculteur` (
  `mail` varchar(30) NOT NULL,
  `id_produit` int(11) NOT NULL,
  `qté_dispo` decimal(10,0) NOT NULL,
  KEY `mail` (`id_produit`),
  KEY `mail_2` (`mail`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
