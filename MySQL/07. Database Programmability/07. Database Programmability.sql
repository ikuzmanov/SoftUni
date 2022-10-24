#1.	Employees with Salary Above 35000

DELIMITER $$
CREATE PROCEDURE usp_get_employees_salary_above_35000()

BEGIN
	SELECT first_name, last_name FROM employees
    WHERE salary > 35000
    ORDER BY first_name, last_name, employee_id;
END
$$
DELIMITER ;

#2.	Employees with Salary Above Number

DELIMITER $$
CREATE PROCEDURE usp_get_employees_salary_above(num DECIMAL(10,4))
BEGIN
	SELECT first_name, last_name FROM employees
    WHERE salary >= num
    ORDER BY first_name, last_name, employee_id;
END
$$
DELIMITER ;

#3.	Town Names Starting With

DELIMITER $$
CREATE PROCEDURE usp_get_towns_starting_with(town_str VARCHAR(20))
BEGIN
	SELECT t.name from towns AS t
    WHERE t.name LIKE CONCAT(town_str,'%')
    ORDER BY t.name;
END
$$
DELIMITER ;

#4.	Employees from Town

DELIMITER $$
CREATE PROCEDURE usp_get_employees_from_town(town_input VARCHAR(20))
BEGIN
	SELECT e.first_name, e.last_name FROM employees AS e
    JOIN addresses AS a ON a.address_id = e.address_id
    JOIN towns as t ON t.town_id = a.town_id
    WHERE t.name = town_input
    ORDER BY e.first_name, e.last_name, t.town_id;
END
$$
DELIMITER ;

#5.	Salary Level Function

DELIMITER $$
CREATE FUNCTION ufn_get_salary_level(salary DECIMAL(19, 4))
RETURNS VARCHAR(8)
DETERMINISTIC
BEGIN
    DECLARE salary_level VARCHAR(8);
    IF salary < 30000 THEN SET salary_level := 'Low';
    ELSEIF salary <= 50000 THEN SET salary_level := 'Average';
    ELSE SET salary_level := 'High';
    END IF;
    RETURN salary_level;
END $$
DELIMITER ;

#6.	Employees by Salary Level
DELIMITER $$
CREATE PROCEDURE usp_get_employees_by_salary_level(salary_level VARCHAR(7))
BEGIN
	SELECT e.first_name, e.last_name
    FROM employees AS e
    WHERE ufn_get_salary_level(e.salary) LIKE salary_level
    ORDER BY e.first_name DESC, e.last_name DESC;
END $$
DELIMITER ;
