CREATE DATABASE if not exists `monitor` /*!40100 DEFAULT CHARACTER SET utf8 */;
  DROP TABLE IF EXISTS `monitor`.`trig_update_monitor`;
  CREATE TABLE `monitor`.`trig_update_monitor`(
  `id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  `txt` varchar(200) NULL,
  `user_id_new` bigint(20) default '0',
  `user_id_old` bigint(20) default '0',
  `account_new` varchar(50) default '',
  `account_old` varchar(50) default '',
  `bet_info_new`	longtext ,
  `bet_info_old`	longtext , 
  `money_new`	double(20,3) default '0',
  `money_old`	double(20,3) default '0', 
  `total_money_new`	double(20,3) default '0',
  `total_money_old`	double(20,3) default '0',  
  `odds_new`	varchar(100) default '',
  `odds_old`	varchar(100) default '', 
  `orderid_new`  int(11) unsigned default '0',
  `orderid_old`  int(11) unsigned default '0',
  `userid_new` bigint(20) DEFAULT '0',
  `userid_old` bigint(20) DEFAULT '0',
  `odds_float_new`  float  default '0',
  `odds_float_old`  float  default '0',
  `ratio_old`  varchar(256)  default '',
  `ratio_new`  varchar(256)  default '',
  `league_old` varchar(256)  default '',
  `league_new` varchar(256)  default '',
  `start_old` datetime default null,
  `start_new` datetime default null,
  `settleteamh_old`  varchar(256) default '',
  `settleteamh_new`  varchar(256) default '',
  `settleteamc_old`  varchar(256) default '',
  `settleteamc_new`  varchar(256) default '',
  `rtype_old` int(11) default '0',
  `rtype_new` int(11) default '0',
  `sportstype_old` int(11) default '0',
  `sportstype_new` int(11) default '0',
  `bettype_old` int(11) default '0',
  `bettype_new` int(11) default '0',
  `user`	varchar(100) default '', 
  `update_time` datetime(0) NULL ON UPDATE CURRENT_TIMESTAMP(0),
  PRIMARY KEY (`id`),
  KEY `idx_txt` (`txt`) USING BTREE,
  KEY `idx_update_time` (`update_time`) USING BTREE
  )ENGINE=InnoDB DEFAULT CHARSET=utf8;


USE `gameplat_sc_data`;

delimiter $$
DROP  TRIGGER IF EXISTS `trig_user_bet_update` $$
CREATE TRIGGER `gameplat_sc_data`.`trig_user_bet_update` BEFORE UPDATE ON `user_bet`
FOR EACH ROW
BEGIN
IF NEW.bet_info != old.bet_info or (old.bet_info is NULL and new.bet_info is not NULL ) THEN
insert into monitor.trig_update_monitor(txt,bet_info_new,bet_info_old,user,update_time) values('警告user_bet表bet_info列有修改数据操作',NEW.bet_info,old.bet_info,user(),now());
set NEW.bet_info = old.bet_info;
END IF;
 
IF NEW.user_id != old.user_id or (old.user_id is NULL and new.user_id is not NULL ) THEN
insert into monitor.trig_update_monitor(txt,user_id_new,user_id_old,user,update_time) values('警告user_bet表user_id列有修改数据操作',NEW.user_id,old.user_id,user(),now());
 set NEW.user_id = old.user_id;
END IF;
 
IF NEW.account != old.account or (old.account is NULL and new.account is not NULL ) THEN
insert into monitor.trig_update_monitor(txt,account_new,account_old,user,update_time) values('警告user_bet表account列有修改数据操作',NEW.account,old.account,user(),now());
 set NEW.account = old.account;
END IF;

IF NEW.odds != old.odds or (old.odds is NULL and new.odds is not NULL ) THEN
insert into monitor.trig_update_monitor(txt,odds_new,odds_old,user,update_time) values('警告user_bet表odds列有修改数据操作',NEW.odds,old.odds,user(),now());
 set NEW.odds = old.odds;
END IF;

IF NEW.total_money != old.total_money or (old.total_money is NULL and new.total_money is not NULL ) THEN
insert into monitor.trig_update_monitor(txt,total_money_new,total_money_old,user,update_time) values('警告user_bet表total_money列有修改数据操作',NEW.total_money,old.total_money,user(),now());
set NEW.total_money = old.total_money;
END IF;

IF NEW.money != old.money or (old.money is NULL and new.money is not NULL ) THEN
insert into monitor.trig_update_monitor(txt,money_new,money_old,user,update_time) values('警告user_bet表money列有修改数据操作',NEW.money,old.money,user(),now());
set NEW.money = old.money;
END IF;
END;$$

DROP  TRIGGER IF EXISTS `trig_user_bill_update` $$
CREATE TRIGGER `gameplat_sc_data`.`trig_user_bill_update` before UPDATE ON `user_bill`
FOR EACH ROW
BEGIN
SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = "警告：user_bill 表不允许update操作"; 
END;$$

DROP  TRIGGER IF EXISTS `trig_orders_update` $$
CREATE TRIGGER `gameplat_sc_data`.`trig_orders_update` BEFORE UPDATE ON `gameplat_sc_data`.`orders`
FOR EACH ROW
BEGIN

IF NEW.userid != old.userid or (old.userid is NULL and new.userid is not NULL ) THEN
insert into monitor.trig_update_monitor(txt,userid_new,userid_old,user,update_time) values('警告orders表userid列有修改数据操作',NEW.userid,old.userid,user(),now());
set NEW.userid = old.userid;
END IF;

IF NEW.odds != old.odds or (old.odds is NULL and new.odds is not NULL ) THEN
insert into monitor.trig_update_monitor(txt,Odds_float_new,Odds_float_old,user,update_time) values('警告orders表odds列有修改数据操作',NEW.odds,old.odds,user(),now());
set NEW.odds = old.odds;
END IF;

IF NEW.ratio != old.ratio or (old.ratio is NULL and new.ratio is not NULL ) THEN
insert into monitor.trig_update_monitor(txt,ratio_new,ratio_old,user,update_time) values('警告orders表ratio列有修改数据操作',NEW.ratio,old.ratio,user(),now());
 set NEW.ratio = old.ratio;
END IF;

IF NEW.league != old.league or (old.league is NULL and new.league is not NULL ) THEN
insert into monitor.trig_update_monitor(txt,league_new,league_old,user,update_time) values('警告orders表league列有修改数据操作',NEW.league,old.league,user(),now());
 set NEW.league = old.league;
END IF;

IF NEW.start != old.start or (old.start is NULL and new.start is not NULL ) THEN
insert into monitor.trig_update_monitor(txt,start_new,start_old,user,update_time) values('警告orders表start列有修改数据操作',NEW.start,old.start,user(),now());
 set NEW.start = old.start;
END IF;

IF NEW.settleteamh != old.settleteamh or (old.settleteamh is NULL and new.settleteamh is not NULL ) THEN
insert into monitor.trig_update_monitor(txt,settleteamh_new,settleteamh_old,user,update_time) values('警告orders表SettleTeamH列有修改数据操作',NEW.settleteamh,old.settleteamh,user(),now());
 set NEW.settleteamh = old.settleteamh;
END IF;

IF NEW.settleteamc != old.settleteamc or (old.settleteamc is NULL and new.settleteamc is not NULL ) THEN
insert into monitor.trig_update_monitor(txt,settleteamc_new,settleteamc_old,user,update_time) values('警告orders表SettleTeamC列有修改数据操作',NEW.settleteamc,old.settleteamc,user(),now());
 set NEW.settleteamc = old.settleteamc;
END IF;

IF NEW.rtype != old.rtype or (old.rtype is NULL and new.rtype is not NULL ) THEN
insert into monitor.trig_update_monitor(txt,RType_new,RType_old,user,update_time) values('警告orders表RType列有修改数据操作',NEW.rtype,old.rtype,user(),now());
 set NEW.rtype = old.rtype;
END IF;

IF NEW.sportstype != old.sportstype or (old.sportstype is NULL and new.sportstype is not NULL ) THEN
insert into monitor.trig_update_monitor(txt,SportsType_new,SportsType_old,user,update_time) values('警告orders表SportsType列有修改数据操作',NEW.sportstype,old.sportstype,user(),now());
 set NEW.sportstype = old.sportstype;
END IF;

IF NEW.bettype != old.bettype or (old.bettype is NULL and new.bettype is not NULL ) THEN
insert into monitor.trig_update_monitor(txt,SportsType_new,SportsType_old,user,update_time) values('警告orders表BetType列有修改数据操作',NEW.bettype,old.bettype,user(),now());
 set NEW.bettype = old.bettype;
END IF;
END;$$


DROP  TRIGGER IF EXISTS `trig_orders_chuan_update` $$
CREATE TRIGGER `gameplat_sc_data`.`trig_orders_chuan_update` BEFORE UPDATE ON `orders_chuan`
FOR EACH ROW
BEGIN

IF NEW.userid != old.userid or (old.userid is NULL and new.userid is not NULL ) THEN
insert into monitor.trig_update_monitor(txt,userid_new,userid_old,user,update_time) values('警告orders_chuan表userid列有修改数据操作',NEW.userid,old.userid,user(),now());
 set NEW.userid = old.userid;
END IF;

IF NEW.odds != old.odds or (old.odds is NULL and new.odds is not NULL ) THEN
insert into monitor.trig_update_monitor(txt,Odds_float_new,Odds_float_old,user,update_time) values('警告orders_chuan表odds列有修改数据操作',NEW.odds,old.odds,user(),now());
 set NEW.odds = old.odds;
END IF;

IF NEW.ratio != old.ratio or (old.ratio is NULL and new.ratio is not NULL ) THEN
insert into monitor.trig_update_monitor(txt,ratio_new,ratio_old,user,update_time) values('警告orders_chuan表ratio列有修改数据操作',NEW.ratio,old.ratio,user(),now());
 set NEW.ratio = old.ratio;
END IF;

IF NEW.league != old.league or (old.league is NULL and new.league is not NULL ) THEN
insert into monitor.trig_update_monitor(txt,league_new,league_old,user,update_time) values('警告orders_chuan表league列有修改数据操作',NEW.league,old.league,user(),now());
 set NEW.league = old.league;
END IF;

IF NEW.start != old.start or (old.start is NULL and new.start is not NULL ) THEN
insert into monitor.trig_update_monitor(txt,start_new,start_old,user,update_time) values('警告orders_chuan表start列有修改数据操作',NEW.start,old.start,user(),now());
 set NEW.start = old.start;
END IF;

IF NEW.settleteamh != old.settleteamh or (old.settleteamh is NULL and new.settleteamh is not NULL ) THEN
insert into monitor.trig_update_monitor(txt,settleteamh_new,settleteamh_old,user,update_time) values('警告orders_chuan表SettleTeamH列有修改数据操作',NEW.settleteamh,old.settleteamh,user(),now());
 set NEW.settleteamh = old.settleteamh;
END IF;

IF NEW.settleteamc != old.settleteamc or (old.settleteamc is NULL and new.settleteamc is not NULL ) THEN
insert into monitor.trig_update_monitor(txt,settleteamc_new,settleteamc_old,user,update_time) values('警告orders_chuan表SettleTeamC列有修改数据操作',NEW.settleteamc,old.settleteamc,user(),now());
 set NEW.settleteamc = old.settleteamc;
END IF;

IF NEW.rtype != old.rtype or (old.rtype is NULL and new.rtype is not NULL ) THEN
insert into monitor.trig_update_monitor(txt,RType_new,RType_old,user,update_time) values('警告orders_chuan表RType列有修改数据操作',NEW.rtype,old.rtype,user(),now());
 set NEW.rtype = old.rtype;
END IF;

IF NEW.sportstype != old.sportstype or (old.sportstype is NULL and new.sportstype is not NULL ) THEN
insert into monitor.trig_update_monitor(txt,SportsType_new,SportsType_old,user,update_time) values('警告orders_chuan表SportsType列有修改数据操作',NEW.sportstype,old.sportstype,user(),now());
 set NEW.sportstype = old.sportstype;
END IF;

IF NEW.bettype != old.bettype or (old.bettype is NULL and new.bettype is not NULL ) THEN
insert into monitor.trig_update_monitor(txt,SportsType_new,SportsType_old,user,update_time) values('警告orders_chuan表BetType列有修改数据操作',NEW.bettype,old.bettype,user(),now());
 set NEW.bettype = old.bettype;
END IF;

END;$$
delimiter ;
