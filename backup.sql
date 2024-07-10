-- MySQL dump 10.13  Distrib 8.0.37, for Linux (x86_64)
--
-- Host: localhost    Database: hms_ccai
-- ------------------------------------------------------
-- Server version	8.0.37-0ubuntu0.24.04.1

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
-- Table structure for table `accounts_accountledger`
--

DROP TABLE IF EXISTS `accounts_accountledger`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts_accountledger` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `account_name` varchar(100) NOT NULL,
  `balance` decimal(10,2) NOT NULL,
  `owner_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `accounts_accountledg_owner_id_43a339fa_fk_hos_login` (`owner_id`),
  CONSTRAINT `accounts_accountledg_owner_id_43a339fa_fk_hos_login` FOREIGN KEY (`owner_id`) REFERENCES `hos_login_custom_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_accountledger`
--

LOCK TABLES `accounts_accountledger` WRITE;
/*!40000 ALTER TABLE `accounts_accountledger` DISABLE KEYS */;
/*!40000 ALTER TABLE `accounts_accountledger` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `accounts_bankaccount`
--

DROP TABLE IF EXISTS `accounts_bankaccount`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts_bankaccount` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `account_name` varchar(100) NOT NULL,
  `balance` decimal(10,2) NOT NULL,
  `owner_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `accounts_bankaccount_owner_id_c280ffba_fk_hos_login` (`owner_id`),
  CONSTRAINT `accounts_bankaccount_owner_id_c280ffba_fk_hos_login` FOREIGN KEY (`owner_id`) REFERENCES `hos_login_custom_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_bankaccount`
--

LOCK TABLES `accounts_bankaccount` WRITE;
/*!40000 ALTER TABLE `accounts_bankaccount` DISABLE KEYS */;
/*!40000 ALTER TABLE `accounts_bankaccount` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `accounts_cashbook`
--

DROP TABLE IF EXISTS `accounts_cashbook`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts_cashbook` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `transaction_type` varchar(100) NOT NULL,
  `amount` decimal(10,2) NOT NULL,
  `date` date NOT NULL,
  `owner_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `accounts_cashbook_owner_id_85fc13d8_fk_hos_login_custom_user_id` (`owner_id`),
  CONSTRAINT `accounts_cashbook_owner_id_85fc13d8_fk_hos_login_custom_user_id` FOREIGN KEY (`owner_id`) REFERENCES `hos_login_custom_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_cashbook`
--

LOCK TABLES `accounts_cashbook` WRITE;
/*!40000 ALTER TABLE `accounts_cashbook` DISABLE KEYS */;
/*!40000 ALTER TABLE `accounts_cashbook` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `accounts_paymentvoucher`
--

DROP TABLE IF EXISTS `accounts_paymentvoucher`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts_paymentvoucher` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `amount_paid` decimal(10,2) NOT NULL,
  `date_paid` date NOT NULL,
  `owner_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `accounts_paymentvouc_owner_id_0604d031_fk_hos_login` (`owner_id`),
  CONSTRAINT `accounts_paymentvouc_owner_id_0604d031_fk_hos_login` FOREIGN KEY (`owner_id`) REFERENCES `hos_login_custom_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_paymentvoucher`
--

LOCK TABLES `accounts_paymentvoucher` WRITE;
/*!40000 ALTER TABLE `accounts_paymentvoucher` DISABLE KEYS */;
/*!40000 ALTER TABLE `accounts_paymentvoucher` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `accounts_receiptvoucher`
--

DROP TABLE IF EXISTS `accounts_receiptvoucher`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts_receiptvoucher` (
  `id` char(32) NOT NULL,
  `amount_received` decimal(10,2) NOT NULL,
  `date_received` date NOT NULL,
  `owner_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `accounts_receiptvouc_owner_id_dcad6c72_fk_hos_login` (`owner_id`),
  CONSTRAINT `accounts_receiptvouc_owner_id_dcad6c72_fk_hos_login` FOREIGN KEY (`owner_id`) REFERENCES `hos_login_custom_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_receiptvoucher`
--

LOCK TABLES `accounts_receiptvoucher` WRITE;
/*!40000 ALTER TABLE `accounts_receiptvoucher` DISABLE KEYS */;
/*!40000 ALTER TABLE `accounts_receiptvoucher` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=245 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add patient',6,'add_patient'),(22,'Can change patient',6,'change_patient'),(23,'Can delete patient',6,'delete_patient'),(24,'Can view patient',6,'view_patient'),(25,'Can add treatment information',7,'add_treatmentinformation'),(26,'Can change treatment information',7,'change_treatmentinformation'),(27,'Can delete treatment information',7,'delete_treatmentinformation'),(28,'Can view treatment information',7,'view_treatmentinformation'),(29,'Can add patient visit list',8,'add_patientvisitlist'),(30,'Can change patient visit list',8,'change_patientvisitlist'),(31,'Can delete patient visit list',8,'delete_patientvisitlist'),(32,'Can view patient visit list',8,'view_patientvisitlist'),(33,'Can add patient reminder',9,'add_patientreminder'),(34,'Can change patient reminder',9,'change_patientreminder'),(35,'Can delete patient reminder',9,'delete_patientreminder'),(36,'Can view patient reminder',9,'view_patientreminder'),(37,'Can add patient ledger',10,'add_patientledger'),(38,'Can change patient ledger',10,'change_patientledger'),(39,'Can delete patient ledger',10,'delete_patientledger'),(40,'Can view patient ledger',10,'view_patientledger'),(41,'Can add patient history',11,'add_patienthistory'),(42,'Can change patient history',11,'change_patienthistory'),(43,'Can delete patient history',11,'delete_patienthistory'),(44,'Can view patient history',11,'view_patienthistory'),(45,'Can add patient billing',12,'add_patientbilling'),(46,'Can change patient billing',12,'change_patientbilling'),(47,'Can delete patient billing',12,'delete_patientbilling'),(48,'Can view patient billing',12,'view_patientbilling'),(49,'Can add hospital',13,'add_hospital'),(50,'Can change hospital',13,'change_hospital'),(51,'Can delete hospital',13,'delete_hospital'),(52,'Can view hospital',13,'view_hospital'),(53,'Can add custom_ user',14,'add_custom_user'),(54,'Can change custom_ user',14,'change_custom_user'),(55,'Can delete custom_ user',14,'delete_custom_user'),(56,'Can view custom_ user',14,'view_custom_user'),(57,'Can add op d_register',15,'add_opd_register'),(58,'Can change op d_register',15,'change_opd_register'),(59,'Can delete op d_register',15,'delete_opd_register'),(60,'Can view op d_register',15,'view_opd_register'),(61,'Can add op d_ billing',16,'add_opd_billing'),(62,'Can change op d_ billing',16,'change_opd_billing'),(63,'Can delete op d_ billing',16,'delete_opd_billing'),(64,'Can view op d_ billing',16,'view_opd_billing'),(65,'Can add op d_report',17,'add_opd_report'),(66,'Can change op d_report',17,'change_opd_report'),(67,'Can delete op d_report',17,'delete_opd_report'),(68,'Can view op d_report',17,'view_opd_report'),(69,'Can add op d_prescription',18,'add_opd_prescription'),(70,'Can change op d_prescription',18,'change_opd_prescription'),(71,'Can delete op d_prescription',18,'delete_opd_prescription'),(72,'Can view op d_prescription',18,'view_opd_prescription'),(73,'Can add opdtoipdtransfer',19,'add_opdtoipdtransfer'),(74,'Can change opdtoipdtransfer',19,'change_opdtoipdtransfer'),(75,'Can delete opdtoipdtransfer',19,'delete_opdtoipdtransfer'),(76,'Can view opdtoipdtransfer',19,'view_opdtoipdtransfer'),(77,'Can add opd patient summary',20,'add_opdpatientsummary'),(78,'Can change opd patient summary',20,'change_opdpatientsummary'),(79,'Can delete opd patient summary',20,'delete_opdpatientsummary'),(80,'Can view opd patient summary',20,'view_opdpatientsummary'),(81,'Can add depwisereport',21,'add_depwisereport'),(82,'Can change depwisereport',21,'change_depwisereport'),(83,'Can delete depwisereport',21,'delete_depwisereport'),(84,'Can view depwisereport',21,'view_depwisereport'),(85,'Can add ref doctor report',22,'add_refdoctorreport'),(86,'Can change ref doctor report',22,'change_refdoctorreport'),(87,'Can delete ref doctor report',22,'delete_refdoctorreport'),(88,'Can view ref doctor report',22,'view_refdoctorreport'),(89,'Can add consultant doctor report',23,'add_consultantdoctorreport'),(90,'Can change consultant doctor report',23,'change_consultantdoctorreport'),(91,'Can delete consultant doctor report',23,'delete_consultantdoctorreport'),(92,'Can view consultant doctor report',23,'view_consultantdoctorreport'),(93,'Can add receipt voucher',24,'add_receiptvoucher'),(94,'Can change receipt voucher',24,'change_receiptvoucher'),(95,'Can delete receipt voucher',24,'delete_receiptvoucher'),(96,'Can view receipt voucher',24,'view_receiptvoucher'),(97,'Can add payment voucher',25,'add_paymentvoucher'),(98,'Can change payment voucher',25,'change_paymentvoucher'),(99,'Can delete payment voucher',25,'delete_paymentvoucher'),(100,'Can view payment voucher',25,'view_paymentvoucher'),(101,'Can add cashbook',26,'add_cashbook'),(102,'Can change cashbook',26,'change_cashbook'),(103,'Can delete cashbook',26,'delete_cashbook'),(104,'Can view cashbook',26,'view_cashbook'),(105,'Can add bank account',27,'add_bankaccount'),(106,'Can change bank account',27,'change_bankaccount'),(107,'Can delete bank account',27,'delete_bankaccount'),(108,'Can view bank account',27,'view_bankaccount'),(109,'Can add account ledger',28,'add_accountledger'),(110,'Can change account ledger',28,'change_accountledger'),(111,'Can delete account ledger',28,'delete_accountledger'),(112,'Can view account ledger',28,'view_accountledger'),(113,'Can add bed',29,'add_bed'),(114,'Can change bed',29,'change_bed'),(115,'Can delete bed',29,'delete_bed'),(116,'Can view bed',29,'view_bed'),(117,'Can add ipd deposit',30,'add_ipddeposit'),(118,'Can change ipd deposit',30,'change_ipddeposit'),(119,'Can delete ipd deposit',30,'delete_ipddeposit'),(120,'Can view ipd deposit',30,'view_ipddeposit'),(121,'Can add ipd discharge',31,'add_ipddischarge'),(122,'Can change ipd discharge',31,'change_ipddischarge'),(123,'Can delete ipd discharge',31,'delete_ipddischarge'),(124,'Can view ipd discharge',31,'view_ipddischarge'),(125,'Can add ward',32,'add_ward'),(126,'Can change ward',32,'change_ward'),(127,'Can delete ward',32,'delete_ward'),(128,'Can view ward',32,'view_ward'),(129,'Can add ward wise report',33,'add_wardwisereport'),(130,'Can change ward wise report',33,'change_wardwisereport'),(131,'Can delete ward wise report',33,'delete_wardwisereport'),(132,'Can view ward wise report',33,'view_wardwisereport'),(133,'Can add ward wise bed report',34,'add_wardwisebedreport'),(134,'Can change ward wise bed report',34,'change_wardwisebedreport'),(135,'Can delete ward wise bed report',34,'delete_wardwisebedreport'),(136,'Can view ward wise bed report',34,'view_wardwisebedreport'),(137,'Can add tpa report',35,'add_tpareport'),(138,'Can change tpa report',35,'change_tpareport'),(139,'Can delete tpa report',35,'delete_tpareport'),(140,'Can view tpa report',35,'view_tpareport'),(141,'Can add ipd registration',36,'add_ipdregistration'),(142,'Can change ipd registration',36,'change_ipdregistration'),(143,'Can delete ipd registration',36,'delete_ipdregistration'),(144,'Can view ipd registration',36,'view_ipdregistration'),(145,'Can add ipd discharge report',37,'add_ipddischargereport'),(146,'Can change ipd discharge report',37,'change_ipddischargereport'),(147,'Can delete ipd discharge report',37,'delete_ipddischargereport'),(148,'Can view ipd discharge report',37,'view_ipddischargereport'),(149,'Can add ipd deposit report',38,'add_ipddepositreport'),(150,'Can change ipd deposit report',38,'change_ipddepositreport'),(151,'Can delete ipd deposit report',38,'delete_ipddepositreport'),(152,'Can view ipd deposit report',38,'view_ipddepositreport'),(153,'Can add ipd admit report',39,'add_ipdadmitreport'),(154,'Can change ipd admit report',39,'change_ipdadmitreport'),(155,'Can delete ipd admit report',39,'delete_ipdadmitreport'),(156,'Can view ipd admit report',39,'view_ipdadmitreport'),(157,'Can add doctor wise report',40,'add_doctorwisereport'),(158,'Can change doctor wise report',40,'change_doctorwisereport'),(159,'Can delete doctor wise report',40,'delete_doctorwisereport'),(160,'Can view doctor wise report',40,'view_doctorwisereport'),(161,'Can add discharge history',41,'add_dischargehistory'),(162,'Can change discharge history',41,'change_dischargehistory'),(163,'Can delete discharge history',41,'delete_dischargehistory'),(164,'Can view discharge history',41,'view_dischargehistory'),(165,'Can add department report',42,'add_departmentreport'),(166,'Can change department report',42,'change_departmentreport'),(167,'Can delete department report',42,'delete_departmentreport'),(168,'Can view department report',42,'view_departmentreport'),(169,'Can add bed status update',43,'add_bedstatusupdate'),(170,'Can change bed status update',43,'change_bedstatusupdate'),(171,'Can delete bed status update',43,'delete_bedstatusupdate'),(172,'Can view bed status update',43,'view_bedstatusupdate'),(173,'Can add bed booking',44,'add_bedbooking'),(174,'Can change bed booking',44,'change_bedbooking'),(175,'Can delete bed booking',44,'delete_bedbooking'),(176,'Can view bed booking',44,'view_bedbooking'),(177,'Can add bed availability',45,'add_bedavailability'),(178,'Can change bed availability',45,'change_bedavailability'),(179,'Can delete bed availability',45,'delete_bedavailability'),(180,'Can view bed availability',45,'view_bedavailability'),(181,'Can add bed allocation',46,'add_bedallocation'),(182,'Can change bed allocation',46,'change_bedallocation'),(183,'Can delete bed allocation',46,'delete_bedallocation'),(184,'Can view bed allocation',46,'view_bedallocation'),(185,'Can add doctor',47,'add_doctor'),(186,'Can change doctor',47,'change_doctor'),(187,'Can delete doctor',47,'delete_doctor'),(188,'Can view doctor',47,'view_doctor'),(189,'Can add equipment',48,'add_equipment'),(190,'Can change equipment',48,'change_equipment'),(191,'Can delete equipment',48,'delete_equipment'),(192,'Can view equipment',48,'view_equipment'),(193,'Can add inventory item',49,'add_inventoryitem'),(194,'Can change inventory item',49,'change_inventoryitem'),(195,'Can delete inventory item',49,'delete_inventoryitem'),(196,'Can view inventory item',49,'view_inventoryitem'),(197,'Can add stock level alert',50,'add_stocklevelalert'),(198,'Can change stock level alert',50,'change_stocklevelalert'),(199,'Can delete stock level alert',50,'delete_stocklevelalert'),(200,'Can view stock level alert',50,'view_stocklevelalert'),(201,'Can add purchase order',51,'add_purchaseorder'),(202,'Can change purchase order',51,'change_purchaseorder'),(203,'Can delete purchase order',51,'delete_purchaseorder'),(204,'Can view purchase order',51,'view_purchaseorder'),(205,'Can add patient equipment usage',52,'add_patientequipmentusage'),(206,'Can change patient equipment usage',52,'change_patientequipmentusage'),(207,'Can delete patient equipment usage',52,'delete_patientequipmentusage'),(208,'Can view patient equipment usage',52,'view_patientequipmentusage'),(209,'Can add medicine',53,'add_medicine'),(210,'Can change medicine',53,'change_medicine'),(211,'Can delete medicine',53,'delete_medicine'),(212,'Can view medicine',53,'view_medicine'),(213,'Can add medicine equipment usage',54,'add_medicineequipmentusage'),(214,'Can change medicine equipment usage',54,'change_medicineequipmentusage'),(215,'Can delete medicine equipment usage',54,'delete_medicineequipmentusage'),(216,'Can view medicine equipment usage',54,'view_medicineequipmentusage'),(217,'Can add appointment',55,'add_appointment'),(218,'Can change appointment',55,'change_appointment'),(219,'Can delete appointment',55,'delete_appointment'),(220,'Can view appointment',55,'view_appointment'),(221,'Can add auth token',56,'add_authtoken'),(222,'Can change auth token',56,'change_authtoken'),(223,'Can delete auth token',56,'delete_authtoken'),(224,'Can view auth token',56,'view_authtoken'),(225,'Can add staff',57,'add_staff'),(226,'Can change staff',57,'change_staff'),(227,'Can delete staff',57,'delete_staff'),(228,'Can view staff',57,'view_staff'),(229,'Can add staff attendance',58,'add_staffattendance'),(230,'Can change staff attendance',58,'change_staffattendance'),(231,'Can delete staff attendance',58,'delete_staffattendance'),(232,'Can view staff attendance',58,'view_staffattendance'),(233,'Can add staff leave',59,'add_staffleave'),(234,'Can change staff leave',59,'change_staffleave'),(235,'Can delete staff leave',59,'delete_staffleave'),(236,'Can view staff leave',59,'view_staffleave'),(237,'Can add staff performance',60,'add_staffperformance'),(238,'Can change staff performance',60,'change_staffperformance'),(239,'Can delete staff performance',60,'delete_staffperformance'),(240,'Can view staff performance',60,'view_staffperformance'),(241,'Can add staff shift',61,'add_staffshift'),(242,'Can change staff shift',61,'change_staffshift'),(243,'Can delete staff shift',61,'delete_staffshift'),(244,'Can view staff shift',61,'view_staffshift');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_hos_login_custom_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_hos_login_custom_user_id` FOREIGN KEY (`user_id`) REFERENCES `hos_login_custom_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=62 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (28,'accounts','accountledger'),(27,'accounts','bankaccount'),(26,'accounts','cashbook'),(25,'accounts','paymentvoucher'),(24,'accounts','receiptvoucher'),(1,'admin','logentry'),(55,'appointment','appointment'),(3,'auth','group'),(2,'auth','permission'),(4,'contenttypes','contenttype'),(47,'doctor','doctor'),(14,'hos_login','custom_user'),(13,'hos_login','hospital'),(48,'inventory','equipment'),(49,'inventory','inventoryitem'),(53,'inventory','medicine'),(54,'inventory','medicineequipmentusage'),(52,'inventory','patientequipmentusage'),(51,'inventory','purchaseorder'),(50,'inventory','stocklevelalert'),(29,'ipd','bed'),(46,'ipd','bedallocation'),(45,'ipd','bedavailability'),(44,'ipd','bedbooking'),(43,'ipd','bedstatusupdate'),(42,'ipd','departmentreport'),(41,'ipd','dischargehistory'),(40,'ipd','doctorwisereport'),(39,'ipd','ipdadmitreport'),(30,'ipd','ipddeposit'),(38,'ipd','ipddepositreport'),(31,'ipd','ipddischarge'),(37,'ipd','ipddischargereport'),(36,'ipd','ipdregistration'),(35,'ipd','tpareport'),(32,'ipd','ward'),(34,'ipd','wardwisebedreport'),(33,'ipd','wardwisereport'),(56,'knox','authtoken'),(23,'opd','consultantdoctorreport'),(21,'opd','depwisereport'),(16,'opd','opd_billing'),(18,'opd','opd_prescription'),(15,'opd','opd_register'),(17,'opd','opd_report'),(20,'opd','opdpatientsummary'),(19,'opd','opdtoipdtransfer'),(22,'opd','refdoctorreport'),(6,'patient','patient'),(12,'patient','patientbilling'),(11,'patient','patienthistory'),(10,'patient','patientledger'),(9,'patient','patientreminder'),(8,'patient','patientvisitlist'),(7,'patient','treatmentinformation'),(5,'sessions','session'),(57,'staff','staff'),(58,'staff','staffattendance'),(59,'staff','staffleave'),(60,'staff','staffperformance'),(61,'staff','staffshift');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'accounts','0001_initial','2024-07-08 22:08:17.286592'),(2,'contenttypes','0001_initial','2024-07-08 22:08:17.353011'),(3,'admin','0001_initial','2024-07-08 22:08:17.445887'),(4,'admin','0002_logentry_remove_auto_add','2024-07-08 22:08:17.460345'),(5,'admin','0003_logentry_add_action_flag_choices','2024-07-08 22:08:17.469675'),(6,'contenttypes','0002_remove_content_type_name','2024-07-08 22:08:17.590355'),(7,'auth','0001_initial','2024-07-08 22:08:17.800919'),(8,'auth','0002_alter_permission_name_max_length','2024-07-08 22:08:17.895103'),(9,'auth','0003_alter_user_email_max_length','2024-07-08 22:08:17.903410'),(10,'auth','0004_alter_user_username_opts','2024-07-08 22:08:17.912107'),(11,'auth','0005_alter_user_last_login_null','2024-07-08 22:08:17.919921'),(12,'auth','0006_require_contenttypes_0002','2024-07-08 22:08:17.924587'),(13,'auth','0007_alter_validators_add_error_messages','2024-07-08 22:08:17.932080'),(14,'auth','0008_alter_user_username_max_length','2024-07-08 22:08:17.941027'),(15,'auth','0009_alter_user_last_name_max_length','2024-07-08 22:08:17.951153'),(16,'auth','0010_alter_group_name_max_length','2024-07-08 22:08:17.974218'),(17,'auth','0011_update_proxy_permissions','2024-07-08 22:08:17.990866'),(18,'auth','0012_alter_user_first_name_max_length','2024-07-08 22:08:17.998871'),(19,'doctor','0001_initial','2024-07-08 22:08:18.065242'),(20,'patient','0001_initial','2024-07-08 22:08:18.668863'),(21,'inventory','0001_initial','2024-07-08 22:08:19.222790'),(22,'inventory','0002_alter_inventoryitem_description_and_more','2024-07-08 22:08:19.419643'),(23,'ipd','0001_initial','2024-07-08 22:08:21.475738'),(24,'knox','0001_initial','2024-07-08 22:08:21.580163'),(25,'knox','0002_auto_20150916_1425','2024-07-08 22:08:21.714621'),(26,'knox','0003_auto_20150916_1526','2024-07-08 22:08:21.787232'),(27,'knox','0004_authtoken_expires','2024-07-08 22:08:21.846576'),(28,'knox','0005_authtoken_token_key','2024-07-08 22:08:21.938271'),(29,'knox','0006_auto_20160818_0932','2024-07-08 22:08:22.109716'),(30,'knox','0007_auto_20190111_0542','2024-07-08 22:08:22.173163'),(31,'knox','0008_remove_authtoken_salt','2024-07-08 22:08:22.280161'),(32,'sessions','0001_initial','2024-07-08 22:08:22.352123'),(36,'staff','0001_initial','2024-07-08 22:19:28.360227');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `doctor_doctor`
--

DROP TABLE IF EXISTS `doctor_doctor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `doctor_doctor` (
  `DoctorID` int NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `email` varchar(254) DEFAULT NULL,
  `phone_number` varchar(20) NOT NULL,
  `dob` date NOT NULL,
  `specialty` varchar(100) NOT NULL,
  `Gender` varchar(10) NOT NULL,
  `Address` longtext NOT NULL,
  `PinCode` varchar(10) DEFAULT NULL,
  `experince` varchar(100) NOT NULL,
  `education_qualification` varchar(100) NOT NULL,
  `working_details` varchar(100) NOT NULL,
  `identity_proof` varchar(100) NOT NULL,
  `medical_liscence` varchar(100) NOT NULL,
  `owner_id` bigint NOT NULL,
  PRIMARY KEY (`DoctorID`),
  KEY `doctor_doctor_owner_id_f09f4f4e_fk_hos_login_custom_user_id` (`owner_id`),
  CONSTRAINT `doctor_doctor_owner_id_f09f4f4e_fk_hos_login_custom_user_id` FOREIGN KEY (`owner_id`) REFERENCES `hos_login_custom_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `doctor_doctor`
--

LOCK TABLES `doctor_doctor` WRITE;
/*!40000 ALTER TABLE `doctor_doctor` DISABLE KEYS */;
/*!40000 ALTER TABLE `doctor_doctor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `inventory_equipment`
--

DROP TABLE IF EXISTS `inventory_equipment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `inventory_equipment` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `manufacturer` varchar(100) NOT NULL,
  `quantity` int unsigned NOT NULL,
  `unit_price` decimal(10,2) NOT NULL,
  `purchase_date` date NOT NULL,
  `owner_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `inventory_equipment_owner_id_fa24d640_fk_hos_login` (`owner_id`),
  CONSTRAINT `inventory_equipment_owner_id_fa24d640_fk_hos_login` FOREIGN KEY (`owner_id`) REFERENCES `hos_login_custom_user` (`id`),
  CONSTRAINT `inventory_equipment_chk_1` CHECK ((`quantity` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inventory_equipment`
--

LOCK TABLES `inventory_equipment` WRITE;
/*!40000 ALTER TABLE `inventory_equipment` DISABLE KEYS */;
/*!40000 ALTER TABLE `inventory_equipment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `inventory_inventoryitem`
--

DROP TABLE IF EXISTS `inventory_inventoryitem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `inventory_inventoryitem` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `medicine_manufacturer` varchar(100) NOT NULL,
  `medicine_name` varchar(100) NOT NULL,
  `sale_price` decimal(10,2) NOT NULL,
  `description` longtext NOT NULL,
  `quantity` int unsigned NOT NULL,
  `expiration_date` date NOT NULL,
  `owner_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `inventory_inventoryi_owner_id_1103e280_fk_hos_login` (`owner_id`),
  CONSTRAINT `inventory_inventoryi_owner_id_1103e280_fk_hos_login` FOREIGN KEY (`owner_id`) REFERENCES `hos_login_custom_user` (`id`),
  CONSTRAINT `inventory_inventoryitem_chk_1` CHECK ((`quantity` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inventory_inventoryitem`
--

LOCK TABLES `inventory_inventoryitem` WRITE;
/*!40000 ALTER TABLE `inventory_inventoryitem` DISABLE KEYS */;
/*!40000 ALTER TABLE `inventory_inventoryitem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `inventory_medicine`
--

DROP TABLE IF EXISTS `inventory_medicine`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `inventory_medicine` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `manufacturer` varchar(100) NOT NULL,
  `quantity` int unsigned NOT NULL,
  `unit_price` decimal(10,2) NOT NULL,
  `expiration_date` date NOT NULL,
  `owner_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `inventory_medicine_owner_id_1457f8a2_fk_hos_login_custom_user_id` (`owner_id`),
  CONSTRAINT `inventory_medicine_owner_id_1457f8a2_fk_hos_login_custom_user_id` FOREIGN KEY (`owner_id`) REFERENCES `hos_login_custom_user` (`id`),
  CONSTRAINT `inventory_medicine_chk_1` CHECK ((`quantity` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inventory_medicine`
--

LOCK TABLES `inventory_medicine` WRITE;
/*!40000 ALTER TABLE `inventory_medicine` DISABLE KEYS */;
/*!40000 ALTER TABLE `inventory_medicine` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `inventory_medicineequipmentusage`
--

DROP TABLE IF EXISTS `inventory_medicineequipmentusage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `inventory_medicineequipmentusage` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `quantity_used` int unsigned NOT NULL,
  `usage_date` date NOT NULL,
  `unit_price` decimal(10,2) NOT NULL,
  `medicine_id` bigint NOT NULL,
  `owner_id` bigint NOT NULL,
  `patient_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `inventory_medicineeq_medicine_id_6b34d1fe_fk_inventory` (`medicine_id`),
  KEY `inventory_medicineeq_owner_id_1a0cfaa5_fk_hos_login` (`owner_id`),
  KEY `inventory_medicineeq_patient_id_2e7711bb_fk_patient_p` (`patient_id`),
  CONSTRAINT `inventory_medicineeq_medicine_id_6b34d1fe_fk_inventory` FOREIGN KEY (`medicine_id`) REFERENCES `inventory_medicine` (`id`),
  CONSTRAINT `inventory_medicineeq_owner_id_1a0cfaa5_fk_hos_login` FOREIGN KEY (`owner_id`) REFERENCES `hos_login_custom_user` (`id`),
  CONSTRAINT `inventory_medicineeq_patient_id_2e7711bb_fk_patient_p` FOREIGN KEY (`patient_id`) REFERENCES `patient_patient` (`PatientID`),
  CONSTRAINT `inventory_medicineequipmentusage_chk_1` CHECK ((`quantity_used` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inventory_medicineequipmentusage`
--

LOCK TABLES `inventory_medicineequipmentusage` WRITE;
/*!40000 ALTER TABLE `inventory_medicineequipmentusage` DISABLE KEYS */;
/*!40000 ALTER TABLE `inventory_medicineequipmentusage` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `inventory_patientequipmentusage`
--

DROP TABLE IF EXISTS `inventory_patientequipmentusage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `inventory_patientequipmentusage` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `quantity_used` int unsigned NOT NULL,
  `usage_date` date NOT NULL,
  `unit_price` decimal(10,2) NOT NULL,
  `equipment_id` bigint NOT NULL,
  `owner_id` bigint NOT NULL,
  `patient_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `inventory_patientequ_equipment_id_3877ac82_fk_inventory` (`equipment_id`),
  KEY `inventory_patientequ_owner_id_dfb8d411_fk_hos_login` (`owner_id`),
  KEY `inventory_patientequ_patient_id_f66a29cd_fk_patient_p` (`patient_id`),
  CONSTRAINT `inventory_patientequ_equipment_id_3877ac82_fk_inventory` FOREIGN KEY (`equipment_id`) REFERENCES `inventory_equipment` (`id`),
  CONSTRAINT `inventory_patientequ_owner_id_dfb8d411_fk_hos_login` FOREIGN KEY (`owner_id`) REFERENCES `hos_login_custom_user` (`id`),
  CONSTRAINT `inventory_patientequ_patient_id_f66a29cd_fk_patient_p` FOREIGN KEY (`patient_id`) REFERENCES `patient_patient` (`PatientID`),
  CONSTRAINT `inventory_patientequipmentusage_chk_1` CHECK ((`quantity_used` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inventory_patientequipmentusage`
--

LOCK TABLES `inventory_patientequipmentusage` WRITE;
/*!40000 ALTER TABLE `inventory_patientequipmentusage` DISABLE KEYS */;
/*!40000 ALTER TABLE `inventory_patientequipmentusage` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `inventory_purchaseorder`
--

DROP TABLE IF EXISTS `inventory_purchaseorder`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `inventory_purchaseorder` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `quantity_to_order` int unsigned NOT NULL,
  `order_date` date NOT NULL,
  `inventory_item_id` bigint NOT NULL,
  `owner_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `inventory_purchaseor_inventory_item_id_6ad4bf03_fk_inventory` (`inventory_item_id`),
  KEY `inventory_purchaseor_owner_id_4ac13c17_fk_hos_login` (`owner_id`),
  CONSTRAINT `inventory_purchaseor_inventory_item_id_6ad4bf03_fk_inventory` FOREIGN KEY (`inventory_item_id`) REFERENCES `inventory_inventoryitem` (`id`),
  CONSTRAINT `inventory_purchaseor_owner_id_4ac13c17_fk_hos_login` FOREIGN KEY (`owner_id`) REFERENCES `hos_login_custom_user` (`id`),
  CONSTRAINT `inventory_purchaseorder_chk_1` CHECK ((`quantity_to_order` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inventory_purchaseorder`
--

LOCK TABLES `inventory_purchaseorder` WRITE;
/*!40000 ALTER TABLE `inventory_purchaseorder` DISABLE KEYS */;
/*!40000 ALTER TABLE `inventory_purchaseorder` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `inventory_stocklevelalert`
--

DROP TABLE IF EXISTS `inventory_stocklevelalert`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `inventory_stocklevelalert` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `threshold_quantity` int unsigned NOT NULL,
  `inventory_item_id` bigint NOT NULL,
  `owner_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `inventory_stocklevel_inventory_item_id_cbf16a9a_fk_inventory` (`inventory_item_id`),
  KEY `inventory_stocklevel_owner_id_3e819f7c_fk_hos_login` (`owner_id`),
  CONSTRAINT `inventory_stocklevel_inventory_item_id_cbf16a9a_fk_inventory` FOREIGN KEY (`inventory_item_id`) REFERENCES `inventory_inventoryitem` (`id`),
  CONSTRAINT `inventory_stocklevel_owner_id_3e819f7c_fk_hos_login` FOREIGN KEY (`owner_id`) REFERENCES `hos_login_custom_user` (`id`),
  CONSTRAINT `inventory_stocklevelalert_chk_1` CHECK ((`threshold_quantity` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inventory_stocklevelalert`
--

LOCK TABLES `inventory_stocklevelalert` WRITE;
/*!40000 ALTER TABLE `inventory_stocklevelalert` DISABLE KEYS */;
/*!40000 ALTER TABLE `inventory_stocklevelalert` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ipd_bed`
--

DROP TABLE IF EXISTS `ipd_bed`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ipd_bed` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `number` varchar(20) NOT NULL,
  `is_available` tinyint(1) NOT NULL,
  `owner_id` bigint NOT NULL,
  `ward_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ipd_bed_ward_id_69621b27_fk_ipd_ward_id` (`ward_id`),
  KEY `ipd_bed_owner_id_14c765c8_fk_hos_login_custom_user_id` (`owner_id`),
  CONSTRAINT `ipd_bed_owner_id_14c765c8_fk_hos_login_custom_user_id` FOREIGN KEY (`owner_id`) REFERENCES `hos_login_custom_user` (`id`),
  CONSTRAINT `ipd_bed_ward_id_69621b27_fk_ipd_ward_id` FOREIGN KEY (`ward_id`) REFERENCES `ipd_ward` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ipd_bed`
--

LOCK TABLES `ipd_bed` WRITE;
/*!40000 ALTER TABLE `ipd_bed` DISABLE KEYS */;
/*!40000 ALTER TABLE `ipd_bed` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ipd_bedallocation`
--

DROP TABLE IF EXISTS `ipd_bedallocation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ipd_bedallocation` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `admission_id` int NOT NULL,
  `bed_id` bigint NOT NULL,
  `owner_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ipd_bedallocation_admission_id_a5bf6b99_fk_ipd_ipdre` (`admission_id`),
  KEY `ipd_bedallocation_bed_id_5dfcd042_fk_ipd_bed_id` (`bed_id`),
  KEY `ipd_bedallocation_owner_id_c4bb4ca7_fk_hos_login_custom_user_id` (`owner_id`),
  CONSTRAINT `ipd_bedallocation_admission_id_a5bf6b99_fk_ipd_ipdre` FOREIGN KEY (`admission_id`) REFERENCES `ipd_ipdregistration` (`admission_id`),
  CONSTRAINT `ipd_bedallocation_bed_id_5dfcd042_fk_ipd_bed_id` FOREIGN KEY (`bed_id`) REFERENCES `ipd_bed` (`id`),
  CONSTRAINT `ipd_bedallocation_owner_id_c4bb4ca7_fk_hos_login_custom_user_id` FOREIGN KEY (`owner_id`) REFERENCES `hos_login_custom_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ipd_bedallocation`
--

LOCK TABLES `ipd_bedallocation` WRITE;
/*!40000 ALTER TABLE `ipd_bedallocation` DISABLE KEYS */;
/*!40000 ALTER TABLE `ipd_bedallocation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ipd_bedavailability`
--

DROP TABLE IF EXISTS `ipd_bedavailability`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ipd_bedavailability` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `available` tinyint(1) NOT NULL,
  `last_updated` datetime(6) NOT NULL,
  `bed_id` bigint NOT NULL,
  `owner_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `bed_id` (`bed_id`),
  KEY `ipd_bedavailability_owner_id_a312022c_fk_hos_login` (`owner_id`),
  CONSTRAINT `ipd_bedavailability_bed_id_844222fc_fk_ipd_bed_id` FOREIGN KEY (`bed_id`) REFERENCES `ipd_bed` (`id`),
  CONSTRAINT `ipd_bedavailability_owner_id_a312022c_fk_hos_login` FOREIGN KEY (`owner_id`) REFERENCES `hos_login_custom_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ipd_bedavailability`
--

LOCK TABLES `ipd_bedavailability` WRITE;
/*!40000 ALTER TABLE `ipd_bedavailability` DISABLE KEYS */;
/*!40000 ALTER TABLE `ipd_bedavailability` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ipd_bedbooking`
--

DROP TABLE IF EXISTS `ipd_bedbooking`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ipd_bedbooking` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `booking_date` date NOT NULL,
  `bed_id` bigint NOT NULL,
  `owner_id` bigint NOT NULL,
  `patient_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ipd_bedbooking_bed_id_92694848_fk_ipd_bed_id` (`bed_id`),
  KEY `ipd_bedbooking_owner_id_79e81b28_fk_hos_login_custom_user_id` (`owner_id`),
  KEY `ipd_bedbooking_patient_id_01e38206_fk_patient_patient_PatientID` (`patient_id`),
  CONSTRAINT `ipd_bedbooking_bed_id_92694848_fk_ipd_bed_id` FOREIGN KEY (`bed_id`) REFERENCES `ipd_bed` (`id`),
  CONSTRAINT `ipd_bedbooking_owner_id_79e81b28_fk_hos_login_custom_user_id` FOREIGN KEY (`owner_id`) REFERENCES `hos_login_custom_user` (`id`),
  CONSTRAINT `ipd_bedbooking_patient_id_01e38206_fk_patient_patient_PatientID` FOREIGN KEY (`patient_id`) REFERENCES `patient_patient` (`PatientID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ipd_bedbooking`
--

LOCK TABLES `ipd_bedbooking` WRITE;
/*!40000 ALTER TABLE `ipd_bedbooking` DISABLE KEYS */;
/*!40000 ALTER TABLE `ipd_bedbooking` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ipd_bedstatusupdate`
--

DROP TABLE IF EXISTS `ipd_bedstatusupdate`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ipd_bedstatusupdate` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `updated_status` tinyint(1) NOT NULL,
  `update_date` date NOT NULL,
  `bed_id` bigint NOT NULL,
  `owner_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ipd_bedstatusupdate_bed_id_d5e639c3_fk_ipd_bed_id` (`bed_id`),
  KEY `ipd_bedstatusupdate_owner_id_2ce2f81f_fk_hos_login` (`owner_id`),
  CONSTRAINT `ipd_bedstatusupdate_bed_id_d5e639c3_fk_ipd_bed_id` FOREIGN KEY (`bed_id`) REFERENCES `ipd_bed` (`id`),
  CONSTRAINT `ipd_bedstatusupdate_owner_id_2ce2f81f_fk_hos_login` FOREIGN KEY (`owner_id`) REFERENCES `hos_login_custom_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ipd_bedstatusupdate`
--

LOCK TABLES `ipd_bedstatusupdate` WRITE;
/*!40000 ALTER TABLE `ipd_bedstatusupdate` DISABLE KEYS */;
/*!40000 ALTER TABLE `ipd_bedstatusupdate` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ipd_departmentreport`
--

DROP TABLE IF EXISTS `ipd_departmentreport`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ipd_departmentreport` (
  `report_id` int NOT NULL AUTO_INCREMENT,
  `department` varchar(50) NOT NULL,
  `data_details` longtext NOT NULL,
  `owner_id` bigint NOT NULL,
  PRIMARY KEY (`report_id`),
  KEY `ipd_departmentreport_owner_id_6c3d37cb_fk_hos_login` (`owner_id`),
  CONSTRAINT `ipd_departmentreport_owner_id_6c3d37cb_fk_hos_login` FOREIGN KEY (`owner_id`) REFERENCES `hos_login_custom_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ipd_departmentreport`
--

LOCK TABLES `ipd_departmentreport` WRITE;
/*!40000 ALTER TABLE `ipd_departmentreport` DISABLE KEYS */;
/*!40000 ALTER TABLE `ipd_departmentreport` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ipd_dischargehistory`
--

DROP TABLE IF EXISTS `ipd_dischargehistory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ipd_dischargehistory` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `admission_date` date NOT NULL,
  `discharge_date` date DEFAULT NULL,
  `owner_id` bigint DEFAULT NULL,
  `patient_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ipd_dischargehistory_owner_id_402186b9_fk_hos_login` (`owner_id`),
  KEY `ipd_dischargehistory_patient_id_2a41b687_fk_patient_p` (`patient_id`),
  CONSTRAINT `ipd_dischargehistory_owner_id_402186b9_fk_hos_login` FOREIGN KEY (`owner_id`) REFERENCES `hos_login_custom_user` (`id`),
  CONSTRAINT `ipd_dischargehistory_patient_id_2a41b687_fk_patient_p` FOREIGN KEY (`patient_id`) REFERENCES `patient_patient` (`PatientID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ipd_dischargehistory`
--

LOCK TABLES `ipd_dischargehistory` WRITE;
/*!40000 ALTER TABLE `ipd_dischargehistory` DISABLE KEYS */;
/*!40000 ALTER TABLE `ipd_dischargehistory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ipd_doctorwisereport`
--

DROP TABLE IF EXISTS `ipd_doctorwisereport`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ipd_doctorwisereport` (
  `report_id` int NOT NULL AUTO_INCREMENT,
  `doctor_id` varchar(20) NOT NULL,
  `data_details` longtext NOT NULL,
  `owner_id` bigint NOT NULL,
  PRIMARY KEY (`report_id`),
  KEY `ipd_doctorwisereport_owner_id_679b6548_fk_hos_login` (`owner_id`),
  CONSTRAINT `ipd_doctorwisereport_owner_id_679b6548_fk_hos_login` FOREIGN KEY (`owner_id`) REFERENCES `hos_login_custom_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ipd_doctorwisereport`
--

LOCK TABLES `ipd_doctorwisereport` WRITE;
/*!40000 ALTER TABLE `ipd_doctorwisereport` DISABLE KEYS */;
/*!40000 ALTER TABLE `ipd_doctorwisereport` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ipd_ipdadmitreport`
--

DROP TABLE IF EXISTS `ipd_ipdadmitreport`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ipd_ipdadmitreport` (
  `report_id` int NOT NULL AUTO_INCREMENT,
  `report_details` longtext NOT NULL,
  `admission_id` int NOT NULL,
  `owner_id` bigint NOT NULL,
  PRIMARY KEY (`report_id`),
  KEY `ipd_ipdadmitreport_admission_id_711dd85c_fk_ipd_ipdre` (`admission_id`),
  KEY `ipd_ipdadmitreport_owner_id_2c84f91b_fk_hos_login_custom_user_id` (`owner_id`),
  CONSTRAINT `ipd_ipdadmitreport_admission_id_711dd85c_fk_ipd_ipdre` FOREIGN KEY (`admission_id`) REFERENCES `ipd_ipdregistration` (`admission_id`),
  CONSTRAINT `ipd_ipdadmitreport_owner_id_2c84f91b_fk_hos_login_custom_user_id` FOREIGN KEY (`owner_id`) REFERENCES `hos_login_custom_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ipd_ipdadmitreport`
--

LOCK TABLES `ipd_ipdadmitreport` WRITE;
/*!40000 ALTER TABLE `ipd_ipdadmitreport` DISABLE KEYS */;
/*!40000 ALTER TABLE `ipd_ipdadmitreport` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ipd_ipddeposit`
--

DROP TABLE IF EXISTS `ipd_ipddeposit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ipd_ipddeposit` (
  `deposit_id` int NOT NULL AUTO_INCREMENT,
  `deposit_amount` decimal(10,2) NOT NULL,
  `deposit_date` date NOT NULL,
  `admission_id` int NOT NULL,
  `owner_id` bigint NOT NULL,
  PRIMARY KEY (`deposit_id`),
  KEY `ipd_ipddeposit_admission_id_82096a0a_fk_ipd_ipdre` (`admission_id`),
  KEY `ipd_ipddeposit_owner_id_0108a0c9_fk_hos_login_custom_user_id` (`owner_id`),
  CONSTRAINT `ipd_ipddeposit_admission_id_82096a0a_fk_ipd_ipdre` FOREIGN KEY (`admission_id`) REFERENCES `ipd_ipdregistration` (`admission_id`),
  CONSTRAINT `ipd_ipddeposit_owner_id_0108a0c9_fk_hos_login_custom_user_id` FOREIGN KEY (`owner_id`) REFERENCES `hos_login_custom_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ipd_ipddeposit`
--

LOCK TABLES `ipd_ipddeposit` WRITE;
/*!40000 ALTER TABLE `ipd_ipddeposit` DISABLE KEYS */;
/*!40000 ALTER TABLE `ipd_ipddeposit` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ipd_ipddepositreport`
--

DROP TABLE IF EXISTS `ipd_ipddepositreport`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ipd_ipddepositreport` (
  `report_id` int NOT NULL AUTO_INCREMENT,
  `report_details` longtext NOT NULL,
  `deposit_id` int NOT NULL,
  `owner_id` bigint NOT NULL,
  PRIMARY KEY (`report_id`),
  KEY `ipd_ipddepositreport_deposit_id_b9370c26_fk_ipd_ipdde` (`deposit_id`),
  KEY `ipd_ipddepositreport_owner_id_64e02513_fk_hos_login` (`owner_id`),
  CONSTRAINT `ipd_ipddepositreport_deposit_id_b9370c26_fk_ipd_ipdde` FOREIGN KEY (`deposit_id`) REFERENCES `ipd_ipddeposit` (`deposit_id`),
  CONSTRAINT `ipd_ipddepositreport_owner_id_64e02513_fk_hos_login` FOREIGN KEY (`owner_id`) REFERENCES `hos_login_custom_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ipd_ipddepositreport`
--

LOCK TABLES `ipd_ipddepositreport` WRITE;
/*!40000 ALTER TABLE `ipd_ipddepositreport` DISABLE KEYS */;
/*!40000 ALTER TABLE `ipd_ipddepositreport` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ipd_ipddischarge`
--

DROP TABLE IF EXISTS `ipd_ipddischarge`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ipd_ipddischarge` (
  `discharge_id` int NOT NULL AUTO_INCREMENT,
  `discharge_date` date DEFAULT NULL,
  `admission_date` date NOT NULL,
  `discharge_summary` longtext NOT NULL,
  `admission_id` int NOT NULL,
  `owner_id` bigint DEFAULT NULL,
  PRIMARY KEY (`discharge_id`),
  UNIQUE KEY `admission_id` (`admission_id`),
  KEY `ipd_ipddischarge_owner_id_05779414_fk_hos_login_custom_user_id` (`owner_id`),
  CONSTRAINT `ipd_ipddischarge_admission_id_4e5070f3_fk_ipd_ipdre` FOREIGN KEY (`admission_id`) REFERENCES `ipd_ipdregistration` (`admission_id`),
  CONSTRAINT `ipd_ipddischarge_owner_id_05779414_fk_hos_login_custom_user_id` FOREIGN KEY (`owner_id`) REFERENCES `hos_login_custom_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ipd_ipddischarge`
--

LOCK TABLES `ipd_ipddischarge` WRITE;
/*!40000 ALTER TABLE `ipd_ipddischarge` DISABLE KEYS */;
/*!40000 ALTER TABLE `ipd_ipddischarge` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ipd_ipddischargereport`
--

DROP TABLE IF EXISTS `ipd_ipddischargereport`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ipd_ipddischargereport` (
  `report_id` int NOT NULL AUTO_INCREMENT,
  `report_details` longtext NOT NULL,
  `discharge_id` int NOT NULL,
  `owner_id` bigint NOT NULL,
  PRIMARY KEY (`report_id`),
  KEY `ipd_ipddischargerepo_discharge_id_3f5e4f59_fk_ipd_ipddi` (`discharge_id`),
  KEY `ipd_ipddischargerepo_owner_id_c22efdb9_fk_hos_login` (`owner_id`),
  CONSTRAINT `ipd_ipddischargerepo_discharge_id_3f5e4f59_fk_ipd_ipddi` FOREIGN KEY (`discharge_id`) REFERENCES `ipd_ipddischarge` (`discharge_id`),
  CONSTRAINT `ipd_ipddischargerepo_owner_id_c22efdb9_fk_hos_login` FOREIGN KEY (`owner_id`) REFERENCES `hos_login_custom_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ipd_ipddischargereport`
--

LOCK TABLES `ipd_ipddischargereport` WRITE;
/*!40000 ALTER TABLE `ipd_ipddischargereport` DISABLE KEYS */;
/*!40000 ALTER TABLE `ipd_ipddischargereport` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ipd_ipdregistration`
--

DROP TABLE IF EXISTS `ipd_ipdregistration`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ipd_ipdregistration` (
  `admission_id` int NOT NULL AUTO_INCREMENT,
  `admission_date` date NOT NULL,
  `discharge_date` date DEFAULT NULL,
  `is_discharged` tinyint(1) NOT NULL,
  `bed_id` bigint NOT NULL,
  `owner_id` bigint NOT NULL,
  `patient_id` int NOT NULL,
  `ward_id` bigint NOT NULL,
  PRIMARY KEY (`admission_id`),
  UNIQUE KEY `bed_id` (`bed_id`),
  KEY `ipd_ipdregistration_owner_id_e8a8d23d_fk_hos_login` (`owner_id`),
  KEY `ipd_ipdregistration_patient_id_c6bcc2e0_fk_patient_p` (`patient_id`),
  KEY `ipd_ipdregistration_ward_id_8941f525_fk_ipd_ward_id` (`ward_id`),
  CONSTRAINT `ipd_ipdregistration_bed_id_7f1cb0f9_fk_ipd_bed_id` FOREIGN KEY (`bed_id`) REFERENCES `ipd_bed` (`id`),
  CONSTRAINT `ipd_ipdregistration_owner_id_e8a8d23d_fk_hos_login` FOREIGN KEY (`owner_id`) REFERENCES `hos_login_custom_user` (`id`),
  CONSTRAINT `ipd_ipdregistration_patient_id_c6bcc2e0_fk_patient_p` FOREIGN KEY (`patient_id`) REFERENCES `patient_patient` (`PatientID`),
  CONSTRAINT `ipd_ipdregistration_ward_id_8941f525_fk_ipd_ward_id` FOREIGN KEY (`ward_id`) REFERENCES `ipd_ward` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ipd_ipdregistration`
--

LOCK TABLES `ipd_ipdregistration` WRITE;
/*!40000 ALTER TABLE `ipd_ipdregistration` DISABLE KEYS */;
/*!40000 ALTER TABLE `ipd_ipdregistration` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ipd_tpareport`
--

DROP TABLE IF EXISTS `ipd_tpareport`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ipd_tpareport` (
  `report_id` int NOT NULL AUTO_INCREMENT,
  `tpa_id` varchar(20) NOT NULL,
  `transaction_details` longtext NOT NULL,
  `owner_id` bigint NOT NULL,
  PRIMARY KEY (`report_id`),
  KEY `ipd_tpareport_owner_id_b15ba0cb_fk_hos_login_custom_user_id` (`owner_id`),
  CONSTRAINT `ipd_tpareport_owner_id_b15ba0cb_fk_hos_login_custom_user_id` FOREIGN KEY (`owner_id`) REFERENCES `hos_login_custom_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ipd_tpareport`
--

LOCK TABLES `ipd_tpareport` WRITE;
/*!40000 ALTER TABLE `ipd_tpareport` DISABLE KEYS */;
/*!40000 ALTER TABLE `ipd_tpareport` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ipd_ward`
--

DROP TABLE IF EXISTS `ipd_ward`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ipd_ward` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `daily_charge` int unsigned NOT NULL,
  `total_beds` int unsigned NOT NULL,
  `owner_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ipd_ward_owner_id_b89fac26_fk_hos_login_custom_user_id` (`owner_id`),
  CONSTRAINT `ipd_ward_owner_id_b89fac26_fk_hos_login_custom_user_id` FOREIGN KEY (`owner_id`) REFERENCES `hos_login_custom_user` (`id`),
  CONSTRAINT `ipd_ward_chk_1` CHECK ((`daily_charge` >= 0)),
  CONSTRAINT `ipd_ward_chk_2` CHECK ((`total_beds` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ipd_ward`
--

LOCK TABLES `ipd_ward` WRITE;
/*!40000 ALTER TABLE `ipd_ward` DISABLE KEYS */;
/*!40000 ALTER TABLE `ipd_ward` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ipd_wardwisebedreport`
--

DROP TABLE IF EXISTS `ipd_wardwisebedreport`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ipd_wardwisebedreport` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `occupied_beds` int NOT NULL,
  `available_beds` int NOT NULL,
  `report_date` date NOT NULL,
  `owner_id` bigint NOT NULL,
  `ward_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ipd_wardwisebedrepor_owner_id_8184eaed_fk_hos_login` (`owner_id`),
  KEY `ipd_wardwisebedreport_ward_id_a277d524_fk_ipd_ward_id` (`ward_id`),
  CONSTRAINT `ipd_wardwisebedrepor_owner_id_8184eaed_fk_hos_login` FOREIGN KEY (`owner_id`) REFERENCES `hos_login_custom_user` (`id`),
  CONSTRAINT `ipd_wardwisebedreport_ward_id_a277d524_fk_ipd_ward_id` FOREIGN KEY (`ward_id`) REFERENCES `ipd_ward` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ipd_wardwisebedreport`
--

LOCK TABLES `ipd_wardwisebedreport` WRITE;
/*!40000 ALTER TABLE `ipd_wardwisebedreport` DISABLE KEYS */;
/*!40000 ALTER TABLE `ipd_wardwisebedreport` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ipd_wardwisereport`
--

DROP TABLE IF EXISTS `ipd_wardwisereport`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ipd_wardwisereport` (
  `report_id` int NOT NULL AUTO_INCREMENT,
  `ward` varchar(50) NOT NULL,
  `data_details` longtext NOT NULL,
  `owner_id` bigint NOT NULL,
  PRIMARY KEY (`report_id`),
  KEY `ipd_wardwisereport_owner_id_9ea1e933_fk_hos_login_custom_user_id` (`owner_id`),
  CONSTRAINT `ipd_wardwisereport_owner_id_9ea1e933_fk_hos_login_custom_user_id` FOREIGN KEY (`owner_id`) REFERENCES `hos_login_custom_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ipd_wardwisereport`
--

LOCK TABLES `ipd_wardwisereport` WRITE;
/*!40000 ALTER TABLE `ipd_wardwisereport` DISABLE KEYS */;
/*!40000 ALTER TABLE `ipd_wardwisereport` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `knox_authtoken`
--

DROP TABLE IF EXISTS `knox_authtoken`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `knox_authtoken` (
  `digest` varchar(128) NOT NULL,
  `created` datetime(6) NOT NULL,
  `user_id` bigint NOT NULL,
  `expiry` datetime(6) DEFAULT NULL,
  `token_key` varchar(8) NOT NULL,
  PRIMARY KEY (`digest`),
  KEY `knox_authtoken_user_id_e5a5d899_fk_hos_login_custom_user_id` (`user_id`),
  KEY `knox_authtoken_token_key_8f4f7d47` (`token_key`),
  CONSTRAINT `knox_authtoken_user_id_e5a5d899_fk_hos_login_custom_user_id` FOREIGN KEY (`user_id`) REFERENCES `hos_login_custom_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `knox_authtoken`
--

LOCK TABLES `knox_authtoken` WRITE;
/*!40000 ALTER TABLE `knox_authtoken` DISABLE KEYS */;
/*!40000 ALTER TABLE `knox_authtoken` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `patient_patient`
--

DROP TABLE IF EXISTS `patient_patient`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `patient_patient` (
  `PatientID` int NOT NULL AUTO_INCREMENT,
  `FirstName` varchar(255) NOT NULL,
  `phone` varchar(20) NOT NULL,
  `email` varchar(254) NOT NULL,
  `Relationship` varchar(100) NOT NULL,
  `fullname` varchar(255) NOT NULL,
  `blood` varchar(10) NOT NULL,
  `city` varchar(100) NOT NULL,
  `phone_no` varchar(20) NOT NULL,
  `referred` varchar(255) NOT NULL,
  `allergy` longtext NOT NULL,
  `initial_balance` decimal(10,2) NOT NULL,
  `facility_code` varchar(100) NOT NULL,
  `membernum` varchar(100) NOT NULL,
  `Insurance_name` varchar(100) NOT NULL,
  `card_num` varchar(100) NOT NULL,
  `Insurance_Provider` varchar(100) NOT NULL,
  `Gender` varchar(10) NOT NULL,
  `DOB` date NOT NULL,
  `Register_Date` date NOT NULL,
  `PinCode` varchar(10) DEFAULT NULL,
  `owner_id` bigint NOT NULL,
  PRIMARY KEY (`PatientID`),
  KEY `patient_patient_owner_id_6fca25a8_fk_hos_login_custom_user_id` (`owner_id`),
  CONSTRAINT `patient_patient_owner_id_6fca25a8_fk_hos_login_custom_user_id` FOREIGN KEY (`owner_id`) REFERENCES `hos_login_custom_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `patient_patient`
--

LOCK TABLES `patient_patient` WRITE;
/*!40000 ALTER TABLE `patient_patient` DISABLE KEYS */;
/*!40000 ALTER TABLE `patient_patient` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `patient_patientbilling`
--

DROP TABLE IF EXISTS `patient_patientbilling`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `patient_patientbilling` (
  `BillingID` int NOT NULL AUTO_INCREMENT,
  `InvoiceDetails` longtext NOT NULL,
  `PatientID_id` int NOT NULL,
  `owner_id` bigint NOT NULL,
  PRIMARY KEY (`BillingID`),
  KEY `patient_patientbilli_PatientID_id_91c906ff_fk_patient_p` (`PatientID_id`),
  KEY `patient_patientbilli_owner_id_82ab086f_fk_hos_login` (`owner_id`),
  CONSTRAINT `patient_patientbilli_owner_id_82ab086f_fk_hos_login` FOREIGN KEY (`owner_id`) REFERENCES `hos_login_custom_user` (`id`),
  CONSTRAINT `patient_patientbilli_PatientID_id_91c906ff_fk_patient_p` FOREIGN KEY (`PatientID_id`) REFERENCES `patient_patient` (`PatientID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `patient_patientbilling`
--

LOCK TABLES `patient_patientbilling` WRITE;
/*!40000 ALTER TABLE `patient_patientbilling` DISABLE KEYS */;
/*!40000 ALTER TABLE `patient_patientbilling` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `patient_patienthistory`
--

DROP TABLE IF EXISTS `patient_patienthistory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `patient_patienthistory` (
  `HistoryID` int NOT NULL AUTO_INCREMENT,
  `MedicalHistoryDetails` longtext NOT NULL,
  `TreatmentDetails` longtext NOT NULL,
  `PatientID_id` int NOT NULL,
  `owner_id` bigint NOT NULL,
  PRIMARY KEY (`HistoryID`),
  KEY `patient_patienthisto_PatientID_id_9db13f8e_fk_patient_p` (`PatientID_id`),
  KEY `patient_patienthisto_owner_id_0d0eda39_fk_hos_login` (`owner_id`),
  CONSTRAINT `patient_patienthisto_owner_id_0d0eda39_fk_hos_login` FOREIGN KEY (`owner_id`) REFERENCES `hos_login_custom_user` (`id`),
  CONSTRAINT `patient_patienthisto_PatientID_id_9db13f8e_fk_patient_p` FOREIGN KEY (`PatientID_id`) REFERENCES `patient_patient` (`PatientID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `patient_patienthistory`
--

LOCK TABLES `patient_patienthistory` WRITE;
/*!40000 ALTER TABLE `patient_patienthistory` DISABLE KEYS */;
/*!40000 ALTER TABLE `patient_patienthistory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `patient_patientledger`
--

DROP TABLE IF EXISTS `patient_patientledger`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `patient_patientledger` (
  `LedgerID` int NOT NULL AUTO_INCREMENT,
  `TransactionDetails` longtext NOT NULL,
  `PatientID_id` int NOT NULL,
  `owner_id` bigint NOT NULL,
  PRIMARY KEY (`LedgerID`),
  KEY `patient_patientledge_PatientID_id_5de5017f_fk_patient_p` (`PatientID_id`),
  KEY `patient_patientledge_owner_id_1cf3dfda_fk_hos_login` (`owner_id`),
  CONSTRAINT `patient_patientledge_owner_id_1cf3dfda_fk_hos_login` FOREIGN KEY (`owner_id`) REFERENCES `hos_login_custom_user` (`id`),
  CONSTRAINT `patient_patientledge_PatientID_id_5de5017f_fk_patient_p` FOREIGN KEY (`PatientID_id`) REFERENCES `patient_patient` (`PatientID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `patient_patientledger`
--

LOCK TABLES `patient_patientledger` WRITE;
/*!40000 ALTER TABLE `patient_patientledger` DISABLE KEYS */;
/*!40000 ALTER TABLE `patient_patientledger` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `patient_patientreminder`
--

DROP TABLE IF EXISTS `patient_patientreminder`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `patient_patientreminder` (
  `ReminderID` int NOT NULL AUTO_INCREMENT,
  `ReminderDetails` longtext NOT NULL,
  `PatientID_id` int NOT NULL,
  `owner_id` bigint NOT NULL,
  PRIMARY KEY (`ReminderID`),
  KEY `patient_patientremin_PatientID_id_e0c650ff_fk_patient_p` (`PatientID_id`),
  KEY `patient_patientremin_owner_id_927c7413_fk_hos_login` (`owner_id`),
  CONSTRAINT `patient_patientremin_owner_id_927c7413_fk_hos_login` FOREIGN KEY (`owner_id`) REFERENCES `hos_login_custom_user` (`id`),
  CONSTRAINT `patient_patientremin_PatientID_id_e0c650ff_fk_patient_p` FOREIGN KEY (`PatientID_id`) REFERENCES `patient_patient` (`PatientID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `patient_patientreminder`
--

LOCK TABLES `patient_patientreminder` WRITE;
/*!40000 ALTER TABLE `patient_patientreminder` DISABLE KEYS */;
/*!40000 ALTER TABLE `patient_patientreminder` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `patient_patientvisitlist`
--

DROP TABLE IF EXISTS `patient_patientvisitlist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `patient_patientvisitlist` (
  `VisitID` int NOT NULL AUTO_INCREMENT,
  `VisitDate` date NOT NULL,
  `Reason` longtext NOT NULL,
  `PatientID_id` int NOT NULL,
  `owner_id` bigint NOT NULL,
  PRIMARY KEY (`VisitID`),
  KEY `patient_patientvisit_PatientID_id_942e2ab3_fk_patient_p` (`PatientID_id`),
  KEY `patient_patientvisit_owner_id_d061a8ce_fk_hos_login` (`owner_id`),
  CONSTRAINT `patient_patientvisit_owner_id_d061a8ce_fk_hos_login` FOREIGN KEY (`owner_id`) REFERENCES `hos_login_custom_user` (`id`),
  CONSTRAINT `patient_patientvisit_PatientID_id_942e2ab3_fk_patient_p` FOREIGN KEY (`PatientID_id`) REFERENCES `patient_patient` (`PatientID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `patient_patientvisitlist`
--

LOCK TABLES `patient_patientvisitlist` WRITE;
/*!40000 ALTER TABLE `patient_patientvisitlist` DISABLE KEYS */;
/*!40000 ALTER TABLE `patient_patientvisitlist` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `patient_treatmentinformation`
--

DROP TABLE IF EXISTS `patient_treatmentinformation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `patient_treatmentinformation` (
  `TreatmentID` int NOT NULL AUTO_INCREMENT,
  `TreatmentDetails` longtext NOT NULL,
  `PatientID_id` int NOT NULL,
  `owner_id` bigint NOT NULL,
  PRIMARY KEY (`TreatmentID`),
  KEY `patient_treatmentinf_PatientID_id_9ef77375_fk_patient_p` (`PatientID_id`),
  KEY `patient_treatmentinf_owner_id_73065d75_fk_hos_login` (`owner_id`),
  CONSTRAINT `patient_treatmentinf_owner_id_73065d75_fk_hos_login` FOREIGN KEY (`owner_id`) REFERENCES `hos_login_custom_user` (`id`),
  CONSTRAINT `patient_treatmentinf_PatientID_id_9ef77375_fk_patient_p` FOREIGN KEY (`PatientID_id`) REFERENCES `patient_patient` (`PatientID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `patient_treatmentinformation`
--

LOCK TABLES `patient_treatmentinformation` WRITE;
/*!40000 ALTER TABLE `patient_treatmentinformation` DISABLE KEYS */;
/*!40000 ALTER TABLE `patient_treatmentinformation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `staff_staff`
--

DROP TABLE IF EXISTS `staff_staff`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `staff_staff` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `address` varchar(255) NOT NULL,
  `email` varchar(100) NOT NULL,
  `dob` date DEFAULT NULL,
  `hire_datee` date DEFAULT NULL,
  `department` varchar(100) NOT NULL,
  `phone_number` varchar(15) DEFAULT NULL,
  `owner_id` bigint NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `staff_staff`
--

LOCK TABLES `staff_staff` WRITE;
/*!40000 ALTER TABLE `staff_staff` DISABLE KEYS */;
/*!40000 ALTER TABLE `staff_staff` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `staff_staffleave`
--

DROP TABLE IF EXISTS `staff_staffleave`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `staff_staffleave` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `leave_start` date NOT NULL,
  `leave_end` date NOT NULL,
  `reason` longtext NOT NULL,
  `is_approved` tinyint(1) NOT NULL,
  `Staff_id` bigint NOT NULL,
  `owner_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `staff_staffleave_Staff_id_379aebe0_fk_staff_staff_id` (`Staff_id`),
  KEY `staff_staffleave_owner_id_f7a35503_fk_hos_login_custom_user_id` (`owner_id`),
  CONSTRAINT `staff_staffleave_owner_id_f7a35503_fk_hos_login_custom_user_id` FOREIGN KEY (`owner_id`) REFERENCES `hos_login_custom_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `staff_staffleave`
--

LOCK TABLES `staff_staffleave` WRITE;
/*!40000 ALTER TABLE `staff_staffleave` DISABLE KEYS */;
/*!40000 ALTER TABLE `staff_staffleave` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `staff_staffperformance`
--

DROP TABLE IF EXISTS `staff_staffperformance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `staff_staffperformance` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `evaluation_date` date NOT NULL,
  `performance_rating` int NOT NULL,
  `Staff_id` bigint NOT NULL,
  `owner_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `staff_staffperformance_Staff_id_19a28893_fk_staff_staff_id` (`Staff_id`),
  KEY `staff_staffperforman_owner_id_808e9299_fk_hos_login` (`owner_id`),
  CONSTRAINT `staff_staffperforman_owner_id_808e9299_fk_hos_login` FOREIGN KEY (`owner_id`) REFERENCES `hos_login_custom_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `staff_staffperformance`
--

LOCK TABLES `staff_staffperformance` WRITE;
/*!40000 ALTER TABLE `staff_staffperformance` DISABLE KEYS */;
/*!40000 ALTER TABLE `staff_staffperformance` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `staff_staffshift`
--

DROP TABLE IF EXISTS `staff_staffshift`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `staff_staffshift` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `shift_start` time(6) NOT NULL,
  `shift_end` datetime(6) NOT NULL,
  `Staff_id` bigint NOT NULL,
  `owner_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `staff_staffshift_Staff_id_acf6bdd7_fk_staff_staff_id` (`Staff_id`),
  KEY `staff_staffshift_owner_id_1e512f50_fk_hos_login_custom_user_id` (`owner_id`),
  CONSTRAINT `staff_staffshift_owner_id_1e512f50_fk_hos_login_custom_user_id` FOREIGN KEY (`owner_id`) REFERENCES `hos_login_custom_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `staff_staffshift`
--

LOCK TABLES `staff_staffshift` WRITE;
/*!40000 ALTER TABLE `staff_staffshift` DISABLE KEYS */;
/*!40000 ALTER TABLE `staff_staffshift` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-07-09 12:45:14
