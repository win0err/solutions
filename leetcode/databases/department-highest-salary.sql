select
  Department.Name as `Department`,
  Employee.Name as `Employee`,
  Salary
from Employee
join Department on Department.Id = Employee.DepartmentId
where 
  (DepartmentId, Salary) in (
    select DepartmentId, max(Salary)
    from Employee
    group by DepartmentId
  )
order by Salary desc
;