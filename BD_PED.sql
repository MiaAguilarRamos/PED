-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: ppedd
-- ------------------------------------------------------
-- Server version	8.0.36

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
-- Table structure for table `tabla_apple`
--

DROP TABLE IF EXISTS `tabla_apple`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tabla_apple` (
  `Cuenta` varchar(100) DEFAULT NULL,
  `2024-31/03` int DEFAULT NULL,
  `2023-31/12` int DEFAULT NULL,
  `2023-30/09` int DEFAULT NULL,
  `2023-30/06` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tabla_apple`
--

LOCK TABLES `tabla_apple` WRITE;
/*!40000 ALTER TABLE `tabla_apple` DISABLE KEYS */;
INSERT INTO `tabla_apple` VALUES ('Total de activos corrientes',128416,143692,143566,122659),('Efectivo e inversiones a corto plazo',67150,73100,61555,62482),('Efectivo',0,0,0,0),('Efectivo y equivalentes de efectivo',32695,40760,29965,28408),('Inversiones a corto plazo',34455,32340,31590,34074),('Cuentas por cobrar, Neto',41150,50102,60985,39186),('Cuentas por cobrar - Comercio, Neto',21837,23194,29508,19549),('Inventarios, Neto',6232,6511,6331,7351),('Pagos anticipados',0,0,0,0),('Otros activos corrientes, Neto',13884,13979,14695,13640),('Total activo',337411,353514,352583,335038),('Inmuebles, mobiliario y equipo (neto)',43546,43666,54376,43550),('Inmuebles, mobiliario y equipo (bruto)',0,116176,125260,114337),('Depreciación acumulada, Total',0,-72510,-70884,-70787),('Crédito mercantil',0,0,0,0),('Intangibles, Neto',0,0,0,0),('Inversiones permanentes',95187,99475,100544,104061),('Documentos a cobrar a largo plazo',19313,26908,31477,19637),('Otros activos permanentes, Total',70262,66681,54097,64768),('Otros activos, Total',13421,2728,-8369,15879),('Total pasivos corrientes',123822,133973,145308,124963),('Cuentas por pagar',45753,58146,62611,46699),('Cuentas por pagar /Obligaciones',0,0,0,0),('Inversiones a corto plazo',0,0,0,0),('Documentos por pagar/Deuda a corto plazo',1997,1998,5985,3993),('Deudas con entidades de crédito y obligaciones u otros valores negociables',10762,10954,11397,7216),('Otras cuentas por pagar, Total',65310,62875,65315,67055),('Total pasivo',263217,279414,290437,274764),('Deuda a largo plazo, Total',91831,95088,96140,98071),('Deuda a largo plazo',91831,95088,95281,98071),('Obligaciones por contratos de arrendamiento financiero',0,0,859,0),('Impuesto a las ganancias diferido',0,0,0,0),('Participación no controladora',0,0,0,0),('Otros pasivos, Total',45567,48355,43004,47737),('Capital contable',74194,74100,62146,60274),('Acciones preferidas rescatable',0,0,0,0),('Crédito mercantil',0,0,0,0),('Acciones comunes Total',78815,75236,73812,70667),('Prima en venta de acciones',0,0,0,0),('Resultado de ejercicios anteriores',4339,8242,-214,1408),('Acciones en tesorería - Acciones Comunes',0,0,0,0),('ESOP Acciones a empleados',0,0,0,0),('Ganancia (pérdida) no realizada',0,0,0,0),('Otras participaciones, Total',-8960,-9378,-11452,-11801),('Total Pasivo y Capital Contable',337411,353514,352583,335038),('Total de Acciones Comunes en circulación',15337,15460,15550,15647),('Total de Acciones preferidas en circulación',0,0,0,0);
/*!40000 ALTER TABLE `tabla_apple` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tabla_spotify`
--

DROP TABLE IF EXISTS `tabla_spotify`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tabla_spotify` (
  `Cuenta` varchar(100) DEFAULT NULL,
  `2024-31/03` int DEFAULT NULL,
  `2023-31/12` int DEFAULT NULL,
  `2023-30/09` int DEFAULT NULL,
  `2023-30/06` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tabla_spotify`
--

LOCK TABLES `tabla_spotify` WRITE;
/*!40000 ALTER TABLE `tabla_spotify` DISABLE KEYS */;
INSERT INTO `tabla_spotify` VALUES ('Total de activos corrientes',5644,5260,4695,4329),('Efectivo e inversiones a corto plazo',4334,3973,3475,3391),('Efectivo',0,0,0,0),('Efectivo y equivalentes de efectivo',3451,3114,2618,2550),('Inversiones a corto plazo',883,859,857,841),('Cuentas por cobrar, Neto',798,878,755,640),('Cuentas por cobrar - Comercio, Neto',559,602,516,427),('Inventarios, Neto',0,0,0,0),('Pagos anticipados',77,64,89,109),('Otros activos corrientes, Neto',435,345,376,189),('Total activo',9075,8346,7592,7312),('Inmuebles, mobiliario y equipo (neto)',498,547,618,624),('Inmuebles, mobiliario y equipo (bruto)',1086,1221,1251,1220),('Depreciación acumulada, Total',-588,-674,-633,-596),('Crédito mercantil',1159,1137,1180,1148),('Intangibles, Neto',76,84,98,105),('Inversiones permanentes',1534,1215,903,1015),('Documentos a cobrar a largo plazo',239,276,239,213),('Otros activos permanentes, Total',72,75,75,76),('Otros activos, Total',612,354,501,405),('Total pasivos corrientes',3966,4090,3701,3546),('Cuentas por pagar',715,662,655,623),('Cuentas por pagar /Obligaciones',0,0,0,0),('Inversiones a corto plazo',2467,2674,2323,2261),('Documentos por pagar/Deuda a corto plazo',0,0,0,0),('Deudas con entidades de crédito y obligaciones u otros valores negociables',69,65,65,54),('Otras cuentas por pagar, Total',715,689,658,608),('Total pasivo',5766,5823,5453,5258),('Deuda a largo plazo, Total',1763,1696,1729,1689),('Deuda a largo plazo',1270,1203,1209,1167),('Obligaciones por contratos de arrendamiento financiero',493,493,520,522),('Impuesto a las ganancias diferido',17,8,6,6),('Participación no controladora',0,0,0,0),('Otros pasivos, Total',20,29,17,17),('Capital contable',3309,2523,2139,2054),('Acciones preferidas rescatable',0,0,0,0),('Crédito mercantil',0,0,0,0),('Acciones comunes Total',0,0,0,0),('Prima en venta de acciones',5397,5155,4931,4899),('Resultado de ejercicios anteriores',-3985,-4182,-4112,-4177),('Acciones en tesorería - Acciones Comunes',-262,-262,-262,-262),('ESOP Acciones a empleados',0,0,0,0),('Ganancia (pérdida) no realizada',0,0,0,0),('Otras participaciones, Total',2159,1812,1582,1594),('Total Pasivo y Capital Contable',9075,8346,7592,7312),('Total de Acciones Comunes en circulación',199,197,195,194),('Total de Acciones preferidas en circulación',0,0,0,0),('Total de activos corrientes',5644,5260,4695,4329),('Efectivo e inversiones a corto plazo',4334,3973,3475,3391),('Efectivo',0,0,0,0),('Efectivo y equivalentes de efectivo',3451,3114,2618,2550),('Inversiones a corto plazo',883,859,857,841),('Cuentas por cobrar, Neto',798,878,755,640),('Cuentas por cobrar - Comercio, Neto',559,602,516,427),('Inventarios, Neto',0,0,0,0),('Pagos anticipados',77,64,89,109),('Otros activos corrientes, Neto',435,345,376,189),('Total activo',9075,8346,7592,7312),('Inmuebles, mobiliario y equipo (neto)',498,547,618,624),('Inmuebles, mobiliario y equipo (bruto)',1086,1221,1251,1220),('Depreciación acumulada, Total',-588,-674,-633,-596),('Crédito mercantil',1159,1137,1180,1148),('Intangibles, Neto',76,84,98,105),('Inversiones permanentes',1534,1215,903,1015),('Documentos a cobrar a largo plazo',239,276,239,213),('Otros activos permanentes, Total',72,75,75,76),('Otros activos, Total',612,354,501,405),('Total pasivos corrientes',3966,4090,3701,3546),('Cuentas por pagar',715,662,655,623),('Cuentas por pagar /Obligaciones',0,0,0,0),('Inversiones a corto plazo',2467,2674,2323,2261),('Documentos por pagar/Deuda a corto plazo',0,0,0,0),('Deudas con entidades de crédito y obligaciones u otros valores negociables',69,65,65,54),('Otras cuentas por pagar, Total',715,689,658,608),('Total pasivo',5766,5823,5453,5258),('Deuda a largo plazo, Total',1763,1696,1729,1689),('Deuda a largo plazo',1270,1203,1209,1167),('Obligaciones por contratos de arrendamiento financiero',493,493,520,522),('Impuesto a las ganancias diferido',17,8,6,6),('Participación no controladora',0,0,0,0),('Otros pasivos, Total',20,29,17,17),('Capital contable',3309,2523,2139,2054),('Acciones preferidas rescatable',0,0,0,0),('Crédito mercantil',0,0,0,0),('Acciones comunes Total',0,0,0,0),('Prima en venta de acciones',5397,5155,4931,4899),('Resultado de ejercicios anteriores',-3985,-4182,-4112,-4177),('Acciones en tesorería - Acciones Comunes',-262,-262,-262,-262),('ESOP Acciones a empleados',0,0,0,0),('Ganancia (pérdida) no realizada',0,0,0,0),('Otras participaciones, Total',2159,1812,1582,1594),('Total Pasivo y Capital Contable',9075,8346,7592,7312),('Total de Acciones Comunes en circulación',199,197,195,194),('Total de Acciones preferidas en circulación',0,0,0,0),('Total de activos corrientes',5644,5260,4695,4329),('Efectivo e inversiones a corto plazo',4334,3973,3475,3391),('Efectivo',0,0,0,0),('Efectivo y equivalentes de efectivo',3451,3114,2618,2550),('Inversiones a corto plazo',883,859,857,841),('Cuentas por cobrar, Neto',798,878,755,640),('Cuentas por cobrar - Comercio, Neto',559,602,516,427),('Inventarios, Neto',0,0,0,0),('Pagos anticipados',77,64,89,109),('Otros activos corrientes, Neto',435,345,376,189),('Total activo',9075,8346,7592,7312),('Inmuebles, mobiliario y equipo (neto)',498,547,618,624),('Inmuebles, mobiliario y equipo (bruto)',1086,1221,1251,1220),('Depreciación acumulada, Total',-588,-674,-633,-596),('Crédito mercantil',1159,1137,1180,1148),('Intangibles, Neto',76,84,98,105),('Inversiones permanentes',1534,1215,903,1015),('Documentos a cobrar a largo plazo',239,276,239,213),('Otros activos permanentes, Total',72,75,75,76),('Otros activos, Total',612,354,501,405),('Total pasivos corrientes',3966,4090,3701,3546),('Cuentas por pagar',715,662,655,623),('Cuentas por pagar /Obligaciones',0,0,0,0),('Inversiones a corto plazo',2467,2674,2323,2261),('Documentos por pagar/Deuda a corto plazo',0,0,0,0),('Deudas con entidades de crédito y obligaciones u otros valores negociables',69,65,65,54),('Otras cuentas por pagar, Total',715,689,658,608),('Total pasivo',5766,5823,5453,5258),('Deuda a largo plazo, Total',1763,1696,1729,1689),('Deuda a largo plazo',1270,1203,1209,1167),('Obligaciones por contratos de arrendamiento financiero',493,493,520,522),('Impuesto a las ganancias diferido',17,8,6,6),('Participación no controladora',0,0,0,0),('Otros pasivos, Total',20,29,17,17),('Capital contable',3309,2523,2139,2054),('Acciones preferidas rescatable',0,0,0,0),('Crédito mercantil',0,0,0,0),('Acciones comunes Total',0,0,0,0),('Prima en venta de acciones',5397,5155,4931,4899),('Resultado de ejercicios anteriores',-3985,-4182,-4112,-4177),('Acciones en tesorería - Acciones Comunes',-262,-262,-262,-262),('ESOP Acciones a empleados',0,0,0,0),('Ganancia (pérdida) no realizada',0,0,0,0),('Otras participaciones, Total',2159,1812,1582,1594),('Total Pasivo y Capital Contable',9075,8346,7592,7312),('Total de Acciones Comunes en circulación',199,197,195,194),('Total de Acciones preferidas en circulación',0,0,0,0);
/*!40000 ALTER TABLE `tabla_spotify` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-06-11  2:13:58
