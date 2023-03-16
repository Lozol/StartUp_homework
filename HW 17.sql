-- 1. Напишіть запит, щоб перерахувати кідбкість вакансій, доступних у таблиці empliyees
-- (Не зовсім зрозуміла завдання, просте перерахування рівне кількості співробітників) 
SELECT  COUNT(JOB_ID) AS VACANCIES FROM employees
;

-- 2. Напишіть запит, щоб отримати середню заробітну плату та кількість працівників відділу 90.
SELECT (AVG(SALARY),2) AS AVG_SALARY, COUNT(EMPLOYEE_ID) AS AMOUNT_STAFF
FROM employees
WHERE DEPARTMENT_ID=90
;
-- 3. Напишіть запит, що отримати кількість працівників з тією самою роботою.
SELECT  JOB_TITLE, COUNT(employees.JOB_ID) as AMOUNT
FROM employees 
JOIN jobs ON employees.JOB_ID=jobs.JOB_ID
GROUP BY employees.JOB_ID
;
-- 4. Напишіть запит, щоб знайти (ім'я, прізвище), код відділу та імена всіх співробітників.
SELECT FIRST_NAME, LAST_NAME, em.DEPARTMENT_ID, DEPARTMENT_NAME
FROM employees  em JOIN departments  dp ON em.DEPARTMENT_ID=dp.DEPARTMENT_ID
ORDER BY FIRST_NAME
;
-- 5. Напишіть запит , щоб знайти ім'я (ім'я та призвище), роботу, ідентифікатор відділу  
-- та імена співробітників, які працюють в Лондоні.
SELECT FIRST_NAME, LAST_NAME, JOB_ID, em.DEPARTMENT_ID, DEPARTMENT_NAME
FROM employees  em JOIN departments  dp ON em.DEPARTMENT_ID=dp.DEPARTMENT_ID
JOIN locations  lc ON dp.LOCATION_ID=lc.LOCATION_ID
WHERE CITY= 'London'
;
