-- Вычисляемый столбец с названием вакансии
alter table vacancy
add column name_30 text as (substr(name, 1, 30))
;

-- Представление вакансий
create view v_vacancy as
select 
  vacancy.id,
  case 
    when vacancy.name like '%(%' then
      substr(vacancy.name, 1, instr(vacancy.name, '(')-2)
    else vacancy.name
  end as short_name,
  employer.name as employer,
  area.name as area,
  cast(salary_from / currency.rate as integer) as salary
from vacancy
join currency on vacancy.salary_currency = currency.code
join employer on vacancy.employer_id = employer.id
join area on vacancy.area_id = area.id
;

-- Временная таблица с адресами России
create temporary table russia as
select * from address
where country = 'Россия'
;