-- Query1
SELECT customer.first_name, customer.last_name, 
       customer.email, address.address
FROM customer
INNER JOIN address ON customer.address_id = address.address_id
WHERE address.city_id = 312;

-- Query2
SELECT film.title, film.description, film.release_year,
       film.rating, film.special_features, category.name
FROM film
INNER JOIN film_category ON film.film_id = film_category.film_id
INNER JOIN category ON film_category.category_id = category.category_id
WHERE category.name = 'Comedy';

-- Query3
SELECT actor.actor_id, actor.first_name, actor.last_name,
       film.title, film.description, film.release_year
FROM actor
INNER JOIN film_actor ON actor.actor_id = film_actor.actor_id
INNER JOIN film ON film_actor.film_id = film.film_id
WHERE actor.actor_id = 5;

-- Query4
SELECT customer.first_name, customer.last_name,
       customer.email, address.address
FROM customer
INNER JOIN address ON customer.address_id = address.address_id
WHERE customer.store_id = 1
AND address.city_id IN (1, 42, 312, 459);

-- Query5
SELECT film.title, film.description, film.release_year,
       film.rating, film.special_features
FROM film
INNER JOIN film_actor ON film.film_id = film_actor.film_id
WHERE film.rating = 'G'
AND film.special_features LIKE '%Behind the Scenes%'
AND film_actor.actor_id = 15;

-- Query6
SELECT film.film_id, film.title,
       actor.actor_id, actor.first_name, actor.last_name
FROM film
INNER JOIN film_actor ON film.film_id = film_actor.film_id
INNER JOIN actor ON film_actor.actor_id = actor.actor_id
WHERE film.film_id = 369;

-- Query7
SELECT film.title, film.description, film.release_year,
       film.rating, film.special_features, category.name
FROM film
INNER JOIN film_category ON film.film_id = film_category.film_id
INNER JOIN category ON film_category.category_id = category.category_id
WHERE category.name = 'Drama'
AND film.rental_rate = 2.99;

-- Query8
SELECT film.title, film.description, film.release_year,
       film.rating, film.special_features, category.name,
       actor.first_name, actor.last_name
FROM film
INNER JOIN film_category ON film.film_id = film_category.film_id
INNER JOIN category ON film_category.category_id = category.category_id
INNER JOIN film_actor ON film.film_id = film_actor.film_id
INNER JOIN actor ON film_actor.actor_id = actor.actor_id
WHERE category.name = 'Action'
AND actor.first_name = 'SANDRA'
AND actor.last_name = 'KILMER';