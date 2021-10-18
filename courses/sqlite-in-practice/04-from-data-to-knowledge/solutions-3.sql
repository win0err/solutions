-- Распределение книг по количеству страниц
select
  (num_pages+1)/100 as slot,
  count(*) as book_count
from books
group by slot
order by slot
;

-- Столбчатая диаграмма
-- select printf('%.5c', '*') as bar; -- 5 - количество звёздочек
with slots as (
  select
    (num_pages+1) / 100 as slot,
    count(*) as book_count
  from books
  group by slot
),
max as (
  select max(book_count) as value
  from slots
)
select
  slot,
  book_count,
  printf('%.' || (book_count * 30 / max.value) || 'c', '*') as bar
from slots, max
order by slot
;

-- Распределение книг по average_rating
select 
  round(average_rating, 1) as rating,
  count(*) as book_count
from books 
where average_rating > 0
group by rating
order by 1
;

-- Столбчатая диаграмма
with ratings as (
    select 
        round(average_rating, 1) as rating,
        count(*) as book_count
    from books 
    where average_rating > 0
    group by rating
    order by 1
),
max as (
    select max(book_count) as value
    from ratings
) 
select
  rating,
  book_count,
  printf('%.' || (book_count * 30 / max.value) || 'c', '*') as bar
from ratings, max
order by rating;


-- Стандартное отклонение оценки книги
with stats as (
  select
    avg(average_rating) as mean,
    stddev(average_rating) as std
  from books
    where average_rating > 0
)
select 
    round(mean - std, 2) as std1_lower_bound,
    round(mean + std, 2) as std1_upper_bound
from stats
;

-- Разброс оценок книг
with stats as (
  select
    avg(average_rating) as mean,
    stddev(average_rating) as std,
    count(*) as total
  from books
    where average_rating > 0
)
select 
  round(count(*) * 100.0 / total, 0) as "books %"
from stats, books
  where average_rating between mean - std and mean + std
;