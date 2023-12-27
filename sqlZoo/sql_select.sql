/*
Modify it to show the population of Germany
*/

SELECT population FROM world
WHERE name = 'Germany'

/*
Checking a list The word IN allows us to check if an item is in a list. The example shows the name and population for the countries 'Brazil', 'Russia', 'India' and 'China'.
Show the name and the population for 'Sweden', 'Norway' and 'Denmark'.
*/

SELECT name, population FROM world
WHERE name IN('Sweden', 'Norway', 'Denmark');

/*
Which countries are not too small and not too big? BETWEEN allows range checking 
(range specified is inclusive of boundary values). The example below shows countries with an area of 250,000-300,000 sq. km.
Modify it to show the country and the area for countries with an area between 200,000 and 250,000.
*/

SELECT name, area FROM world
WHERE area BETWEEN 200000 AND 250000;

/* QUIZ */

SELECT name, population
  FROM world
 WHERE population BETWEEN 1000000 AND 1250000;

SELECT name, population
FROM world
WHERE name LIKE "Al%";

-- 3. Select the code which shows the countries that end in A or L

SELECT name FROM world
WHERE name LIKE '%a' OR name LIKE '%l';

SELECT name,length(name)
FROM world
WHERE length(name)=5 and region='Europe'

-- 6. Select the code that would show the countries with an area larger than 50000 and a population smaller than 10000000
SELECT name, area, population
  FROM world
 WHERE area > 50000 AND population < 10000000

--  7. Select the code that shows the population density of China, Australia, Nigeria and France
SELECT name, population/area
  FROM world
 WHERE name IN ('China', 'Nigeria', 'France', 'Australia')