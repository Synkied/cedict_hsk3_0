-- MySQL dump 10.13  Distrib 5.1.61, for redhat-linux-gnu (x86_64)
--
-- Host: localhost    Database: newindex
-- ------------------------------------------------------
-- Server version	5.1.61

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `words_types`
--

DROP TABLE IF EXISTS `words_types`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `words_types` (
  `id` bigint(22) NOT NULL AUTO_INCREMENT,
  `word` varchar(255) COLLATE utf8_bin NOT NULL,
  `reverse` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `count` int(8) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `word_2` (`word`),
  KEY `reverse` (`reverse`(32)) USING BTREE,
  KEY `count` (`count`) USING BTREE
) ENGINE=MyISAM AUTO_INCREMENT=1738342 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2012-03-20 20:31:44
