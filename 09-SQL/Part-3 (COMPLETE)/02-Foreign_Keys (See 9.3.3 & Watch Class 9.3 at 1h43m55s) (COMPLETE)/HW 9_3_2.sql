DROP TABLE IF EXISTS employees;
DROP TABLE IF EXISTS departments;


CREATE TABLE departments (
  id INT PRIMARY KEY,
  dept_name VARCHAR(30) NOT NULL
);

-- Insert data
INSERT INTO departments (id, dept_name)
VALUES
  (45, 'webdev');
  
CREATE TABLE employees (
  employee_id int,
  first_name VARCHAR(30) NOT NULL,
  last_name VARCHAR(30) NOT NULL,
  department_id int,
  FOREIGN KEY (department_id) REFERENCES departments(id)
);

INSERT INTO employees (employee_id, first_name, last_name, department_id)
VALUES
  (14, 'Jan', 'Jansson', 45),
  (17, 'Sam', 'Samuels', 45);

SELECT * FROM employees e
JOIN departments d
ON (e.department_id = d.id)
WHERE e.department_id = 45;