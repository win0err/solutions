select
  publication_date
from books
where
  publication_date between '2005-01-01' and '2005-12-31'
order by 1 desc
limit 1
;

-- Author's solution:
select
  max(publication_date)
from books
where
  publication_date <= '2005-12-31'
;

select
  book_id
from books
where
  publication_date = date('2005-09-01', '+21 days', 'weekday 4')
;


