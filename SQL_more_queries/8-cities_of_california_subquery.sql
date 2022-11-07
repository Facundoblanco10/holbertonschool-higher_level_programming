-- script that lists all the cities of California that can be found in the database hbtn_0d_usa.
-- task8
SELECT cities.id, cities.name
FROM cities, states
WHERE states.name = 'California' AND cities.id = states.id
ORDER BY cities.id ASC
