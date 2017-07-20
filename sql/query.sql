SELECT employee.LastName, employee.DepartmentID, department.DepartmentName 
FROM employee 
INNER JOIN department ON
employee.DepartmentID = department.DepartmentID