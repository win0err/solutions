select 
  score,
  dense_rank() over (w) as `Rank`
from scores
window w as (order by score desc)
order by score desc
;