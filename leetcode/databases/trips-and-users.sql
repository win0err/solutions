pragma foreign_keys = on;

create table if not exists Users (
    Users_Id int,
    Banned text,
    Role text,
    primary key (Users_Id)
);
create table if not exists Trips (
    Id int,
    Client_Id int,
    Driver_Id int,
    City_Id int,
    Status text,
    Request_at text,
    primary key (Id),
    foreign key (Client_Id) references Users (Users_Id),
    foreign key (Driver_Id) references Users (Users_Id)
);

truncate table Users;
insert into Users (Users_Id, Banned, Role) values 
('1', 'No', 'client'), ('2', 'Yes', 'client'), ('3', 'No', 'client'), ('4', 'No', 'client'),
('10', 'No', 'driver'), ('11', 'No', 'driver'), ('12', 'No', 'driver'), ('13', 'No', 'driver');

truncate table Trips;
insert into Trips (Id, Client_Id, Driver_Id, City_Id, Status, Request_at) values 
('1', '1', '10', '1', 'completed', '2013-10-01'), ('2', '2', '11', '1', 'cancelled_by_driver', '2013-10-01'),
('3', '3', '12', '6', 'completed', '2013-10-01'), ('4', '4', '13', '6', 'cancelled_by_client', '2013-10-01'),
('5', '1', '10', '1', 'completed', '2013-10-02'), ('6', '2', '11', '6', 'completed', '2013-10-02'),
('7', '3', '12', '6', 'completed', '2013-10-02'), ('8', '2', '12', '12', 'completed', '2013-10-03'),
('9', '3', '10', '12', 'completed', '2013-10-03'), ('10', '4', '13', '12', 'cancelled_by_driver', '2013-10-03');


with stats as (
  select 
    Request_at, 
    T.Status <> 'completed' as IsCancelled
  from Trips T 
  join Users C on (Client_Id = C.Users_Id and C.Banned = 'No') 
  join Users D on (Driver_Id = D.Users_Id and D.Banned = 'No') 
  where
    Request_at between '2013-10-01' and '2013-10-03'
)
select 
  Request_at as Day,
  Round(
    cast(sum(IsCancelled) as real) / cast(count(*) as real),
    2
  ) as 'Cancellation Rate'
from stats
group by Request_at
;