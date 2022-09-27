insert into sales_person (name) values ('Gabriel'), ('Natalia'), ('Daniel');

insert into item (name, price) values ('Corolla', 25000), ('Civic', 26000), ('CR-V', 30000), ('RAV4', 32000), ('Focus', 23000);

select sp.id, sp.name 
from sales_person sp;

call get_all_sales_person();

select i.id, i.name, i.price 
from item i;

call get_all_items();