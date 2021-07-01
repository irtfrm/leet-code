--
-- @lc app=leetcode id=197 lang=mysql
--
-- [197] Rising Temperature
--

-- @lc code=start
# Write your MySQL query statement below
select Id from
(SELECT Id, Temperature,
datediff(recordDate, LAG(recordDate) over (order by recordDate)) as diff,
LAG(Temperature) over (order by recordDate) as prev
FROM Weather
) as T
where prev < Temperature and diff=1
-- @lc code=end

