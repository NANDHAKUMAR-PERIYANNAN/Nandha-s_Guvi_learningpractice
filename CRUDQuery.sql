#structural query
CREATE DATABASE student;
CREATE DATABASE employee;

USE student;
CREATE TABLE student_info(id INT,f_name VARCHAR(20),age INT);
#Value assessing query
INSERT INTO student_info(id, f_name, age)
VALUES(101,"nandha",21),(102,"kumar",22),
(103,"chutti",20);

SELECT id FROM student_info;
#filter by where
SELECT * FROM student_info WHERE id = 101 and f_name="nandha";
#delete table row by where
DELETE FROM student_info  WHERE id in (103,101);
#truncate
TRUNCATE TABLE student_info;
#drop by using alter
SELECT * FROM student_info;
ALTER TABLE student_info DROP column age;
#drop all column in table
DROP TABLE student_info;
#update values
UPDATE student_info SET id=104 where id in(101,102);
Delete from student_info where id =104;
SELECT * FROM student_info;
#sorting by order
SELECT *FROM student_info
ORDER BY age ASC;
#groupby
