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