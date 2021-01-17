update city
set
  population = cast(population as integer)
where
  typeof(population) = 'text'
;

update city
set
  city_type = region_type,
  city = region
where
  city = '' and settlement = ''
;

update city
set
  city_type = settlement_type,
  city = settlement
where
  city = '' and settlement <> ''
;

update city
set foundation_year = NULL
where foundation_year like '%век%'
;

update city
set foundation_year = NULL
where city = 'Евпатория'
;

update city
set
  foundation_year = cast(foundation_year as integer)
where
  typeof(foundation_year) = 'text'
;


