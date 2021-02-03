-- Вакансии по валютам
select 
  currency.name as currency_name, 
  count(*) as vacancy_count
from vacancy 
join currency 
  on vacancy.salary_currency = currency.code
group by 1 
order by 2 desc
;

-- Доля вакансий с гибким графиком
select
  employer.name as employer_name,
  cast(
    sum(iif(vacancy.schedule_id = 'flexible', 1, 0))
    as real
  ) / cast(
    count(*)
    as real
  ) as flexible_ratio
from vacancy
  join employer on vacancy.employer_id = employer.id
group by employer.id
having count(*) >= 10
order by flexible_ratio desc
limit 5
;
-- alternative
select
  employer.name as employer_name,
  cast(count(*) as real) / open_vacancies as flexible_ratio
from vacancy
  join employer on vacancy.employer_id = employer.id
where
  vacancy.schedule_id = 'flexible'
  and open_vacancies >= 10
group by employer.id
order by flexible_ratio desc
limit 5
;

-- Самые денежные вакансии
select
  employer.name as employer_name,
  vacancy.name as vacancy_name,
  round(
    cast(salary_from as real) / currency.rate,
    2
  ) as salary
from vacancy
  join employer on vacancy.employer_id = employer.id
  join currency on vacancy.salary_currency = currency.code
order by salary desc
limit 5
;