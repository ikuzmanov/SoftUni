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

#3. Update
UPDATE coaches AS c
LEFT JOIN players_coaches AS pc ON c.id = pc.coach_id
SET c.coach_level = c.coach_level + 1
WHERE c.first_name LIKE 'A%' AND player_id IS NOT NULL;

#4. Delete
DELETE FROM players
WHERE age >=45;

#5. Players 
SELECT first_name, age, salary FROM players
ORDER BY salary DESC;

#6.	Young offense players without contract
SELECT p.id, p.salary, CONCAT(p.first_name,' ', p.last_name) AS 'full_name', p.age, p.position,p.hire_date FROM players AS p
JOIN skills_data AS sd ON sd.id = p.skills_data_id
WHERE p.position = "A" AND p.hire_date IS NULL AND p.age < 23 AND sd.strength > 50
ORDER BY p.salary ASC, p.age;

#7.	Detail info for all teams
SELECT t.name, t.established, t.fan_base, COUNT(p.id) AS 'players_count' FROM teams AS t
LEFT JOIN players AS p on t.id = p.team_id
GROUP BY t.id
ORDER BY players_count DESC, fan_base DESC;

#8.	The fastest player by towns
SELECT MAX(sd.speed) AS 'max_speed', t.name AS 'town_name' FROM towns AS t
JOIN stadiums AS s ON t.id = s.town_id
JOIN teams AS ts ON ts.stadium_id = s.id
LEFT JOIN players AS p ON ts.id = p.team_id
LEFT JOIN skills_data AS sd ON p.skills_data_id = sd.id
WHERE ts.name <> 'Devify'
GROUP BY t.id
ORDER BY max_speed DESC, town_name;

#9.	Total salaries and players by country
SELECT c.name, COUNT(p.id) AS 'total_count_of_players',
SUM(p.salary) AS 'total_sum_of_salaries' FROM countries AS c
LEFT JOIN towns AS t ON t.country_id = c.id
LEFT JOIN stadiums AS s ON s.town_id = t.id
LEFT JOIN teams AS tm ON tm.stadium_id = s.id
LEFT JOIN players AS p ON p.team_id = tm.id
GROUP BY c.id
ORDER BY total_count_of_players DESC, name ASC;

#10. Find all players that play on stadium
DELIMITER $$
CREATE FUNCTION udf_stadium_players_count(stadium_name VARCHAR(20))
RETURNS INTEGER
DETERMINISTIC
BEGIN
	RETURN (SELECT COUNT(p.id) AS cnt
	FROM players AS p
	RIGHT JOIN teams AS tm ON p.team_id = tm.id
	RIGHT JOIN stadiums AS s ON tm.stadium_id = s.id
	WHERE s.name = stadium_name);
END
$$

#11. Find good playmaker by teams
DELIMITER $$
CREATE PROCEDURE `udp_find_playmaker` (min_dribbling INT, teamname VARCHAR(40))
BEGIN
	SELECT CONCAT(first_name, ' ', last_name) AS 'full_name', p.age, p.salary, sd.dribbling, sd.speed, t.name AS 'team_name' FROM skills_data AS sd
	JOIN players AS p on p.skills_data_id = sd.id
	RIGHT JOIN teams AS t ON t.id = p.team_id
	WHERE t.name = teamname AND sd.speed > (SELECT AVG(speed) FROM skills_data) AND sd.dribbling > min_dribbling
	ORDER BY sd.speed DESC
	LIMIT 1;
END
$$