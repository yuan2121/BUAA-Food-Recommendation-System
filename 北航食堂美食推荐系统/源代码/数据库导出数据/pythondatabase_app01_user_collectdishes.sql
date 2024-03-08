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
-- Table structure for table `app01_user_collectdishes`
--

DROP TABLE IF EXISTS `app01_user_collectdishes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `app01_user_collectdishes` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` bigint NOT NULL,
  `dish_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app01_user_collectDishes_user_id_dish_id_0bff9411_uniq` (`user_id`,`dish_id`),
  KEY `app01_user_collectDishes_dish_id_89ef08d5_fk_app01_dish_id` (`dish_id`),
  CONSTRAINT `app01_user_collectDishes_dish_id_89ef08d5_fk_app01_dish_id` FOREIGN KEY (`dish_id`) REFERENCES `app01_dish` (`id`),
  CONSTRAINT `app01_user_collectDishes_user_id_52ca797f_fk_app01_user_id` FOREIGN KEY (`user_id`) REFERENCES `app01_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app01_user_collectdishes`
--

LOCK TABLES `app01_user_collectdishes` WRITE;
/*!40000 ALTER TABLE `app01_user_collectdishes` DISABLE KEYS */;
INSERT INTO `app01_user_collectdishes` VALUES (16,1,1),(43,1,157),(42,1,164),(4,1,168),(39,1,193),(41,1,253),(7,1,506),(40,1,511),(6,1,563),(5,1,568),(12,3,414),(44,3,584),(37,4,1);
/*!40000 ALTER TABLE `app01_user_collectdishes` ENABLE KEYS */;
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
