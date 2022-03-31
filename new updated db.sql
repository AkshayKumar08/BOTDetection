/*
SQLyog Community Edition- MySQL GUI v7.15 
MySQL - 5.5.29 : Database - socialnetworking
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`socialnetworking` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `socialnetworking`;

/*Table structure for table `adds` */

DROP TABLE IF EXISTS `adds`;

CREATE TABLE `adds` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `img` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `adds` */

/*Table structure for table `admin` */

DROP TABLE IF EXISTS `admin`;

CREATE TABLE `admin` (
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `admin` */

insert  into `admin`(`username`,`password`) values ('admin','admin');

/*Table structure for table `advetiser` */

DROP TABLE IF EXISTS `advetiser`;

CREATE TABLE `advetiser` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `dob` varchar(100) DEFAULT NULL,
  `mail` varchar(100) DEFAULT NULL,
  `mobile` varchar(100) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `advetiser` */

/*Table structure for table `chat` */

DROP TABLE IF EXISTS `chat`;

CREATE TABLE `chat` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `uname` varchar(100) DEFAULT NULL,
  `fname` varchar(100) DEFAULT NULL,
  `msg` varchar(2000) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `chat` */

/*Table structure for table `comment` */

DROP TABLE IF EXISTS `comment`;

CREATE TABLE `comment` (
  `name` varchar(100) DEFAULT NULL,
  `post` varchar(100) DEFAULT NULL,
  `comment` varchar(100) DEFAULT NULL,
  `type` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `comment` */

/*Table structure for table `frequest` */

DROP TABLE IF EXISTS `frequest`;

CREATE TABLE `frequest` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `uname` varchar(100) DEFAULT NULL,
  `fname` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT 'Pending',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;

/*Data for the table `frequest` */

insert  into `frequest`(`id`,`uname`,`fname`,`status`) values (17,'raj','hari','Accepted'),(18,'hari','raj','Accepted');

/*Table structure for table `post` */

DROP TABLE IF EXISTS `post`;

CREATE TABLE `post` (
  `name` varchar(100) DEFAULT NULL,
  `post` varchar(100) DEFAULT NULL,
  `comment` varchar(100) DEFAULT 'pending',
  `type` varchar(100) DEFAULT 'pending'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `post` */

insert  into `post`(`name`,`post`,`comment`,`type`) values ('check','https://t.co/dnWuDbFRkt','pending','positive'),('new','https://t.co/dnWuDbFRkt','pending','positive');

/*Table structure for table `predict` */

DROP TABLE IF EXISTS `predict`;

CREATE TABLE `predict` (
  `ids` int(100) DEFAULT NULL,
  `url` varchar(100) DEFAULT NULL,
  `followers_count` int(30) DEFAULT NULL,
  `friends_count` int(20) DEFAULT NULL,
  `listed_count` int(20) DEFAULT NULL,
  `favourites_count` int(20) DEFAULT NULL,
  `verified` varchar(100) DEFAULT NULL,
  `statuses_count` int(20) DEFAULT NULL,
  `default_profile` varchar(20) DEFAULT NULL,
  `default_profile_image` varchar(20) DEFAULT NULL,
  `username` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `predict` */

insert  into `predict`(`ids`,`url`,`followers_count`,`friends_count`,`listed_count`,`favourites_count`,`verified`,`statuses_count`,`default_profile`,`default_profile_image`,`username`) values (2147483647,'https://t.co/dnWuDbFRkt',1291,0,10,0,'False',78554,'True','False','raj'),(16834046,'https://t.co/dzqjlKBL9p',1108807,1662,7220,2877,'True',27085,'False','False','hari');

/*Table structure for table `result` */

DROP TABLE IF EXISTS `result`;

CREATE TABLE `result` (
  `username` varchar(20) DEFAULT NULL,
  `prediction` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `result` */

insert  into `result`(`username`,`prediction`) values ('raj','this is bot message'),('hari','this is not a bot message');

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `mail` varchar(100) DEFAULT NULL,
  `gender` varchar(100) DEFAULT NULL,
  `dob` varchar(100) DEFAULT NULL,
  `mobile` varchar(100) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT 'pending',
  PRIMARY KEY (`id`),
  UNIQUE KEY `NewIndex1` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`id`,`name`,`password`,`mail`,`gender`,`dob`,`mobile`,`address`,`status`) values (15,'raj','raj','raj@gmail.com','Male','1984-12-13','7878787878','hyderabad','pending'),(16,'hari','hari','hari@gmail.com','Male','1984-12-12','3434343434','hyderabad','pending');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
