with samara as (
  select
    geo_lat as samara_lat,
    geo_lon as samara_lon
  from city
  where city = 'Самара'
)

select 
	city,
	(
	  (geo_lat - samara_lat) * (geo_lat - samara_lat) 
	  + 
	  (geo_lon - samara_lon) * (geo_lon - samara_lon) 
	) as distance
from city, samara 
group by distance
having distance > 0 
order by distance
limit 3
;
