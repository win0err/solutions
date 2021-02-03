-- Большие работодатели в регионах
select
  area.name,
  count(employer.id) as employer_count    
from 
  employer
  join employer_area on employer_id = employer.id
  join area on area.id = area_id
where 
  open_vacancies >= 10
group by area.id
order by employer_count     desc
limit 10
;

-- Связка между работодателем и метро
create table employer_metro as
select distinct 
  employer_id, 
  metro_station_id
from vacancy
where
  employer_id is not null
  and metro_station_id is not null
;
-- alternative
create table employer_metro(
  employer_id int, 
  metro_station_id text
);
create unique index idx_employer_metro_station
on employer_metro(employer_id, metro_station_id);
insert into employer_metro
select distinct 
  employer_id, 
  metro_station_id
from vacancy
where
  employer_id is not null
  and metro_station_id is not null
;

-- Топ станций метро по работодателям
select
  metro.name as station,
  count(distinct employer_id) as employer_count
from vacancy
join metro on vacancy.metro_station_id = metro.id
group by metro_name
order by 2 desc
limit 3
;