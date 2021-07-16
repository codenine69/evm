-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema evm
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema evm
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `evm` DEFAULT CHARACTER SET utf8 ;
USE `evm` ;

-- -----------------------------------------------------
-- Table `evm`.`detalleac`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `evm`.`detalleac` ;

CREATE TABLE IF NOT EXISTS `evm`.`detalleac` (
  `iddetalleac` INT(11) NOT NULL AUTO_INCREMENT,
  `id_proyecto` INT(11) NULL DEFAULT NULL,
  `orden` INT(11) NULL DEFAULT NULL,
  `ac` INT(11) NULL DEFAULT NULL,
  `ac_acumulado` INT(11) NULL DEFAULT NULL,
  PRIMARY KEY (`iddetalleac`))
ENGINE = InnoDB
AUTO_INCREMENT = 1
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `evm`.`detalleev`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `evm`.`detalleev` ;

CREATE TABLE IF NOT EXISTS `evm`.`detalleev` (
  `iddetalleEV` INT(11) NOT NULL AUTO_INCREMENT,
  `id_proyecto` INT(11) NULL DEFAULT NULL,
  `orden` INT(11) NULL DEFAULT NULL,
  `ev` INT(11) NULL DEFAULT NULL,
  `ev_acumulado` INT(11) NULL DEFAULT NULL,
  PRIMARY KEY (`iddetalleEV`))
ENGINE = InnoDB
AUTO_INCREMENT = 1
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `evm`.`proyecto`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `evm`.`proyecto` ;

CREATE TABLE IF NOT EXISTS `evm`.`proyecto` (
  `idproyecto` INT(11) NOT NULL AUTO_INCREMENT,
  `nom_proyecto` VARCHAR(45) NULL DEFAULT NULL,
  `hitos` INT(11) NULL DEFAULT NULL,
  `bac` INT(11) NULL DEFAULT NULL,
  PRIMARY KEY (`idproyecto`))
ENGINE = InnoDB
AUTO_INCREMENT = 1
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `evm`.`detallepv`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `evm`.`detallepv` ;

CREATE TABLE IF NOT EXISTS `evm`.`detallepv` (
  `id_detalle` INT(11) NOT NULL AUTO_INCREMENT,
  `id_proyecto` INT(11) NULL DEFAULT NULL,
  `orden` INT(11) NULL DEFAULT NULL,
  `pv` INT(11) NULL DEFAULT NULL,
  `pv_acumulado` INT(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id_detalle`),
  INDEX `id_proyecto_idx` (`id_proyecto` ASC),
  CONSTRAINT `id_proyecto`
    FOREIGN KEY (`id_proyecto`)
    REFERENCES `evm`.`proyecto` (`idproyecto`))
ENGINE = InnoDB
AUTO_INCREMENT = 1
DEFAULT CHARACTER SET = utf8;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

/*INSERTAR UN REGISTRO*/ 

insert into proyecto values(1,'1',1,1);
insert into detallepv values(1,1,1,1,1);
insert into detalleev values(1,1,1,1,1);
insert into detalleac values(1,1,1,1,1);