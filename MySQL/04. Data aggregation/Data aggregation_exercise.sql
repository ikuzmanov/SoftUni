#1. Records’ Count
SELECT COUNT(id) AS 'count' FROM wizzard_deposits;

#2.	 Longest Magic Wand
SELECT MAX(magic_wand_size) AS 'longest_magic_wand' FROM wizzard_deposits;

#3. Longest Magic Wand Per Deposit Groups
SELECT deposit_group, MAX(magic_wand_size) AS 'longest_magic_wand' FROM wizzard_deposits
GROUP BY deposit_group
ORDER BY  longest_magic_wand ASC, deposit_group ASC;

#4. Smallest Deposit Group Per Magic Wand Size
SELECT deposit_group FROM wizzard_deposits
GROUP BY deposit_group
ORDER BY AVG(magic_wand_size)
LIMIT 1;

#5.	 Deposits Sum
SELECT deposit_group, SUM(deposit_amount) AS 'total_sum' FROM wizzard_deposits
GROUP BY deposit_group
ORDER BY SUM(deposit_amount) ASC;

#6. Deposits Sum for Ollivander Family
SELECT deposit_group, SUM(deposit_amount) AS 'total_sum' FROM wizzard_deposits
WHERE magic_wand_creator = 'Ollivander family'
GROUP BY deposit_group
ORDER BY deposit_group ASC;

#7. Deposits Filter
SELECT deposit_group, SUM(deposit_amount) AS 'total_sum' FROM wizzard_deposits
WHERE magic_wand_creator = 'Ollivander family'
GROUP BY deposit_group
HAVING total_sum < 150000
ORDER BY total_sum DESC;

#8. Deposit Charge
SELECT deposit_group, magic_wand_creator, MIN(deposit_charge) AS 'min_deposit_charge' FROM wizzard_deposits
GROUP BY deposit_group, magic_wand_creator
ORDER BY magic_wand_creator, deposit_group ASC;

#9. Age Groups
SELECT 
    CASE
        WHEN age <= 10 THEN '[0-10]'
        WHEN age <= 20 THEN '[11-20]'
        WHEN age <= 30 THEN '[21-30]'
        WHEN age <= 40 THEN '[31-40]'
        WHEN age <= 50 THEN '[41-50]'
        WHEN age <= 60 THEN '[51-60]'
        ELSE '[61+]'
    END AS 'age_group',
    COUNT(*) AS 'wizard_count'
FROM
    wizzard_deposits
GROUP BY age_group
ORDER BY wizard_count;
        