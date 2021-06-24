--
-- @lc app=leetcode id=176 lang=mysql
--
-- [176] Second Highest Salary
--

-- @lc code=start
# Write your MySQL query statement below
select
(
    select
        MAX(Employee.Salary) as SecondHighestSalary
    from
    (
        select
            Salary
            , rank() over(ORDER BY Salary DESC) as salary_rank
        from 
            Employee
    ) as Employee
    where
        Employee.salary_rank=2
    group BY
        salary_rank
) as SecondHighestSalary
from dual


-- @lc code=end

