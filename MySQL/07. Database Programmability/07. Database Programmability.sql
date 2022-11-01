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

#7.	Define Function

CREATE FUNCTION ufn_is_word_comprised(set_of_letters varchar(50), word varchar(50)) 
RETURNs BIT
RETURN word REGEXP(concat('^[', set_of_letters, ']+$'));


#8.	Find Full Name
DELIMITER $$
CREATE PROCEDURE usp_get_holders_full_name()
BEGIN
	SELECT CONCAT(first_name, ' ', last_name) AS 'full_name' FROM account_holders
    ORDER BY full_name, id;
END $$
DELIMITER ;

#9.	People with Balance Higher Than
DELIMITER $$
CREATE PROCEDURE usp_get_holders_with_balance_higher_than(balance_input DECIMAL(10,4))
BEGIN
	SELECT ah.first_name, ah.last_name
    FROM account_holders AS ah
    JOIN accounts AS a ON a.account_holder_id = ah.id
    GROUP BY a.account_holder_id
    HAVING SUM(a.balance) > balance_input
    ORDER BY a.id;
END $$
DELIMITER ;

#10 Future Value Function
DELIMITER $$
CREATE FUNCTION usp_calculate_future_value(initial_sum DECIMAL(19,2), 
					 									interest_rate DECIMAL(19,2),
                                                        years INT)
RETURNS DECIMAL(19,4)
DETERMINISTIC
BEGIN
	RETURN initial_sum * POW((1 + interest_rate), years);
END $$
DELIMITER ;

# 11. Calculating Interest
DELIMITER $$
CREATE PROCEDURE usp_calculate_future_value_for_account(account_id INT, interest_rate DECIMAL(19,4))
BEGIN
	SELECT 
		a.id AS 'account-id', 
		ah.first_name, 
		ah.last_name, 
		a.balance AS 'current_balance',
		usp_calculate_future_value(a.balance, interest_rate, 5) AS 'balance_in_5_years'
    FROM account_holders AS ah
    JOIN accounts AS a ON ah.id = a.account_holder_id
    WHERE a.id = account_id;
END $$
DELIMITER ;

#15.	Log Accounts Trigger

CREATE TABLE `logs`(
	log_id INT PRIMARY KEY AUTO_INCREMENT,
    account_id INT NOT NULL,
    old_sum DECIMAL(19,4) NOT NULL,
    new_sum DECIMAL(19,4) NOT NULL
    );

DELIMITER $$
	CREATE TRIGGER tr_balance_updated
    AFTER UPDATE ON accounts
    FOR EACH ROW
    BEGIN
		IF OLD.balance <> NEW.balance THEN
			INSERT INTO `logs` (account_id, old_sum, new_sum)
			VALUES (OLD.id, OLD.balance, NEW.balance);
		END IF;
    END $$
    
DELIMITER ;

#16.	Emails Trigger
CREATE TABLE notification_emails(
	`id` INT PRIMARY KEY AUTO_INCREMENT,
	`recipient` INT NOT NULL,
    `subject` VARCHAR(100) NOT NULL,
    `body` VARCHAR(255) NOT NULL
);

DELIMITER $$
	CREATE TRIGGER tr_notification_emails
    AFTER INSERT ON `logs`
    FOR EACH ROW 
    BEGIN
		INSERT INTO notification_emails(`recipient`, `subject`, `body`)
        VALUES (
        NEW.account_id,
        CONCAT('Balance change for account: ', NEW.account_id),
        CONCAT('On ', DATE_FORMAT(NOW(), '%b %d %Y at $r'), 
        ' your balance was changed from ',
        ROUND(NEW.old_sum,2) , ' to ', ROUND(NEW.new_sum,2), '.')
        );
    END $$
DELIMITER ;
