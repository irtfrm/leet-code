--
-- @lc app=leetcode id=182 lang=mysql
--
-- [182] Duplicate Emails
--

-- @lc code=start
# Write your MySQL query statement below
select p.Email
from
(select p.Email, count(p.id) as cnt from Person as p group by p.Email) as p
where p.cnt > 1
-- @lc code=end

