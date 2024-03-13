create table cus(id int primary key,f_name varchar(20));
create table orders(id int primary key,amount int, 
id int, foreign key (id) references cus(id));
insert into cus values(1,'john'),(2,'robert'),(3,'alias'),(4,'marry'),(5,'deol');
insert into orders values (1,200,4),(2,400,2),(3,800,1);

select*from orders;
select*from cus;

select cus.id, cus.f_name, orders.ord_id, orders.amount
FROM cus left join orders
on cus.id =orders.ord_id;

select cus.id, cus.f_name, orders.ord_id,orders.amount
from cus right join orders
on cus.id =orders.ord_id;

select cus.id, cus.f_name, orders.ord_id,orders.amount
from cus cross join orders;