--
-- @lc app=leetcode id=196 lang=mysql
--
-- [196] Delete Duplicate Emails
--

-- @lc code=start
# Write your MySQL query statement below
delete from Person where not Id in (
    select t.Id from (
        select min(Id) as Id from Person group by Email
    ) as t
)
-- @lc code=end

