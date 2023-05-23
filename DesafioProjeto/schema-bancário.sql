CREATE TABLE `Clientes` (
	`id` int NOT NULL,
	`nome` VARCHAR(255) NOT NULL,
	`cpf` VARCHAR(255) NOT NULL,
	`endereço` VARCHAR(255) NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `Contas` (
	`id` int NOT NULL AUTO_INCREMENT,
	`tipo` VARCHAR(255) NOT NULL,
	`agencia` VARCHAR(255) NOT NULL,
	`num` INT NOT NULL,
	`id_cliente` INT NOT NULL,
	`saldo` DECIMAL NOT NULL,
	PRIMARY KEY (`id`)
);

ALTER TABLE `Contas` ADD CONSTRAINT `Contas_fk0` FOREIGN KEY (`id_cliente`) REFERENCES `Clientes`(`id`);



