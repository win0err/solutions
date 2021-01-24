create function getNthHighestSalary(N int) returns int
begin
  set n = n-1;
  return (    
      select 
        distinct Salary
    from Employee 
    order by Salary desc
    limit 1 
    offset n
  );
end
;