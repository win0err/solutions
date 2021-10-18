
-- Значение         Связаны переменные или нет?
-- ---------------------------------------------------------------
-- от -1 до -0.7    Скорее всего, связаны: когда одна ↑, другая ↓
-- от -0.7 до -0.3  Скорее не связаны, чем связаны
-- от -0.3 до 0.3   Наверняка не связаны
-- от 0.3 до 0.7    Скорее не связаны, чем связаны
-- от 0.7 до 1      Скорее всего, связаны: когда одна ↑, другая ↑

-- Формула:
-- (avg(x*y) - avg(x) * avg(y)) / (stddev_pop(x) * stddev_pop(y))


-- Связь между количеством страниц и количеством оценок
with stats as (
  select
    (avg(num_pages * ratings_count) - avg(num_pages) * avg(ratings_count)) / 
    (stddev_pop(num_pages) * stddev_pop(ratings_count)) as correlation
  from books
  where average_rating > 0
)
select
  round(correlation, 2) as "num pages / avg ratings_count correlation"
from stats
;

-- Связь между количеством оценок и количеством рецензий
with stats as (
  select
    (avg(text_reviews_count * ratings_count) - avg(text_reviews_count) * avg(ratings_count)) / 
    (stddev_pop(text_reviews_count) * stddev_pop(ratings_count)) as correlation
  from books
  where average_rating > 0
)
select
  round(correlation, 2) as "text_reviews_count / avg ratings_count correlation"
from stats
;
