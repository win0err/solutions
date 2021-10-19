-- Напишите селектор, который выберет значение атрибута name.
-- $.name

-- Напишите селектор, который выберет второй элемент массива.
-- $[1]

-- Напишите селектор, который выберет название третьего элемента в списке industries.
-- $[0].industries[2].name

-- Считаем языки. Сколько объектов в массиве?
select count(*) as lines_count
from json_each(readfile('language.json'))
;

-- Считаем языки. У какого языка самое длинное название? Укажите в ответе идентификатор языка.
select
	json_extract(value, '$.id') as lang_id
from json_each(readfile('language.json'))
order by
	length(json_extract(value, '$.name')) desc
limit 1
;
-- or
with language as (
	select
		json_extract(value, '$.id') as id,
		json_extract(value, '$.name') as name
	from json_each(readfile('language.json'))
)
select
	id,
	name,
	length(name) as name_length
from language
order by length(name) desc
limit 1
;

