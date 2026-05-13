-- Query1
SELECT countries.name, languages.language, languages.percentage
FROM countries
JOIN languages ON countries.id = languages.country_id
WHERE languages.language = 'Slovene'
ORDER BY languages.percentage DESC;

-- Query2
SELECT countries.name, COUNT(*) AS total_cities
FROM countries
JOIN cities ON countries.id = cities.country_id
GROUP BY countries.name
ORDER BY total_cities DESC;

-- Query3
SELECT cities.name, cities.population
FROM cities
JOIN countries ON cities.country_id = countries.id
WHERE countries.name = 'Mexico' AND cities.population > 500000
ORDER BY cities.population DESC;

-- Query4
SELECT countries.name , languages.language ,languages.percentage
FROM countries
JOIN languages ON countries.id =languages.country_id
WHERE languages.percentage > .89
order by languages.percentage desc;

-- Query5
SELECT countries.name , countries.surface_area , countries.population
FROM countries
WHERE countries.surface_area <501 AND countries.population >100000;

-- Query6
SELECT name, government_form, capital, life_expectancy
FROM countries
WHERE government_form = 'Constitutional Monarchy' AND capital > 200
      AND life_expectancy > 75;
      
-- Query7
SELECT countries.name, cities.name, cities.district, cities.population
FROM countries
JOIN cities ON countries.id = cities.country_id
WHERE countries.name = 'Argentina'
  AND cities.district = 'Buenos Aires'
  AND cities.population > 500000;      
      
-- Query8
SELECT region, COUNT(*) AS num_countries
FROM countries
GROUP BY region
ORDER BY num_countries DESC;

