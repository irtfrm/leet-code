--
-- @lc app=leetcode id=175 lang=mysql
--
-- [175] Combine Two Tables
--

-- @lc code=start
# Write your MySQL query statement below
select
    person.FirstName,
    person.LastName,
    address.City,
    address.State
from
    Person as person
    left outer join
        Address as address
    on
        person.PersonId = address.PersonId

-- @lc code=end

