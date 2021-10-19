-- Выбрать подкатегории
select
  value
from
  json_tree(readfile('industry.sample.json'))
where
  fullkey like '$[%].industries[%].name'
;
-- or
select
  json_extract(value, '$.id') as id,
  json_extract(value, '$.name') as name
from
  json_tree(readfile('industry.sample.json'))
where
  path like '$[%].industries'
;


-- Селектор родителя
select
  json_extract(value, '$.id') as id,
  json_extract(value, '$.name') as name
from
  json_tree(readfile('industry.sample.json'))
where
  path like '$[%].industries'
;

-- Фильтруем отрасли второго уровня по отраслям первого уровня
with industries as (select * from json_each(readfile('industry.json'))),
subindustries as (
	select fullkey || '.industries' as key
	from industries
	where json_extract(value, '$.id') in ('7', '24', '388')
)
select
	count(*) as subindustries_count
from
	json_tree(readfile('industry.json'))
where
	path in subindustries
;
-- or
with industries as (select * from json_tree(readfile('industry.json'))),
subindustries as (
	select path || '.industries' as key
	from industries
	where fullkey like '$[%].id'
		and fullkey not like '$[%].industries[%].id'
		and value in ('7', '24', '388')
)
select
	count(*) as subindustries_count
from
	industries
where
	path in subindustries
;

-- Выбираем все отрасли
with data as (select * from json_tree(readfile('industry.json'))),
industries as (
	select
		json_extract(value, '$.id')  as id,
		json_extract(value, '$.name')  as name
	from data
	where
		fullkey like '$[%]'
		and (path = '$' or path like '$[%].industries')
		-- or: type = "object"
)
select id, name
from industries
order by length(name) desc
limit 1
;