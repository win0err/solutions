-- Сколько книг ≤ среднего арифметического
with stats as (
  select
    count(*) as total,
    avg(average_rating) as mean
  from books
)
select
  cast(
    round(count(*) * 100.0 / total) as int
  ) as answer
from books, stats
where average_rating <= mean
;

-- Сколько книг ≤ медианы
with stats as (
  select
    count(*) as total,
    median(average_rating) as median
  from books
)
select
  cast(
    round(count(*) * 100.0 / total) as int
  ) as answer
from books, stats
where average_rating <= median
;

-- Процентили оценки книги
select 
  round(percentile_95(average_rating), 2) as p95 
from books
;

-- Сколько книг ≤ 95-го процентиля
with stats as (
  select 
    count(*) as total,
    percentile_95(average_rating) as p95
  from books
)
select
  cast(
    round(count(*) * 100.0 / total) as int
  ) as answer
from books, stats
where average_rating <= p95
;

-- Сколько книг = моде
with stats as (
  select 
    count(*) as total,
    mode(average_rating) as mode
  from books
)
select
  cast(
    round(count(*) * 100.0 / total) as int
  ) as answer
from books, stats
where average_rating = mode
;