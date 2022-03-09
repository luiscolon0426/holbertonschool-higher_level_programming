-- script that lists all citiee in database
SELECT cities.id,
    cities.namem states.name
FROM cities
    INNER JOIN states ON cities.states_id = states.id
ORDER BY cities.id;