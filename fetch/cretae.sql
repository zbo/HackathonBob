# ************************************************************
# Sequel Pro SQL dump
# Version 4541
#
# http://www.sequelpro.com/
# https://github.com/sequelpro/sequelpro
#
# Host: 10.197.32.135 (MySQL 5.7.20-0ubuntu0.16.04.1)
# Database: hackathon
# Generation Time: 2017-12-20 10:24:43 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Dump of table DefinedExpectation
# ------------------------------------------------------------

DROP TABLE IF EXISTS `DefinedExpectation`;

CREATE TABLE `DefinedExpectation` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `item_name` varchar(11) NOT NULL DEFAULT '',
  `expection` varchar(11) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table DefinedMachineQuota
# ------------------------------------------------------------

DROP TABLE IF EXISTS `DefinedMachineQuota`;

CREATE TABLE `DefinedMachineQuota` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `user_volume` int(11) NOT NULL,
  `data_volume` int(11) NOT NULL,
  `suggested_cpu` varchar(255) NOT NULL DEFAULT '',
  `suggested_memory` varchar(255) NOT NULL DEFAULT '',
  `suggested_cache` varchar(255) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table FetchResult
# ------------------------------------------------------------

DROP TABLE IF EXISTS `FetchResult`;

CREATE TABLE `FetchResult` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `task_id` int(11) NOT NULL,
  `ui_status` int(11) NOT NULL,
  `item_name` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table SetResult
# ------------------------------------------------------------

DROP TABLE IF EXISTS `SetResult`;

CREATE TABLE `SetResult` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `task_id` int(11) NOT NULL,
  `ui_status` varchar(11) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table Task
# ------------------------------------------------------------

DROP TABLE IF EXISTS `Task`;

CREATE TABLE `Task` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `type` char(1) DEFAULT NULL,
  `content` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;




/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
