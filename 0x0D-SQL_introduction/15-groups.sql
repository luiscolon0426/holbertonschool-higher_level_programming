-- list all the numbers of records/row with the same
-- score in the table
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score ORDER BY number DESC
