-- dsiplay top 3 cities temp during sme months
SELECT city, AVG(value) AS "avg_temp"
FROM temperatures
WHERE month = 7 || month = 8
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
