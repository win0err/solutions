-- Знакомство с таблицей area
select name 
from area 
where parent_id = 2235 
order by 1 asc 
limit 3
;


create table if not exists address as
select
  coalesce(city.id, region.id, country.id) as id,
  country.name as country,
  region.name as region,
  city.name as city
from area as country
  left join area as region on country.id = region.parent_id
  left join area as city on region.id = city.parent_id
where
  country.parent_id is null
;

-- Группируем вакансии по областям
select 
  address.region,
  count(*) as vacancy_count
from vacancy
join address on area_id = address.id
where 
  address.country = "Россия"
group by 1
order by 2 desc
limit 3
; 

-- Разворачиваем иерархию метро
select 
  city,
  count(*) as stations_count
from (
  select 
    cities.name as city, 
    lines.name as line,
    stations.name as station
  from metro cities
  join metro lines on lines.parent_id = cities.id
  join metro stations on stations.parent_id = lines.id
    where cities.parent_id is null
)
group by city
order by stations_count desc
limit 5
;

-- Рекурсивный обход метро
with recursive tmp(id, name, level) as (
  select id, name, 1 as level
  from metro
  where parent_id is null

  union all

  select
    metro.id,
    tmp.name || ', ' || metro.name as name,
    tmp.level + 1 as level
  from metro
    join tmp on metro.parent_id = tmp.id 
)
select name 
from tmp
where id = 48.265 
;