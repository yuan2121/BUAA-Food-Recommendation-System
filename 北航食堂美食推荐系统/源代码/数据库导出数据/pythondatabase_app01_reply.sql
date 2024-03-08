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
-- Table structure for table `app01_reply`
--

DROP TABLE IF EXISTS `app01_reply`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `app01_reply` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `content` longtext NOT NULL,
  `likes` int NOT NULL,
  `time` varchar(32) NOT NULL,
  `author_id` bigint NOT NULL,
  `comment_id` bigint NOT NULL,
  `receiver_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `app01_reply_author_id_cf06cda6_fk_app01_user_id` (`author_id`),
  KEY `app01_reply_comment_id_5b0cae8d_fk_app01_comment_id` (`comment_id`),
  KEY `app01_reply_receiver_id_1bb71ee3_fk_app01_user_id` (`receiver_id`),
  CONSTRAINT `app01_reply_author_id_cf06cda6_fk_app01_user_id` FOREIGN KEY (`author_id`) REFERENCES `app01_user` (`id`),
  CONSTRAINT `app01_reply_comment_id_5b0cae8d_fk_app01_comment_id` FOREIGN KEY (`comment_id`) REFERENCES `app01_comment` (`id`),
  CONSTRAINT `app01_reply_receiver_id_1bb71ee3_fk_app01_user_id` FOREIGN KEY (`receiver_id`) REFERENCES `app01_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app01_reply`
--

LOCK TABLES `app01_reply` WRITE;
/*!40000 ALTER TABLE `app01_reply` DISABLE KEYS */;
INSERT INTO `app01_reply` VALUES (1,'非常的美味',3,'2023-07-29 23:59:24',1,1,1),(2,'回复测试',0,'2023-07-30 12:23:50',2,4,1),(3,'同感',1,'2023-07-30 23:25:21',1,6,1);
/*!40000 ALTER TABLE `app01_reply` ENABLE KEYS */;
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
