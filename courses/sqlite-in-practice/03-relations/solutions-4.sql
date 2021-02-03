-- Топ вакансий из разных городов
with moscow as (
  select id
  from vacancy
  where 
        area_id = 1 
    and salary_currency = 'RUR'
  order by salary_from desc
  limit 3
),

vladivostok as (
  select id
  from vacancy
  where 
        area_id = 22 
    and salary_currency = 'RUR'
  order by salary_from desc
  limit 3
)

select id from moscow
union
select id from vladivostok

order by id
;

-- Топовые работодатели Москвы и Санкт-Петербурга
with msk as (
  select employer_id 
  from vacancy 
  where 
        area_id = 1
    and salary_currency = 'RUR' 
  order by salary_from desc 
  limit 20
),
spb as (
  select employer_id 
  from vacancy 
  where 
        area_id = 2
    and salary_currency = 'RUR' 
  order by salary_from desc 
  limit 20
)

select employer_id from msk
intersect
select employer_id from spb

order by employer_id
limit 1
;

-- Топовые работодатели Москвы, но не Санкт-Петербурга
with msk as (
  select employer_id 
  from vacancy 
  where 
        area_id = 1
    and salary_currency = 'RUR' 
  order by salary_from desc 
  limit 10
),
spb as (
  select employer_id 
  from vacancy 
  where 
        area_id = 2
    and salary_currency = 'RUR' 
  order by salary_from desc 
  limit 10
)

select employer_id from msk
except
select employer_id from spb

order by employer_id
limit 3
;