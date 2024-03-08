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
-- Table structure for table `app01_comment`
--

DROP TABLE IF EXISTS `app01_comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `app01_comment` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `content` longtext NOT NULL,
  `score` int NOT NULL,
  `likes` int NOT NULL,
  `time` varchar(32) NOT NULL,
  `replyNum` int NOT NULL,
  `author_id` bigint NOT NULL,
  `dish_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `app01_comment_author_id_f2f4019a_fk_app01_user_id` (`author_id`),
  KEY `app01_comment_dish_id_8b709bf5_fk_app01_dish_id` (`dish_id`),
  CONSTRAINT `app01_comment_author_id_f2f4019a_fk_app01_user_id` FOREIGN KEY (`author_id`) REFERENCES `app01_user` (`id`),
  CONSTRAINT `app01_comment_dish_id_8b709bf5_fk_app01_dish_id` FOREIGN KEY (`dish_id`) REFERENCES `app01_dish` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app01_comment`
--

LOCK TABLES `app01_comment` WRITE;
/*!40000 ALTER TABLE `app01_comment` DISABLE KEYS */;
INSERT INTO `app01_comment` VALUES (1,'非常的新鲜',5,5,'2023-07-29 23:59:18',1,1,1),(2,'鉴定为：没吃过的东西',4,0,'2023-07-30 00:22:09',0,1,253),(3,'从哪里找来的这些图片？',3,0,'2023-07-30 00:22:45',0,1,168),(4,'好吃就多吃点',5,1,'2023-07-30 00:24:00',1,1,568),(5,'有没有黑水煮鸭蛋？',5,0,'2023-07-30 00:24:43',0,1,575),(6,'食堂豆腐脑简直绝了！细腻滑嫩，入口即化。香甜浓郁，让人回味无穷。口感犹如丝滑云朵，每一口都是满满的幸',5,2,'2023-07-30 00:28:41',1,1,563),(7,'很好吃',5,0,'2023-07-30 00:29:46',0,1,568),(8,'',1,0,'2023-07-30 00:30:03',0,1,402),(9,'好吃不贵',5,1,'2023-07-30 00:30:35',0,1,3),(10,'挺好的',1,0,'2023-07-30 00:31:20',0,1,564),(11,'总之还不错，可惜经常卖光。想吃的同学一定要趁早去',4,0,'2023-07-30 12:27:48',0,1,506),(12,'1',4,2,'2023-07-30 14:02:12',0,3,511),(13,'',5,0,'2023-07-30 14:51:57',0,1,589),(14,'真的是小时候的味道！',5,0,'2023-07-30 15:29:25',0,1,8),(15,'好吃不贵',4,0,'2023-07-30 15:30:20',0,1,3),(16,'',4,0,'2023-07-30 17:33:15',0,4,1),(17,'',5,0,'2023-07-30 17:38:26',0,4,168),(18,'给孩子买了一大箱，孩子很喜欢吃',5,3,'2023-07-30 17:40:28',0,4,157),(19,'',4,0,'2023-07-30 17:49:30',0,3,8),(20,'口感尚可，值得一试，但遗憾红豆与奶香不够浓郁，个人感觉略显单调。',4,0,'2023-07-30 18:50:27',0,1,193),(21,'非常好吃耶，很辣很喜欢',5,0,'2023-07-30 19:11:38',0,5,78),(22,'',4,0,'2023-07-30 23:20:17',0,1,78);
/*!40000 ALTER TABLE `app01_comment` ENABLE KEYS */;
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
