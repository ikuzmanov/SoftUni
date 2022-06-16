# 0. Create Database
CREATE SCHEMA `minions`;

# 1. Create Tables
CREATE TABLE `minions`(
`id` INT PRIMARY KEY AUTO_INCREMENT,
`name` VARCHAR(30),
`age` INT
);

CREATE TABLE `towns`(
`town_id` INT PRIMARY KEY AUTO_INCREMENT,
`name` VARCHAR(30)
);

# 2. Alter Minions Table
ALTER TABLE `towns`
CHANGE COLUMN `town_id` `id` INT;

ALTER TABLE `minions`
ADD COLUMN `town_id` INT,
ADD CONSTRAINT FOREIGN KEY minions(`town_id`)
REFERENCES towns(`id`);

# 3. Insert Records in Both Tables
INSERT INTO `towns` (`id`, `name`)
VALUES ("1", "Sofia"),
("2", "Plovdiv"),
("3", "Varna");

INSERT INTO `minions` (`id`, `name`, `age`, `town_id`) 
VALUES ("1", "Kevin", "22", "1"),
("2", "Bob", "15", "3"),
("3", "Steward", NULL, "2");

# 4. Truncate Table Minions
TRUNCATE TABLE `minions`;

# 5. Drop All Tables
DROP TABLE `minions`;
DROP TABLE `towns`;

# 6. Create Table People
CREATE TABLE `people`(
`id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE,
`name` VARCHAR(200) NOT NULL,
`picture` BLOB,
`height` DOUBLE(10,2),
`weight` DOUBLE(10,2),
`gender` CHAR(1) NOT NULL,
`birthdate` DATE NOT NULL,
`biography` TEXT
);
INSERT INTO `people` (`name`, `gender`, `birthdate`)
VALUES 
('Test', 'M', DATE(NOW())),
('Test', 'M', DATE(NOW())),
('Test', 'M', DATE(NOW())),
('Test', 'M', DATE(NOW())),
('Test', 'M', DATE(NOW()));

# 7. Create Table Users
CREATE TABLE `users` (
	`id` INT AUTO_INCREMENT UNIQUE,
    `username` VARCHAR(30) NOT NULL,
    `password` VARCHAR(26) NOT NULL,
    `profile_picture` BLOB,
    `last_login_time` TIME,
    `is_deleted` BOOLEAN,
	CONSTRAINT pk_users 
    PRIMARY KEY `users`(`id`)
);

INSERT INTO `users`(`username`, `password`)
VALUES
('Gosho', '12345'),
('Pesho', '12345'),
('Ivancho', '12345'),
('Mariika', '12345'),
('Diuner', '12345');

# 8. Change Primary Key
ALTER TABLE `users` DROP PRIMARY KEY,
ADD CONSTRAINT pk_users PRIMARY KEY `users`(`id`, `username`);

# 9. Set Default Value of a Field
ALTER TABLE `users`
CHANGE COLUMN `last_login_time` `last_login_time` DATETIME DEFAULT NOW();

# 10. Set Unique Field
ALTER TABLE `users` DROP PRIMARY KEY, 
ADD CONSTRAINT pk_users PRIMARY KEY `users`(`id`), 
CHANGE COLUMN `username` `username` VARCHAR(50) UNIQUE;

# 11. Movies Database
CREATE SCHEMA `movies`;
USE `movies`;

CREATE TABLE `directors`(
	`id` INT AUTO_INCREMENT PRIMARY KEY,
    `director_name` VARCHAR(50) NOT NULL,
    `notes` TEXT
);
INSERT INTO `directors` (`director_name`, `notes`)
VALUES
('Spielberg', 'Note1'),
('Gosho', 'Note2'),
('Petio' ,'Note3'),
('KENEDI', 'Note4'),
('directorsTigara', 'Note5');

CREATE TABLE `genres` (
	`id` INT AUTO_INCREMENT PRIMARY KEY,
    `genre_name` VARCHAR(50) NOT NULL,
    `notes` TEXT
);
INSERT INTO `genres`(`genre_name`, `notes`)
VALUES 
('TestName1', 'TestNotes'),
('TestName2', 'TestNotes'),
('TestName3', 'TestNotes'),
('TestName4', 'TestNotes'),
('TestName5', 'TestNotes');

CREATE TABLE `categories` (
	`id` INT AUTO_INCREMENT PRIMARY KEY,
    `category_name` VARCHAR(50) NOT NULL,
    `notes` TEXT
);
INSERT INTO `categories`(`category_name`, `notes`)
VALUES 
('TestName1', 'TestNotes'),
('TestName2', 'TestNotes'),
('TestName3', 'TestNotes'),
('TestName4', 'TestNotes'),
('TestName5', 'TestNotes');

CREATE TABLE `movies` (
	`id` INT PRIMARY KEY AUTO_INCREMENT,
    `title` VARCHAR(40) NOT NULL, 
    `director_id` INT,
    `copyright_year` INT,
    `length` INT,
    `genre_id` INT,
    `category_id` INT,
    `rating` DOUBLE, 
    `notes` TEXT
);

INSERT INTO `movies` (`title`)
VALUES
("New Movies"),
("Ima takav narod"),
("Goshovite istorii"),
("Varna moreto"),
('Pred plaza shte laza');

# 12. Car Rental Database
CREATE SCHEMA `car_rental`;
USE `car_rental`;

CREATE TABLE `categories`(
	`id` INT PRIMARY KEY AUTO_INCREMENT,
    `category` VARCHAR(30) NOT NULL,
    `daily_rate` DOUBLE,
    `weekly_rate` DOUBLE,
    `monthly_rate` DOUBLE,
    `weekend_rate` DOUBLE
); 

INSERT INTO `categories`(`category`)
VALUES
('TestCategory1'),
('TestCategory2'),
('TestCategory3');

CREATE TABLE `cars`(
	`id` INT PRIMARY KEY AUTO_INCREMENT,
    `plate_number` VARCHAR(10) NOT NULL, 
    `make` VARCHAR(30),
    `model` VARCHAR(30) NOT NULL,
    `car_year` YEAR,
    `category_id` INT,
    `doors` INT,
    `picture` BLOB,
    `car_condition` TEXT,
    `available` BOOLEAN,
    CONSTRAINT fk_cars_category
    FOREIGN KEY `cars`(`category_id`) REFERENCES `categories`(`id`)
);

INSERT INTO `cars`(`plate_number`, `model`, `category_id`)
VALUES
('B1234AP', 'VW Golf', 2),
('CA1234AP', 'VW Passat', 3),
('H5522CA', 'Audi A4', 2);

CREATE TABLE `employees`(
	`id` INT PRIMARY KEY AUTO_INCREMENT,
	`first_name` VARCHAR(20) NOT NULL,
    `last_name` VARCHAR(20) NOT NULL,
    `title` VARCHAR(20),
    `notes` TEXT
);

INSERT INTO `employees`(`first_name`, `last_name`)
VALUES
('Ivancho', 'Stoyanov'),
('Petar', 'Georgiev'),
('Stoyan', 'Ivanov');

CREATE TABLE `customers`(
	`id` INT PRIMARY KEY AUTO_INCREMENT,
    `driver_licence_number` VARCHAR(20) NOT NULL,
    `full_name` VARCHAR(20) NOT NULL,
    `address` VARCHAR(30),
    `city` VARCHAR(30),
    `zip_code` INT(4),
    `notes` TEXT
);

INSERT INTO `customers`(`driver_licence_number`, `full_name`)
VALUES
('B1234AP', 'Gosho'),
('CA1234AP', 'Ivancho'),
('H5522CA', 'Testcho');

CREATE TABLE `rental_orders`(
	`id` INT PRIMARY KEY AUTO_INCREMENT,
	`employee_id` INT, 
	`customer_id` INT, 
	`car_id` INT, 
	`car_condition` TEXT, 
	`tank_level` INT, 
	`kilometrage_start` INT, 
	`kilometrage_end` INT, 
	`total_kilometrage` INT, 
	`start_date` DATETIME, 
	`end_date` DATETIME, 
	`total_days` INT, 
	`rate_applied` DOUBLE, 
	`tax_rate` DOUBLE, 
	`order_status` BOOLEAN, 
    `notes` TEXT,
    CONSTRAINT fk_rental_orders_employees
    FOREIGN KEY `rental_orders`(`employee_id`) REFERENCES `employees`(`id`),
	CONSTRAINT fk_rental_orders_customers
    FOREIGN KEY `rental_orders`(`customer_id`) REFERENCES `customers`(`id`),
	CONSTRAINT fk_rental_orders_cars
    FOREIGN KEY `rental_orders`(`car_id`) REFERENCES `cars`(`id`)
);

INSERT INTO `rental_orders`(`employee_id`, `customer_id`, `car_id`)
VALUES
(1,2,3),
(2,2,3),
(3,1,2);
