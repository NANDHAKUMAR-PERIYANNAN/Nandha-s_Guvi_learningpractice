USE student;
DROP TABLE books;
CREATE TABLE books(title VARCHAR(10), genre VARCHAR(20), qty INT);
INSERT INTO books (title, genre, qty)
VALUES ("book1","adventure",4),("book2","fantasy",3),
("book3","adventure",7),("book4","fantasy",4);

SELECT * from books;
#groupby by (total-column name) to store 
select genre,SUM(qty) AS total FROM books GROUP BY genre 
having avg(qty)>4;
select genre,avg(qty) AS agr FROM books GROUP BY genre;
#linit
select * from books limit 2 offset 2;
#add column by alter and add
alter table books add isbn varchar(10);

#UPDATE VALUE TO COLUMN
update books set isbn="12e3" where title="book1";
update books set isbn="12e4" where title="book2";
update books set isbn="12e5" where title="book3";
update books set isbn="12e6" where title="book4";

#rename column
alter table books rename column qty to price;
#alter table bools  column price float;
alter table books modify column price float;
#rename tablename
rename table books to bools;
select*from bools; 


