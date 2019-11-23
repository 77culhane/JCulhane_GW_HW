--Part 1:
--The join clauses available in SQL include

--1. Inner Joins pair only those values shared by both tables according to
--   the value on which the join is operated.

--2. Outer Joins, which include both RIGHT OUTER JOINS and LEFT OUTER JOINS,
--   produce an output that includes all values in the RIGHT/LEFT table,
--   respectively, but only include those values from the LEFT/RIGHT
--   table, respectively, that match those rows. Rows that don't match will
--   appear with [null] values wherever the rows fail to match.

--3. Full Joins retain all rows from both tables and match all corresponding
--   rows with one another. Rows that don't match will appear with [null]
--   values wherever the rows fail to match.

--(4). Cartesian Joins, while not using the syntax "JOIN" in their execution,
--     still technically join two tables. Unlike the above examples,
--     Cartesian joins pair 1st/left table values with 2nd/right table values
--     by running a nested loop: looping through all values in the RIGHT
--     for all values in the LEFT table, it outputs a table that pairs
--     all of the RIGHT values to each iteration of the LEFT values.


--PART 2:
--The featured example was executed using a FULL (OUTER) JOIN clause.
--An example is seen at the end of the below code sample.


DROP TABLE IF EXISTS vendor_table;
DROP TABLE IF EXISTS yarn_table;


CREATE TABLE vendor_table (
	id int,
	vendor_name varchar(255),
	vendor_country varchar(255)
);
INSERT INTO vendor_table (id, vendor_name, vendor_country)
VALUES (1, 'Carlton', 'Turkey'),
  (2, 'Cascade Yarns', 'US'),
  (3, 'Debbie Bliss', 'Eng'),
  (4, 'Tahki', 'Greece');

CREATE TABLE yarn_table (
	id int,
	yarn_name varchar(255),
	yarn_type varchar(255),
	grams int,
	color int,
	lot int,
	qty int,
	vendor_id int
);

INSERT INTO yarn_table (id, yarn_name, yarn_type, grams, color, lot, qty, vendor_id)
VALUES (1, 'Merino Supreme', 'Worsted', 50, 8, 76123, 1, 1),
  (2, 'Cartwheel', 'Bulky', 200, 2, 1801, 2, 2),
  (3, 'Palmoa Tweed', 'Super Bulky', 50, 42513, 63978, 2, 3),
  (4, 'Heritage', ' Sock', 100, 5640, 1707058, 1, 2);
  
  
--SELECT
--   id,
--	 vendor_name,
-- 	 vendor_country
--FROM
--   vendor_table

--SELECT
--   id,
--	 yarn_name,
--	 yarn_type,
--	 grams,
--	 color,
--	 lot,
--	 qty,
--	 vendor_id
--FROM
--   yarn_table
	 
SELECT vendor_table.vendor_name, vendor_table.vendor_country, yarn_table.yarn_name, yarn_table.yarn_type
FROM yarn_table
FULL OUTER JOIN vendor_table ON
vendor_table.id=yarn_table.vendor_id;