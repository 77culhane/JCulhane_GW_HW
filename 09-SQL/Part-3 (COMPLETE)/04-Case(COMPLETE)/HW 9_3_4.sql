DROP TABLE IF EXISTS Disney;

CREATE TABLE Disney (
    id int,
    animal_name varchar(255),
    species varchar(255)
);

INSERT INTO Disney (id, animal_name, species)
VALUES (1, 'Mickey Mouse', 'duck'),
  (2, 'Minnie Mouse', 'duck'),
  (3, 'Donald Duck', 'mouse');

SELECT
CASE
    WHEN species = 'duck' THEN 'mouse'
    WHEN species = 'mouse' THEN 'duck'
END AS species, animal_name, id
FROM Disney
WHERE species IN ('duck','mouse');
