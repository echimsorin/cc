USE `<Database name>`;

CREATE TABLE `dogs` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `age` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO dogs (name, age) VALUES("Einstein", 3);
INSERT INTO dogs (name, age) VALUES("Kaya", 5);