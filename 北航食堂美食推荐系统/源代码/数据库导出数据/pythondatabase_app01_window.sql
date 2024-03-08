-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: pythondatabase
-- ------------------------------------------------------
-- Server version	8.0.34

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `app01_window`
--

DROP TABLE IF EXISTS `app01_window`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `app01_window` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL,
  `canteen_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `app01_window_canteen_id_c87d7f80_fk_app01_canteen_id` (`canteen_id`),
  CONSTRAINT `app01_window_canteen_id_c87d7f80_fk_app01_canteen_id` FOREIGN KEY (`canteen_id`) REFERENCES `app01_canteen` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app01_window`
--

LOCK TABLES `app01_window` WRITE;
/*!40000 ALTER TABLE `app01_window` DISABLE KEYS */;
INSERT INTO `app01_window` VALUES (1,'铁板风味',1),(2,'基本伙',1),(3,'羊汤煮馍',1),(4,'鱼粉',1),(5,'鸡排饭',1),(6,'冒菜',1),(7,'饮料',1),(8,'一锅鲜',2),(9,'麻辣香锅',2),(10,'小小饮吧',2),(11,'中式饭团',2),(12,'麻辣烫',2),(13,'营养快餐',2),(14,'海南鸡饭',2),(15,'广式套餐',2),(16,'小小饮吧（北）',2),(17,'一品粥饼',2),(18,'早餐',3),(19,'渔康渔粉',3),(20,'轻食套餐',3),(21,'精品菜1',3),(22,'精品菜2',3),(23,'基本伙',3),(24,'精品菜3',3),(25,'美食航行',3),(26,'滋补汤品',3),(27,'套餐熟食',3),(28,'面条米线水饺',3),(29,'套餐',4),(30,'面条米线',4),(31,'早餐',4),(32,'基本伙',4),(33,'小份菜',4),(34,'风味小炒',4),(36,'测试窗口',6);
/*!40000 ALTER TABLE `app01_window` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-07-31 11:23:15
