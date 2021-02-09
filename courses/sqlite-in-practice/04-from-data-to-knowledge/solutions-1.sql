-- Показатели средней оценки книги
select
  sum(case when average_rating is null then 1 else 0 end) as nulls,
  sum(case when average_rating = 0 then 1 else 0 end) as zeros,
  min(average_rating) as min,
  round(avg(average_rating), 2) as mean,
  max(average_rating) as max,
  count(distinct average_rating) as uniq
from books
;