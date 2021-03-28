with ranked_salaries as (
    select 
        Name as Employee,
        Salary,
        DepartmentId,
        dense_rank() over(partition by DepartmentId order by Salary desc) as `rank` 
    from Employee
)
select 
    Department.Name as Department,
    Employee,
    Salary
from ranked_salaries
join Department on (ranked_salaries.DepartmentId = Department.Id)
where `rank` <= 3
;