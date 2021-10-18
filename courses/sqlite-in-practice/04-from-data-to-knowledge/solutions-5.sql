-- Чем популярнее язык, тем выше оценка?
with lang_stats as (
  select 
    language_code,
    count(*) as book_count
  from books
  group by language_code
),
rating_stats as (
  select 
    language_code,
    avg(average_rating) as lang_average_rating
  from books
  where ratings_count >= 10  
  group by language_code
)
select
  (avg(book_count * lang_average_rating) - avg(book_count) * avg(lang_average_rating)) / 
  (stddev_pop(book_count) * stddev_pop(lang_average_rating)) as correlation
from lang_stats
join rating_stats on lang_stats.language_code = rating_stats.language_code
;

-- На каких языках написаны самые высоко оцененные книги?
with rating_stats as (
  select 
    language_code,
    average_rating
  from books
  where ratings_count >= 10  
  order by average_rating desc
  limit 1483/10
)
select count(*) as book_count
from rating_stats 
where language_code = 'jpn'
;

-- Топ-10% издателей выпустили 90% книг?
with publishers as (
  select 
    publisher,
    count(*) as book_count
  from books
  group by 1
  order by 2 desc
  limit 585/10
),
stats as (
  select count(*) as total_book_count
  from books
)
select 
  round(sum(book_count) * 100.0 / total_book_count)
  from publishers, stats
;

-- Короткие названия получают высокую оценку?
with short_stats as (
  select avg(average_rating) as avg_rating
  from books
  where length(title) < 10
  and ratings_count >= 10
),
all_stats as (
  select avg(average_rating) as avg_rating
  from books
  where ratings_count >= 10
)
select
  round(short_stats.avg_rating, 2) as shots_avg_rating,
  round(all_stats.avg_rating, 2) as all_avg_rating,
  round((short_stats.avg_rating - all_stats.avg_rating) * 100.0 / all_stats.avg_rating, 2) as diff
from short_stats, all_stats
;