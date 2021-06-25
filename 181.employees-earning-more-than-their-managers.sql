--
-- @lc app=leetcode id=181 lang=mysql
--
-- [181] Employees Earning More Than Their Managers
--

-- @lc code=start
# Write your MySQL query statement below
select emp1.Name as Employee from Employee as emp1
inner join Employee as emp2 on emp1.ManagerId=emp2.Id
where emp1.Salary > emp2.Salary
-- @lc code=end

