# Write your MySQL query statement below

select customer_id, count(*) as count_no_trans # you want the final table to have 2 cols, customer id and count no trans
from visits
left join transactions on visits.visit_id = transactions.visit_id
where transaction_id is null
group by customer_id

# Write your MySQL query statement below

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


# Write your MySQL query statement below


WITH cte AS 
(Select seller_id, SUM(price) tprice
FROM sales
group by seller_id)

Select seller_id
from cte
WHERE tprice in (select max(tprice) From cte)

# Write your MySQL query statement below
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
 
