-- list all cities of California that can be found in database
SELECT id, name
FROM cities
WHERE state_id = (
        SELECT id
        FROM states
        WHERE name = "California"
    )
ORDER BY cities.id;
