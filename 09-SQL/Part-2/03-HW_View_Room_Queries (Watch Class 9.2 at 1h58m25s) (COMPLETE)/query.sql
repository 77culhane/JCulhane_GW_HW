--finished code--
drop view if exists title_count;

CREATE VIEW title_count AS
SELECT film_id, title,
(SELECT COUNT(inventory.film_id)
	FROM inventory
	WHERE film.film_id = inventory.film_id )
FROM film;

SELECT * FROM title_count
WHERE title_count.count=7

-- initial difficulty with subqueries; attempted using join -- 
drop view if exists title_count;
drop view if exists counter;

create view counter as
(SELECT film_id, COUNT(*) 
FROM inventory 
GROUP BY film_id);

CREATE VIEW title_count AS
(SELECT film.film_id, film.title, counter.count
FROM film
INNER JOIN counter ON film.film_id=counter.film_id);

SELECT * FROM title_count
WHERE title_count.count=7