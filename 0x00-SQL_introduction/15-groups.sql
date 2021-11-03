--  lists the number of records with the same score in the table second_table
SELECT score AS score, COUNT(score) AS number FROM second_table GROUP BY score;
