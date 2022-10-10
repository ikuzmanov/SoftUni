#1. Employee Address
SELECT 
    e.employee_id, e.job_title, a.address_id, a.address_text
FROM
    addresses AS a
        JOIN
    employees AS e ON a.address_id = e.address_id
ORDER BY address_id ASC
LIMIT 5;

#2.	Addresses with Towns
SELECT 
    e.first_name, e.last_name, t.name, a.address_text
FROM
    employees AS e
        JOIN
    addresses AS a ON a.address_id = e.address_id
        JOIN
    towns AS t ON t.town_id = a.town_id
ORDER BY first_name , last_name ASC
LIMIT 5;

#3.	Sales Employee
SELECT
	e.employee_id, e.first_name, e.last_name, d.name AS 'department_name'
FROM
	employees AS e
		JOIN
	departments AS d ON d.department_id = e.department_id
WHERE e.department_id = 3
ORDER BY e.employee_id DESC;
	
#4.	Employee Departments
SELECT
	e.employee_id, e.first_name, e.salary, d.name AS 'department_name'
FROM
	employees AS e
		JOIN
	departments AS d ON d.department_id = e.department_id
WHERE e.salary > 15000
ORDER BY d.department_id DESC
LIMIT 5;

#5.	Employees Without Project
SELECT 
    e.employee_id, e.first_name
FROM
    employees AS e
        LEFT JOIN
    employees_projects AS ep ON e.employee_id = ep.employee_id
WHERE
    ep.project_id is NULL
ORDER BY e.employee_id DESC
LIMIT 3;

#6.	Employees Hired After
SELECT 
	e.first_name, e.last_name, e.hire_date, d.name
FROM
	employees AS e
		JOIN
	departments AS d ON d.department_id = e.department_id
WHERE e.hire_date > 1999-01-01 AND e.department_id IN (3,10)
ORDER BY e.hire_date ASC;

#7.	Employees with Project
SELECT 
    e.employee_id, e.first_name, p.name AS project_name
FROM
    employees AS e
        JOIN
    employees_projects AS ep ON e.employee_id = ep.employee_id
        JOIN
    projects AS p ON ep.project_id = p.project_id
WHERE
    DATE(p.start_date) > '2002-08-13'
        AND p.end_date IS NULL
ORDER BY e.first_name ASC , p.name ASC
LIMIT 5;

#8.	Employee 24
SELECT 
	e.employee_id, e.first_name, IF(YEAR(p.start_date) >= 2005, NULL, p.name)
FROM
	employees AS e
        JOIN
    employees_projects AS ep ON e.employee_id = ep.employee_id
        JOIN
    projects AS p ON ep.project_id = p.project_id
WHERE e.employee_id = 24
ORDER BY p.name;

#9.	Employee Manager
SELECT 
    e.employee_id, e.first_name, e.manager_id, m.first_name
FROM
    employees AS e
        JOIN
    employees AS m ON e.manager_id = m.employee_id
WHERE
    e.manager_id IN (3 , 7)
ORDER BY e.first_name ASC;

#10. Employee Summary
SELECT 
    e.employee_id,
    CONCAT(e.first_name, ' ', e.last_name) AS 'employee_name',
    CONCAT(m.first_name, ' ', m.last_name) AS 'manager_name',
    d.name
FROM
    employees AS e
        JOIN
    employees AS m ON e.manager_id = m.employee_id
        JOIN
    departments AS d ON e.department_id = d.department_id
ORDER BY e.employee_id ASC
LIMIT 5;

#11. Min Average Salary
SELECT 
    AVG(e.salary) AS min_average_salary
FROM
    employees AS e
GROUP BY e.department_id
ORDER BY min_average_salary ASC
LIMIT 1;

#12. Highest Peaks in Bulgaria
SELECT 
    c.country_code, m.mountain_range, p.peak_name, p.elevation
FROM
    peaks AS p
        JOIN
    mountains AS m ON p.mountain_id = m.id
        JOIN
    mountains_countries AS mc ON mc.mountain_id = p.mountain_id
        JOIN
    countries AS c ON c.country_code = mc.country_code
WHERE
    p.elevation > 2835
        AND c.country_code = 'BG'
ORDER BY p.elevation DESC;

#13. Count Mountain Ranges
SELECT 
    c.country_code, COUNT(mc.mountain_id) AS 'mountain_range'
FROM
    countries AS c
        JOIN
    mountains_countries AS mc ON c.country_code = mc.country_code
GROUP BY c.country_code
HAVING c.country_code IN ('BG' , 'RU', 'US')
ORDER BY mountain_range DESC;

#14. Countries with Rivers
SELECT 
    c.country_name, r.river_name
FROM
    rivers AS r
        RIGHT JOIN
    countries_rivers AS cv ON cv.river_id = r.id
        RIGHT JOIN
    countries AS c ON c.country_code = cv.country_code
WHERE
    c.continent_code = 'AF'
ORDER BY country_name ASC
LIMIT 5;