-- Part 2. create `all_parties` view --
drop view if exists actor_view;
Create View actor_view as
(select actor.first_name, actor.last_name, 'actor' as party
from actor);
select * from actor_view

drop view if exists customer_view;
Create View customer_view as
(select customer.first_name, customer.last_name, 'customer' as party
from customer);
select * from customer_view

drop view if exists staff_view;
Create View staff_view as
(select staff.first_name, staff.last_name, 'staff' as party
from staff);
select * from staff

SELECT first_name, last_name, party FROM actor_view
UNION
SELECT first_name, last_name, party FROM customer_view
UNION
SELECT first_name, last_name, party FROM staff_view
ORDER BY last_name;

-- Part 3. create `Union` from `customer` and `customer list`
--3.1 Create view attaching Country Name to City Name (there is also a London, Ontario with the same city_id)
Create View londonengland as
(SELECT country.country_id, country.country, city.city_id, city.city
FROM country
INNER JOIN city ON country.country_id=city.country_id);

--3.2 Create view attaching City Name to Address
Create View londonaddress as
(SELECT address.address, address.address_id, londonengland.country_id, londonengland.country, londonengland.city_id, londonengland.city
FROM londonengland
INNER JOIN address ON londonengland.city_id=address.city_id);

-- 3.3 Create view attaching address to customer from customer list by address
Create View londoncustomer_list as
(SELECT customer_list.name, londonaddress.address, londonaddress.address_id, londonaddress.country_id, londonaddress.country, londonaddress.city_id, londonaddress.city
FROM londonaddress
INNER JOIN customer_list ON londonaddress.address=customer_list.address
Where londonaddress.country='United Kingdom');

-- 3.4 Create view attaching address to customer from customer by address_id
Create View londoncustomer as
(SELECT customer.first_name, customer.last_name, londonaddress.address, londonaddress.address_id, londonaddress.country_id, londonaddress.country, londonaddress.city_id, londonaddress.city
FROM londonaddress
INNER JOIN customer ON londonaddress.address_id=customer.address_id
Where londonaddress.country='United Kingdom');

--3.5 Drop id columns from londoncustomer_list table (no longer necessary)
create view customer_listcleaned as 
(SELECT londoncustomer_list.name, londoncustomer_list.address, londoncustomer_list.city, londoncustomer_list.country
FROM londoncustomer_list
Where city='London');

--3.6 Drop id columns from londoncustomer table (no longer necessary)
create view customercleaned as 
(SELECT londoncustomer.first_name, londoncustomer.last_name, londoncustomer.address, londoncustomer.city, londoncustomer.country
FROM londoncustomer
Where city='London');

SELECT address, city, country FROM customer_listcleaned
UNION ALL
SELECT address, city, country FROM customercleaned
ORDER BY city;

-- Both customers and customer_list have the same number of London customers --