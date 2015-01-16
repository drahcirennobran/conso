USE conso;
drop table if exists conso;
CREATE TABLE conso(
       `idCompteur` INT,
       `captureDate` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
       `conso` INT,
       KEY(captureDate)
);