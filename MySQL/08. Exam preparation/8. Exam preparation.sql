#1.	Table Design

CREATE TABLE countries (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(45) NOT NULL
);

CREATE TABLE towns (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(45) NOT NULL,
    country_id INT NOT NULL,
    CONSTRAINT fk_towns_countries FOREIGN KEY (country_id)
        REFERENCES countries (id)
);

CREATE TABLE stadiums (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(45) NOT NULL,
    capacity INT NOT NULL,
    town_id INT NOT NULL,
    CONSTRAINT fk_stadiums_towns FOREIGN KEY (town_id)
        REFERENCES towns (id)
);

CREATE TABLE teams (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(45) NOT NULL,
    established DATE NOT NULL,
    fan_base BIGINT NOT NULL DEFAULT 0,
    stadium_id INT NOT NULL,
    CONSTRAINT fk_teams_stadiums FOREIGN KEY (stadium_id)
		REFERENCES stadiums (id)
);
 
 CREATE TABLE skills_data (
	id INT PRIMARY KEY AUTO_INCREMENT,
	dribbling INT DEFAULT 0,
	pace INT DEFAULT 0,
	passing INT DEFAULT 0,
	shooting INT DEFAULT 0,
	speed INT DEFAULT 0, 
	strength INT DEFAULT 0
 );

CREATE TABLE coaches (
	id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(10) NOT NULL,
    last_name VARCHAR(20) NOT NULL,
    salary DECIMAL(10,2) NOT NULL DEFAULT 0,
    coach_level INT NOT NULL DEFAULT 0
);

CREATE TABLE players (
    id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(10) NOT NULL,
    last_name VARCHAR(20) NOT NULL,
    age INT NOT NULL DEFAULT 0,
    position CHAR(1) NOT NULL,
    salary DECIMAL(10 , 2 ) NOT NULL DEFAULT 0,
    hire_date DATETIME,
    skills_data_id INT NOT NULL,
    team_id INT,
    CONSTRAINT fk_players_skills_data FOREIGN KEY (skills_data_id)
        REFERENCES skills_data (id),
    CONSTRAINT fk_players_teams FOREIGN KEY (team_id)
        REFERENCES teams (id)
);

CREATE TABLE players_coaches (
    player_id INT,
    coach_id INT,
    CONSTRAINT fk_maping_player FOREIGN KEY (player_id)
        REFERENCES players (id),
    CONSTRAINT fk_maping_coaches FOREIGN KEY (coach_id)
        REFERENCES coaches (id)
);

#2.	Insert
INSERT INTO coaches (first_name, last_name, salary, coach_level) 
SELECT first_name, last_name, salary*2, char_length(first_name) AS 'coach_level' FROM players 
WHERE age >= 45;