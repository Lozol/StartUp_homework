-- 1. Напишіть запит, щоб отримати всі відомості про співробітників із таблиці emlpoee
-- упорядковано за іменами за зростанням
SELECT * 
FROM employees
ORDER BY FIRST_NAME
;
-- 2. Напишіть запит, щоб отримати імена (ім'я та призвище), зарплату
-- та податки усіх співробітників (податки розраховується як 15% від зарплати)
SELECT FIRST_NAME, LAST_NAME, SALARY, ROUND(SALARY*0.15,2) AS TAX
FROM employees
ORDER BY FIRST_NAME
;
-- 3. Напишіть запит, щоб отримати загальну суму заробітної плати всіх співробітників.
SELECT SUM(SALARY) AS SALARY_FUND
FROM employees
;
-- 4. Напишіть запит для отримання максимальної та мінімальної зарплати працівників.
SELECT MAX(SALARY) AS MAX_SALARY, MIN(SALARY) AS MIN_SALARY
FROM employees
;
-- 5. Напишіть запит, щоб отимати середню заробітну плату та кількість працівників у таблиці employee.
SELECT ROUND(AVG(SALARY),2) AS AVG_SALARY, COUNT(EMPLOYEE_ID) AS AMOUNT_STAFF
FROM employees
;