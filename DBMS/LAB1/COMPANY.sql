-- MySQL dump 10.13  Distrib 5.7.27, for Linux (x86_64)
--
-- Host: localhost    Database: COMPANY
-- ------------------------------------------------------
-- Server version	5.7.27-0ubuntu0.16.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `DEPARTMENT`
--

DROP TABLE IF EXISTS `DEPARTMENT`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `DEPARTMENT` (
  `Dname` char(20) NOT NULL,
  `Dnumber` int(3) NOT NULL,
  `Mgr_ssn` bigint(12) DEFAULT NULL,
  `Mgr_start_date` date DEFAULT NULL,
  PRIMARY KEY (`Dnumber`),
  KEY `Mgr_ssn` (`Mgr_ssn`),
  CONSTRAINT `DEPARTMENT_ibfk_1` FOREIGN KEY (`Mgr_ssn`) REFERENCES `EMPLOYEE` (`ssn`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `DEPARTMENT`
--

LOCK TABLES `DEPARTMENT` WRITE;
/*!40000 ALTER TABLE `DEPARTMENT` DISABLE KEYS */;
INSERT INTO `DEPARTMENT` VALUES ('Headquarters',1,888665555,'1981-06-19'),('Administration',4,987654321,'1995-01-01'),('Research',5,333445555,'1988-05-22');
/*!40000 ALTER TABLE `DEPARTMENT` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `DEPENDENT`
--

DROP TABLE IF EXISTS `DEPENDENT`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `DEPENDENT` (
  `Essn` bigint(12) DEFAULT NULL,
  `Dependent_name` char(12) DEFAULT NULL,
  `sex` char(2) DEFAULT NULL,
  `Bdate` date DEFAULT NULL,
  `Relationship` char(12) DEFAULT NULL,
  KEY `Essn` (`Essn`),
  CONSTRAINT `DEPENDENT_ibfk_1` FOREIGN KEY (`Essn`) REFERENCES `EMPLOYEE` (`ssn`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `DEPENDENT`
--

LOCK TABLES `DEPENDENT` WRITE;
/*!40000 ALTER TABLE `DEPENDENT` DISABLE KEYS */;
INSERT INTO `DEPENDENT` VALUES (333445555,'Alice','F','1986-04-05','Daughter'),(333445555,'Thoodore','M','1983-10-25','Son'),(333445555,'Joy','F','1958-05-03','Spouse'),(987654321,'Abner','M','1942-02-28','Spouse'),(123456789,'Michael','M','1988-01-04','Son'),(123456789,'Alice','F','1988-12-30','Daughter'),(123456789,'Elizabeth','F','1967-05-05','Spouse');
/*!40000 ALTER TABLE `DEPENDENT` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `DEPT_LOCATIONS`
--

DROP TABLE IF EXISTS `DEPT_LOCATIONS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `DEPT_LOCATIONS` (
  `Dnumber` int(3) DEFAULT NULL,
  `Dlocation` char(20) DEFAULT NULL,
  KEY `Dnumber` (`Dnumber`),
  CONSTRAINT `DEPT_LOCATIONS_ibfk_1` FOREIGN KEY (`Dnumber`) REFERENCES `DEPARTMENT` (`Dnumber`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `DEPT_LOCATIONS`
--

LOCK TABLES `DEPT_LOCATIONS` WRITE;
/*!40000 ALTER TABLE `DEPT_LOCATIONS` DISABLE KEYS */;
INSERT INTO `DEPT_LOCATIONS` VALUES (1,'Houston'),(4,'Stafford'),(5,'Bellaire'),(5,'Sugarland'),(5,'Houston');
/*!40000 ALTER TABLE `DEPT_LOCATIONS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `EMPLOYEE`
--

DROP TABLE IF EXISTS `EMPLOYEE`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `EMPLOYEE` (
  `Fname` char(20) DEFAULT NULL,
  `Minit` char(5) DEFAULT NULL,
  `Lname` char(20) DEFAULT NULL,
  `ssn` bigint(12) NOT NULL,
  `Bdate` date DEFAULT NULL,
  `Address` tinytext,
  `Sex` char(5) DEFAULT NULL,
  `Salary` bigint(10) DEFAULT NULL,
  `Super_ssn` bigint(12) DEFAULT NULL,
  `Dno` int(5) DEFAULT NULL,
  PRIMARY KEY (`ssn`),
  KEY `Dno` (`Dno`),
  KEY `Super_ssn` (`Super_ssn`),
  CONSTRAINT `EMPLOYEE_ibfk_1` FOREIGN KEY (`Dno`) REFERENCES `DEPARTMENT` (`Dnumber`),
  CONSTRAINT `EMPLOYEE_ibfk_2` FOREIGN KEY (`Super_ssn`) REFERENCES `EMPLOYEE` (`ssn`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `EMPLOYEE`
--

LOCK TABLES `EMPLOYEE` WRITE;
/*!40000 ALTER TABLE `EMPLOYEE` DISABLE KEYS */;
INSERT INTO `EMPLOYEE` VALUES ('John','B','Smith',123456789,'1965-01-09','731 Fondren, Houston, TX','M',30000,333445555,5),('Franklin','T','Wong',333445555,'1955-12-08','638 Voss, Houston, TX','M',40000,888665555,5),('Joyce','A','English',453453453,'1972-07-31','5631 Rice, Houston, TX','F',25000,333445555,5),('Ramesh','K','Narayan',666884444,'1962-09-15','975 Fire Oak, Humble, TX','M',38000,333445555,5),('James','E','Borg',888665555,'1937-11-10','450 Stone, Houston, TX','M',55000,NULL,1),('Jennifer','S','Wallace',987654321,'1941-06-20','321 Berry, Bellaire, TX','F',43000,888665555,4),('Alicia','J','Zelaya',999887777,'1968-01-19','3321 Castle, Spring, TX','F',25000,987654321,4);
/*!40000 ALTER TABLE `EMPLOYEE` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `PROJECT`
--

DROP TABLE IF EXISTS `PROJECT`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `PROJECT` (
  `Pname` char(15) NOT NULL,
  `Pnumber` int(3) NOT NULL,
  `Plocation` char(12) DEFAULT NULL,
  `Dnum` int(3) DEFAULT NULL,
  PRIMARY KEY (`Pnumber`),
  KEY `Dnum` (`Dnum`),
  CONSTRAINT `PROJECT_ibfk_1` FOREIGN KEY (`Dnum`) REFERENCES `DEPARTMENT` (`Dnumber`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PROJECT`
--

LOCK TABLES `PROJECT` WRITE;
/*!40000 ALTER TABLE `PROJECT` DISABLE KEYS */;
INSERT INTO `PROJECT` VALUES ('ProductX',1,'Bellaire',5),('ProductY',2,'Sugarland',5),('ProductZ',3,'Houston',5),('ProductX',10,'Stafford',4),('ProductX',20,'Houston',1),('ProductX',30,'Stafford',4);
/*!40000 ALTER TABLE `PROJECT` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `WORKS_ON`
--

DROP TABLE IF EXISTS `WORKS_ON`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `WORKS_ON` (
  `Essn` bigint(12) NOT NULL,
  `Pno` int(3) DEFAULT NULL,
  `Hours` float DEFAULT NULL,
  KEY `Pno` (`Pno`),
  KEY `Essn` (`Essn`),
  CONSTRAINT `WORKS_ON_ibfk_1` FOREIGN KEY (`Pno`) REFERENCES `PROJECT` (`Pnumber`),
  CONSTRAINT `WORKS_ON_ibfk_2` FOREIGN KEY (`Essn`) REFERENCES `EMPLOYEE` (`ssn`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `WORKS_ON`
--

LOCK TABLES `WORKS_ON` WRITE;
/*!40000 ALTER TABLE `WORKS_ON` DISABLE KEYS */;
INSERT INTO `WORKS_ON` VALUES (123456789,2,7.5),(123456789,1,32.5),(333445555,2,10),(453453453,1,20),(666884444,3,40),(888665555,20,1),(987654321,30,20),(999887777,10,10);
/*!40000 ALTER TABLE `WORKS_ON` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-08-27 15:51:30
