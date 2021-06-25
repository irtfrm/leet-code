--
-- @lc app=leetcode id=183 lang=mysql
--
-- [183] Customers Who Never Order
--

-- @lc code=start
# Write your MySQL query statement below
select c.Name as Customers from Customers as c
where not c.Id in (select o.CustomerId from Orders o)
-- @lc code=end

