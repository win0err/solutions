create table words (word text, pos text, freq real);

select count(word) from words where length(word) = 3 and word like '%т';
-- or
select count(word) from words where word like '__т';

with zwords as (
  select
    word,
    freq
  from words
  where
    word glob 'з[^а]*'
  order by freq desc
  limit 2
)
select word
from zwords
order by freq asc
limit 1
;

with avg_freq as (
  select
    round(avg(freq)) as N
  from words
),
statistics as (
  select
    word,
    iif(freq < N, 'rare', 'frequent') as popularity
  from
    words,
    avg_freq
)
select
  count(*) as count
from statistics
where
  word like 'я%'
  and popularity = 'frequent'
;
