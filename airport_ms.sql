-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: localhost    Database: airport_ms
-- ------------------------------------------------------
-- Server version	8.0.28

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `admin_support`
--

DROP TABLE IF EXISTS `admin_support`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admin_support` (
  `Emp_ID` varchar(15) NOT NULL,
  `ASType` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`Emp_ID`),
  CONSTRAINT `admin_support_ibfk_1` FOREIGN KEY (`Emp_ID`) REFERENCES `employee` (`emp_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin_support`
--

LOCK TABLES `admin_support` WRITE;
/*!40000 ALTER TABLE `admin_support` DISABLE KEYS */;
INSERT INTO `admin_support` VALUES ('EMP 28742','Administrator');
/*!40000 ALTER TABLE `admin_support` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `airline`
--

DROP TABLE IF EXISTS `airline`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `airline` (
  `Air_ID` varchar(6) NOT NULL,
  `Air_Name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`Air_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `airline`
--

LOCK TABLES `airline` WRITE;
/*!40000 ALTER TABLE `airline` DISABLE KEYS */;
INSERT INTO `airline` VALUES ('AI 123','Air India'),('GA 478','Go Air'),('IG 213','Go Indigo'),('JA 344','Jet Airways'),('LA 987','Lufthansa'),('SJ 434','Spicejet');
/*!40000 ALTER TABLE `airline` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `airport`
--

DROP TABLE IF EXISTS `airport`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `airport` (
  `A_Name` varchar(50) NOT NULL,
  `A_State` varchar(50) DEFAULT NULL,
  `A_Country` varchar(50) DEFAULT NULL,
  `city_name` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`A_Name`),
  KEY `city_name` (`city_name`),
  CONSTRAINT `airport_ibfk_1` FOREIGN KEY (`city_name`) REFERENCES `city` (`city_name`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `airport`
--

LOCK TABLES `airport` WRITE;
/*!40000 ALTER TABLE `airport` DISABLE KEYS */;
INSERT INTO `airport` VALUES ('Chhatrapati Shivaji Maharaj International Airport','Maharashtra','India','Mumbai'),('Indira Gandhi International Airport','Haryana','India','Gurgaon'),('Jaipur International Airport','Rajasthan','India','Jaipur'),('Sardar Vallabhbhai Patel International Airport','Gujarat','India','Ahmedabad');
/*!40000 ALTER TABLE `airport` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `airport_consists_of`
--

DROP TABLE IF EXISTS `airport_consists_of`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `airport_consists_of` (
  `A_Name` varchar(50) NOT NULL,
  `Air_ID` varchar(6) NOT NULL,
  PRIMARY KEY (`A_Name`,`Air_ID`),
  KEY `airport_consists_of_ibfk_2` (`Air_ID`),
  CONSTRAINT `airport_consists_of_ibfk_1` FOREIGN KEY (`A_Name`) REFERENCES `airport` (`A_Name`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `airport_consists_of_ibfk_2` FOREIGN KEY (`Air_ID`) REFERENCES `airline` (`Air_ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `airport_consists_of`
--

LOCK TABLES `airport_consists_of` WRITE;
/*!40000 ALTER TABLE `airport_consists_of` DISABLE KEYS */;
INSERT INTO `airport_consists_of` VALUES ('Jaipur International Airport','AI 123'),('Chhatrapati Shivaji Maharaj International Airport','GA 478'),('Indira Gandhi International Airport','GA 478'),('Indira Gandhi International Airport','IG 213'),('Jaipur International Airport','LA 987'),('Sardar Vallabhbhai Patel International Airport','LA 987');
/*!40000 ALTER TABLE `airport_consists_of` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `city`
--

DROP TABLE IF EXISTS `city`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `city` (
  `city_name` varchar(30) NOT NULL,
  `State` varchar(50) DEFAULT NULL,
  `Country` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`city_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `city`
--

LOCK TABLES `city` WRITE;
/*!40000 ALTER TABLE `city` DISABLE KEYS */;
INSERT INTO `city` VALUES ('Ahmedabad','Gujarat','India'),('Gurgaon','Haryana','India'),('Jaipur','Rajasthan','India'),('Mumbai','Maharashtra','India');
/*!40000 ALTER TABLE `city` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `connecting_flight`
--

DROP TABLE IF EXISTS `connecting_flight`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `connecting_flight` (
  `FNo` varchar(6) NOT NULL,
  `layover_time` time DEFAULT NULL,
  `no_of_stops` int DEFAULT NULL,
  PRIMARY KEY (`FNo`),
  CONSTRAINT `connecting_flight_ibfk_1` FOREIGN KEY (`FNo`) REFERENCES `flight` (`FNo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `connecting_flight`
--

LOCK TABLES `connecting_flight` WRITE;
/*!40000 ALTER TABLE `connecting_flight` DISABLE KEYS */;
INSERT INTO `connecting_flight` VALUES ('JA7543','07:00:00',1);
/*!40000 ALTER TABLE `connecting_flight` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee` (
  `emp_id` varchar(15) NOT NULL,
  `EFirst_Name` varchar(20) DEFAULT NULL,
  `ELast_Name` varchar(20) DEFAULT NULL,
  `E_Street` varchar(45) DEFAULT NULL,
  `E_City` varchar(40) DEFAULT NULL,
  `E_State` varchar(45) DEFAULT NULL,
  `E_PINCode` int DEFAULT NULL,
  `Emp_MNo` bigint DEFAULT NULL,
  `Emp_Sex` varchar(1) DEFAULT NULL,
  `Emp_DOB` date DEFAULT NULL,
  `Emp_Salary` int DEFAULT NULL,
  `EDesignation` varchar(30) DEFAULT NULL,
  `A_Name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`emp_id`),
  KEY `A_Name` (`A_Name`),
  CONSTRAINT `employee_ibfk_1` FOREIGN KEY (`A_Name`) REFERENCES `airport` (`A_Name`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
INSERT INTO `employee` VALUES ('EMP 28742','Manasvi','Kothari','Mahal','Nagpur','Maharashtra',440032,9783628202,'F','2002-06-17',100000,'Manager','Jaipur International Airport'),('EMP 67467','Rovin','Singh','Boisar','Mumbai','Maharashtra',401501,9567456342,'M','2002-11-20',90000,'Assistant Manager','Indira Gandhi International Airport');
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee_handles`
--

DROP TABLE IF EXISTS `employee_handles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee_handles` (
  `Emp_ID` varchar(15) NOT NULL,
  `P_ID` varchar(15) NOT NULL,
  PRIMARY KEY (`Emp_ID`,`P_ID`),
  KEY `P_ID` (`P_ID`),
  CONSTRAINT `employee_handles_ibfk_1` FOREIGN KEY (`Emp_ID`) REFERENCES `employee` (`emp_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `employee_handles_ibfk_2` FOREIGN KEY (`P_ID`) REFERENCES `passenger` (`P_ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee_handles`
--

LOCK TABLES `employee_handles` WRITE;
/*!40000 ALTER TABLE `employee_handles` DISABLE KEYS */;
INSERT INTO `employee_handles` VALUES ('EMP 28742','PS 37656'),('EMP 67467','PS 89722');
/*!40000 ALTER TABLE `employee_handles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `engineer`
--

DROP TABLE IF EXISTS `engineer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `engineer` (
  `Emp_ID` varchar(15) NOT NULL,
  `EType` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`Emp_ID`),
  CONSTRAINT `engineer_ibfk_1` FOREIGN KEY (`Emp_ID`) REFERENCES `employee` (`emp_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `engineer`
--

LOCK TABLES `engineer` WRITE;
/*!40000 ALTER TABLE `engineer` DISABLE KEYS */;
INSERT INTO `engineer` VALUES ('EMP 67467','Software Tester');
/*!40000 ALTER TABLE `engineer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `flight`
--

DROP TABLE IF EXISTS `flight`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `flight` (
  `FNo` varchar(6) NOT NULL,
  `FSource` varchar(45) DEFAULT NULL,
  `FDest` varchar(45) DEFAULT NULL,
  `fdepart_time` datetime DEFAULT NULL,
  `farr_time` datetime DEFAULT NULL,
  `FDuration` varchar(45) DEFAULT NULL,
  `FStatus` varchar(45) DEFAULT NULL,
  `Air_ID` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`FNo`),
  KEY `Air_ID` (`Air_ID`),
  CONSTRAINT `flight_ibfk_1` FOREIGN KEY (`Air_ID`) REFERENCES `airline` (`Air_ID`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `flight`
--

LOCK TABLES `flight` WRITE;
/*!40000 ALTER TABLE `flight` DISABLE KEYS */;
INSERT INTO `flight` VALUES ('AI2014','BOM','DFW','2022-03-30 02:10:00','2022-03-30 03:15:00','1:05','On Time','AI 123'),('GA1562','JFK','TPA','2022-03-12 13:00:00','2022-03-12 13:55:00','00:55','Delayed','GA 478'),('JA7543','FRA','DEL','2022-03-15 06:00:00','2022-03-16 05:00:00','23:00','On Time','JA 344');
/*!40000 ALTER TABLE `flight` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `flight_info`
--

DROP TABLE IF EXISTS `flight_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `flight_info` (
  `FNo` varchar(6) DEFAULT NULL,
  `NB_ID` varchar(15) DEFAULT NULL,
  KEY `FNo` (`FNo`),
  KEY `NB_ID` (`NB_ID`),
  CONSTRAINT `flight_info_ibfk_1` FOREIGN KEY (`FNo`) REFERENCES `flight` (`FNo`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `flight_info_ibfk_2` FOREIGN KEY (`NB_ID`) REFERENCES `notice_board` (`NB_ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `flight_info`
--

LOCK TABLES `flight_info` WRITE;
/*!40000 ALTER TABLE `flight_info` DISABLE KEYS */;
/*!40000 ALTER TABLE `flight_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `flight_passenger_transmits`
--

DROP TABLE IF EXISTS `flight_passenger_transmits`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `flight_passenger_transmits` (
  `FNo` varchar(6) NOT NULL,
  `P_ID` varchar(15) NOT NULL,
  `NB_ID` varchar(15) NOT NULL,
  PRIMARY KEY (`FNo`,`P_ID`,`NB_ID`),
  KEY `P_ID` (`P_ID`),
  KEY `NB_ID` (`NB_ID`),
  CONSTRAINT `flight_passenger_transmits_ibfk_1` FOREIGN KEY (`FNo`) REFERENCES `flight` (`FNo`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `flight_passenger_transmits_ibfk_2` FOREIGN KEY (`P_ID`) REFERENCES `passenger` (`P_ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `flight_passenger_transmits_ibfk_3` FOREIGN KEY (`NB_ID`) REFERENCES `notice_board` (`NB_ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `flight_passenger_transmits`
--

LOCK TABLES `flight_passenger_transmits` WRITE;
/*!40000 ALTER TABLE `flight_passenger_transmits` DISABLE KEYS */;
INSERT INTO `flight_passenger_transmits` VALUES ('AI2014','PS 89722','NB 1038');
/*!40000 ALTER TABLE `flight_passenger_transmits` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `luggage`
--

DROP TABLE IF EXISTS `luggage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `luggage` (
  `P_ID` varchar(15) NOT NULL,
  `Luggage_ID` varchar(20) NOT NULL,
  `No_of_bags` int DEFAULT NULL,
  PRIMARY KEY (`P_ID`,`Luggage_ID`),
  CONSTRAINT `luggage_ibfk_1` FOREIGN KEY (`P_ID`) REFERENCES `passenger` (`P_ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `luggage`
--

LOCK TABLES `luggage` WRITE;
/*!40000 ALTER TABLE `luggage` DISABLE KEYS */;
INSERT INTO `luggage` VALUES ('PS 37656','L 252',3),('PS 89722','L 577',2),('PS 89722','L 654',4);
/*!40000 ALTER TABLE `luggage` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `non_stop_flight`
--

DROP TABLE IF EXISTS `non_stop_flight`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `non_stop_flight` (
  `FNo` varchar(6) NOT NULL,
  PRIMARY KEY (`FNo`),
  CONSTRAINT `non_stop_flight_ibfk_1` FOREIGN KEY (`FNo`) REFERENCES `flight` (`FNo`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `non_stop_flight`
--

LOCK TABLES `non_stop_flight` WRITE;
/*!40000 ALTER TABLE `non_stop_flight` DISABLE KEYS */;
INSERT INTO `non_stop_flight` VALUES ('AI2014');
/*!40000 ALTER TABLE `non_stop_flight` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `notice_board`
--

DROP TABLE IF EXISTS `notice_board`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `notice_board` (
  `NB_ID` varchar(15) NOT NULL,
  `Gate_No` int DEFAULT NULL,
  `NB_arr` datetime DEFAULT NULL,
  `NB_depart` datetime DEFAULT NULL,
  `NB_Source` varchar(30) DEFAULT NULL,
  `NB_Dest` varchar(30) DEFAULT NULL,
  `NB_Status` varchar(25) DEFAULT NULL,
  `Terminal` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`NB_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `notice_board`
--

LOCK TABLES `notice_board` WRITE;
/*!40000 ALTER TABLE `notice_board` DISABLE KEYS */;
INSERT INTO `notice_board` VALUES ('NB 1038',6,'2022-03-12 13:55:00','2022-03-12 13:00:00','JFK','TPA','Delayed','T3');
/*!40000 ALTER TABLE `notice_board` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `passenger`
--

DROP TABLE IF EXISTS `passenger`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `passenger` (
  `P_ID` varchar(15) NOT NULL,
  `PFirst_Name` varchar(25) DEFAULT NULL,
  `PLast_Name` varchar(25) DEFAULT NULL,
  `P_MNo` bigint DEFAULT NULL,
  `P_DoB` date DEFAULT NULL,
  `P_Sex` varchar(1) DEFAULT NULL,
  `P_IDNo` varchar(20) DEFAULT NULL,
  `P_IDType` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`P_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `passenger`
--

LOCK TABLES `passenger` WRITE;
/*!40000 ALTER TABLE `passenger` DISABLE KEYS */;
INSERT INTO `passenger` VALUES ('PS 37656','Darshan','Patil	',9247965443,'2001-09-05','M','475437964865','Aadhaar Card'),('PS 89722','Pranav','Ninawe',9363836203,'2001-10-07','M','80273625','Passport');
/*!40000 ALTER TABLE `passenger` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ticket`
--

DROP TABLE IF EXISTS `ticket`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ticket` (
  `Ticket_No` varchar(13) NOT NULL,
  `Air_Name` varchar(50) DEFAULT NULL,
  `Ticket_Price` int DEFAULT NULL,
  `Seat_No` varchar(10) DEFAULT NULL,
  `Class` varchar(15) DEFAULT NULL,
  `Arr` datetime DEFAULT NULL,
  `Depart` datetime DEFAULT NULL,
  `Duration` time DEFAULT NULL,
  `DO_Travel` date DEFAULT NULL,
  `P_Source` varchar(50) DEFAULT NULL,
  `P_Dest` varchar(50) DEFAULT NULL,
  `Terminal` varchar(30) DEFAULT NULL,
  `P_ID` varchar(15) DEFAULT NULL,
  `DO_Book` date DEFAULT NULL,
  `do_cancel` varchar(10) DEFAULT NULL,
  `charge` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`Ticket_No`),
  KEY `P_ID` (`P_ID`),
  CONSTRAINT `ticket_ibfk_1` FOREIGN KEY (`P_ID`) REFERENCES `passenger` (`P_ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ticket`
--

LOCK TABLES `ticket` WRITE;
/*!40000 ALTER TABLE `ticket` DISABLE KEYS */;
INSERT INTO `ticket` VALUES ('TN 329672','Lufthansa',50000,'F 26','Economy','2022-03-16 05:00:00','2022-03-15 06:00:00','23:00:00','2022-03-15','FRA','DEL','T3','PS 37656','2022-02-21','2022-03-03','5000');
/*!40000 ALTER TABLE `ticket` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-03-31  6:09:47
