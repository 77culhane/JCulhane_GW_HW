DROP TABLE IF EXISTS alter_update01;
DROP TABLE IF EXISTS annual_salary;

CREATE TABLE alter_update01 (
	employee_id int,
	first_name varchar(255),
	last_name varchar(255),
	department_id int
);

INSERT INTO alter_update01 (employee_id, first_name, last_name, department_id)
VALUES (3, 'Chris', 'Christian', 25),
     (14, 'Jan', 'Jansson', 45),
	 (17, 'Sam', 'Samuels', 45);

ALTER TABLE alter_update01
RENAME COLUMN department_id to dept_id;

CREATE TABLE annual_salary (
    employee_id SERIAL PRIMARY KEY NOT NULL
    ,annual_salary DEC
);

INSERT INTO annual_salary
(annual_salary)
(
SELECT DISTINCT employee_id FROM alter_update01
);

ALTER TABLE alter_update01
ADD annual_salary INT;

SELECT * FROM alter_update01