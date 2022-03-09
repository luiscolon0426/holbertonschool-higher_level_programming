-- dsiplay top 3 cities temp during sme months
SELECT city, AVG(value) AS "avg_temp"
FROM temperatures
WHERE month = 6 || month = 7
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
