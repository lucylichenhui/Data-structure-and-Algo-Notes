# Write your MySQL query statement below


"""
# you want the final table to have 2 cols, customer id and count no trans
"""

select customer_id, count(*) as count_no_trans 
from visits
left join transactions on visits.visit_id = transactions.visit_id
where transaction_id is null
group by customer_id

"""
# Write your MySQL query statement below
"""

select name, sum(transactions.amount) as balance
from users
left join transactions on transactions.account=users.account 
group by transactions.account
having sum(transactions.amount)>10000


select name, sum(transactions.amount) as balance
from users
left join transactions on users.account = transactions.account
group by transactions.account
having sum(transactions.amount) > 10000

select seller_id
from sales 
where sum(sales.price)

WITH cte AS # must store temporary result in table called cte
(SELECT seller_id, SUM(price) total_price
FROM Sales
GROUP BY seller_id)

SELECT seller_id
FROM cte
WHERE total_price IN (SELECT MAX(total_price) FROM cte)

"""
# Write your MySQL query statement below
"""

WITH cte AS 
(Select seller_id, SUM(price) tprice
FROM sales
group by seller_id)

Select seller_id
from cte
WHERE tprice in (select max(tprice) From cte)

"""
# Write your MySQL query statement below
"""
SELECT id, name
FROM students 
join departments on departments.id=students.department_id
where departments.id is null

Select a.id, a.name from students a
left join departments b
on a.department_id = b.id
where b.id is null

https://leetcode.com/problems/students-with-invalid-departments/submissions/

select id, name from students where department_id not in (select id from Departments)

https://leetcode.com/problems/students-with-invalid-departments/submissions/

SELECT a.id, a.name FROM students a
left join departments on a.department_id=departments.id
where departments.id is null

https://leetcode.com/problems/warehouse-manager/

SELECT name AS WAREHOUSE_NAME, SUM(calc) AS VOLUME 

"""
rename warehouse name as name 
"""

FROM
(
SELECT a.name, a.product_id, units * widthheightlength AS calc
FROM Warehouse a
INNER JOIN products b
ON a.product_id = b.product_id
)a
GROUP BY name

"""
need to group by name
"""

"""
A subquery is a query that is nested inside a SELECT, INSERT, UPDATE, or DELETE statement, or inside another subquery. 

"""


From 
(
    select product, id,width*length*height as vol from products
)a


select w.name as warehouse_name, SUM(p.width*p.length*p.height) as vol
from Warehouse w Products p
where p.product_id=w.product_id
group by warehouse_name



select w.name as warehouse_name, SUM(p.width*p.length*p.height) as vol
from Warehouse w, Products p
where p.product_id=w.product_id
group by warehouse_name


SELECT w.name AS Warehouse_Name, SUM(w.units* p.width * p.length * p.height) AS volume
FROM warehouse w, products p 
WHERE p.product_id = w.product_id 
GROUP BY w.name

"""
https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/
left join
"""

# Write your MySQL query statement below
select em.unique_id, employees.name
from EmployeeUNI em
right join employees on employees.id=em.id

"""
https://leetcode.com/problems/find-the-team-size/

Key: you can create 
"""

SELECT d1.employee_id, d2.team_size
FROM Employee d1 LEFT JOIN 
(SELECT team_id, COUNT(team_id) AS team_size
FROM Employee 
GROUP BY team_id) d2
ON d1.team_id = d2.team_id

"""
https://leetcode.com/problems/unpopular-books/
"""

select t2.book_id, t2.quantity, t2.dispatch_date
from orders t2 left join 
(select t1.book_id, t1.name
from books)t3
group by book_id
on t2.book_id=t3.book_id
WHERE t2.dispatch_date netween (select max(tprice) From cte)
 
"""
SQL regex like vocabulary
"""
Select patient_id, patient_name, conditions from 
Patients where regexp_like(conditions,' *DIAB1')

"""
SQL delete
"""
delete from customers where customername="somename"

"""
SQL select top n
"""

SELECT TOP 3 * FROM Customers
WHERE Country='Germany';

"""
https://leetcode.com/problems/friend-requests-ii-who-has-the-most-friends/
"""

from request_accepted
select requester_id, accepter_id
group by requester_id


# Write your MySQL query statement below

select t1.requester_id id, SUM(t1.id1+t2.id2)
from(select requester_id, COUNT(requester_id) id1
from request_accepted
group by requester_id)t1 
,(select accepter_id, COUNT(accepter_id) id2
from accepter_id
group by accepter_id)t2 
on t1.requester_id=t2.accepter_id




select t1.requester_id id, SUM(t1.id1+t2.id2)
from(select requester_id, COUNT(requester_id) id1
from request_accepted
group by requester_id)t1 
,(select accepter_id, COUNT(accepter_id) id2
from accepter_id
group by accepter_id)t2 
on t1.id1=t2.id2

select t1.requester_id id, t1.id1+t2.id2
from(select requester_id, COUNT(requester_id) id1 from request_accepted group by requester_id)t1 
,(select accepter_id, COUNT(accepter_id) id2
from accepter_id
group by accepter_id)t2 
on t1.id1=t2.id2


select friend,max(cnt)
from (
select friend,count(friend) cnt
From (
select requester_id as friend 
from request_accepted
union all
select accepter_id as friend
from request_accepted)t
group by friend
)


select friend,cnt
from (
select friend,count(friend) cnt
From (
select requester_id as friend 
from request_accepted
union all
select accepter_id as friend
from request_accepted)t
group by friend
)t1
order by cnt desc



select friend id,cnt num
from (
select friend,count(friend) cnt
From (
select requester_id as friend 
from request_accepted
union all
select accepter_id as friend
from request_accepted)t
group by friend
)t1
order by cnt desc
limit 1

"""
https://leetcode.com/problems/capital-gainloss/
1393. Capital Gain/Loss
"""

select stock_name, capital_gain_loss
SELECT s.stock_name, s.operation, if(s.operation="Buy",-1*s.price,s.price)
from stocks s

"""
https://leetcode.com/problems/second-highest-salary/
"""

"""

 Write your MySQL query statement below
 rank descending
 Choose secondmax

"""

select max(salary) as secondhighestsalary
from Employee
where salary not in (select max(salary) from employee)

"""
https://leetcode.com/problems/apples-oranges/submissions/
"""

# Write your MySQL query statement below
select sale_date, sum(sold) as diff
from(
    select sale_date, fruit, if(s.fruit="oranges",-1*s.sold_num,s.sold_num) as sold
    from sales s) t
group by sale_date


"""
https://leetcode.com/problems/department-highest-salary/
"""

# Write your MySQL query statement below

select name department, name employee, max(salary) 
from(
select  t1.salary, t1.departmentid, t1.Name
from employee t1 
left join department t2 on t1.departmentid=t2.id
order by salary desc) t3
group by department 


select  employee.salary, employee.departmentid , employee.name as n
from employee 
left join department t2 on employee.departmentid=t2.id
order by salary desc

select name department, n employee, max(salary) 
from(
select  employee.salary, employee.departmentid , employee.name as n, t2.name
from employee 
left join department t2 on employee.departmentid=t2.id
order by salary desc) t3
group by department 


# Write your MySQL query statement below


select name department, n employee, max(salary) 
from(
select  employee.salary, employee.departmentid , employee.name as n, t2.name
from employee 
left join department t2 on employee.departmentid=t2.id
order by salary desc) t3
group by department 




select name department, n employee, max(salary) 
from(
select  employee.salary, employee.departmentid , employee.name as n, t2.name
from employee 
left join department t2 on employee.departmentid=t2.id
order by salary desc) t3
on max(salary) is salary
group by department 

select name department, n employee, max(salary) 
from(
select  employee.salary, employee.departmentid , employee.name as n, t2.name
from employee 
left join department t2 on employee.departmentid=t2.id
order by salary desc) t3
group by department 


"""
Note: max is simply used to return the max of a sequence, not references
"""

select departmentid, name, salary 
from employee join department
on department.id=employee.departmentid 
where (department.id,salary) in (
    select departmentid , max(salary) from employee group by departmentid)


"""
rectified
"""

select  department.name department, employee.name employee, salary 
from employee join department
on department.id=employee.departmentid 
where (department.id,salary) in (
    select departmentid , max(salary) from employee group by departmentid)


# Write your MySQL query statement below


select  en.student_id, en.course_id, en.grade from enrollments en
right join (
select student_id  , max(grade) grade from enrollments group by student_id order by course_id asc) s
on en.student_id=s.student_id and en.grade=s.grade
group by student_id
order by course_id asc, student_id asc


# Write your MySQL query statement below

WITH temporaryTable (averageValue) as
(select  en.student_id, en.course_id, en.grade from enrollments en
order by course_id asc)
select  en.student_id, en.course_id, en.grade
from Table
right join (
select student_id  , max(grade) grade from enrollments group by student_id ) s
on en.student_id=s.student_id and en.grade=s.grade
group by student_id


select  table1.student_id, min(table1.course_id) course_id, table1.grade
from (select  en.student_id, en.course_id, en.grade from enrollments en
order by course_id asc) table1
right join (
select en.student_id  , max(en.grade) grade from enrollments en group by student_id ) s
on table1.student_id=s.student_id and table1.grade=s.grade 
group by table1.student_id
order by table1. student_id asc, table1. student_id asc

"""
https://leetcode.com/problems/nth-highest-salary/

"""


CREATE FUNCTION getNthHighestSalary(N IN NUMBER) RETURN NUMBER IS
result NUMBER;
BEGIN
/* Write your PL/SQL query statement below */
select distinct salary INTO result from(
select salary , dense_rank() over(order by salary desc ) AS RNK
from employee)
where rnk=N;

RETURN result;
END;



"""

1) How manyusers turned the feature on today? 
USER_ID || ACTION||DATE||TIME

"""

select count(distinct user_id) from t1 
where curdate()=date and action="on"


"""
How manyusers have ever turned the feature on?
"""

"""
WUT
"""


SELECT A.DATE, B.USER_ID, B.STATUS
(SELECT GENERATE_SERIES('2018-01-01'::DATE,'2018-09-01'::DATE, '1D')::DATE) TABLEA(DATE)  
LEFT JOIN  
(SELECT * FROM
TABLE  
QUALIFY ROW_NUMBER() OVER (PARTITION BY USER_ID, DATEORDER BY TIME DESC)  =1
) B
ON TABLEA.DATE >= B.DATE
QUALIFY ROW_NUMBER() OVER(PARTITION BY A.DATE, B.USER_IDORDER BY B.DATE DESC) =1

"""
Data:

table1
| date | business_id | action | tool |

table2
| date | business_id | country | industry |

Find top 3 tools most used by business in each industry.

"""


select industry, Count(tool) tools from( 
select t1.business_id, t1.date, t1.tool, t2.industry from table1 t1
left join table2 t2
on t1.business_id=t2.business_id and t1.date=t2.date) t3 
group by industry
order by tool desc
limit 3


"""
https://leetcode.com/problems/friend-requests-i-overall-acceptance-rate/
"""


select count(friend_request.sender_id)/count(request_accepted.requester_id)
from friend_request, request_accepted


cast(your_float_column as decimal(10,2))



# Write your MySQL query statement below
select cast(count(distinct friend_request.*)/count(distinct request_accepted.*) as decimal(10,2) )accept_rate
from friend_request, request_accepted


# Write your MySQL query statement below
select isnull(count((distinct request_accepted.requester_id,accepter_id )/cast(count(distinct friend_request.sender_id, send_to_id ) as decimal(10,2)),0)accept_rate
from friend_request, request_accepted



# Write your MySQL query statement below
select ifnull(count((distinct request_accepted.requester_id,accepter_id )/cast(count(distinct friend_request.sender_id, send_to_id ) as decimal(10,2)),0)accept_rate
from friend_request, request_accepted


# Write your MySQL query statement below
select ifnull(round(count(distinct request_accepted.requester_id,accepter_id )/count( distinct friend_request.sender_id, send_to_id ),2),0) accept_rate

from friend_request, request_accepted



"""IMPORTANT SQL TIME FUNCTION 

"""


SELECT DATEADD(year, 1, '2017/08/25') AS DateAdd;
SELECT DATEDIFF(year, '2017/08/25', '2011/08/25') AS DateDiff;
SELECT DATEFROMPARTS(2018, 10, 31) AS DateFromParts;
SELECT DATENAME(year, '2017/08/25') AS DatePartString;
SELECT GETDATE();

"""

https://stackoverflow.com/questions/249301/simple-random-samples-from-a-sql-database
"""