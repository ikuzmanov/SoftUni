#1.	One-To-One Relationship

CREATE TABLE `people` (
	person_id INT UNIQUE,
    first_name VARCHAR(50) NOT NULL,
    salary DECIMAL(10,2) ,
    passport_id INT UNIQUE
);

CREATE TABLE `passports`(
	passport_id INT UNIQUE,
    passport_number VARCHAR(50) UNIQUE
)
;

INSERT INTO `people`(person_id, first_name, salary, passport_id)
VALUES 
(1, 'Roberto', 43300, 101),
(2, 'Tom', 56100, 102),
(3, 'Yana', 60200, 103)
;

INSERT INTO `passports` (passport_id, passport_number)
VALUES
(101, 'N34FG21B'),
(102, 'K65LO4R7'),
(103, 'ZE657QP2');

ALTER TABLE `people`
ADD CONSTRAINT pk_people
PRIMARY KEY (person_id);

ALTER TABLE `passports`
ADD CONSTRAINT fk_passports_people
FOREIGN KEY (passport_id)
REFERENCES people(passport_id);