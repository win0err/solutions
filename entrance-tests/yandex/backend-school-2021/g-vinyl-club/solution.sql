CREATE TABLE musicians ( 
  id INTEGER PRIMARY KEY AUTOINCREMENT, 
  name VARCHAR(20) 
); 
CREATE TABLE labels ( 
  id INTEGER PRIMARY KEY AUTOINCREMENT, 
  name VARCHAR(20) 
); 
CREATE TABLE albums ( 
  id INTEGER PRIMARY KEY AUTOINCREMENT, 
  name VARCHAR(20), 
  rating INTEGER, 
  musician_id INTEGER, 
  label_id INTEGER 
);

INSERT INTO musicians VALUES
  (1, "Петя"),
  (2, "Маша")
;
INSERT INTO labels VALUES
  (1, "Граммофон"),
  (2, "Скрипичный ключ")
;
INSERT INTO albums VALUES
  (1, "Дебютный альбом", 8, 1, 1),
  (2, "Этюды", 10, 2, 1),
  (3, "Осень", 6, 2, 2)
;

-- Solution
SELECT
	musicians.name,
	labels.name,
	albums.name,
	albums.rating
FROM
	albums
JOIN labels ON labels.id = albums.label_id
JOIN musicians ON musicians.id = albums.musician_id
WHERE
  labels.name IN ("Граммофон", "Скрипичный ключ")
  AND albums.rating BETWEEN 5 AND 9
ORDER BY musicians.name
;