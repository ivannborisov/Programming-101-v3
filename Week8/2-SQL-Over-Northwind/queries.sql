SELECT FirstName, LastName, Title
FROM Employees


SELECT FirstName, LastName, Title
FROM Employees
WHERE City = 'Seattle'


SELECT FirstName, LastName, Title
FROM Employees
WHERE City = 'London'


SELECT FirstName, LastName, Title
FROM Employees
WHERE Title LIKE '%Sales%'


SELECT FirstName, LastName, Title, TitleOfCourtesy
FROM Employees
WHERE Title LIKE '%Sales%'
AND TitleOfCourtesy LIKE '%s%'


SELECT FirstName, LastName, BirthDate
FROM Employees
ORDER BY BirthDate ASC
LIMIT 5


SELECT FirstName, LastName, HireDate
FROM Employees
ORDER BY HireDate
LIMIT 5


SELECT FirstName, LastName, ReportsTo
FROM Employees
WHERE ReportsTo IS NULL


SELECT e.FirstName, e.LastName, e.ReportsTo, managers.FirstName, managers.LastName
FROM Employees AS e
JOIN Employees AS managers
ON e.ReportsTo = managers.EmployeeID


SELECT COUNT(EmployeeID)
FROM Employees
WHERE TitleOfCourtesy
IN ('Ms.', 'Mrs.')


SELECT COUNT(EmployeeID)
FROM Employees
WHERE TitleOfCourtesy NOT LIKE '%s%'


SELECT City, COUNT(City)
FROM Employees
GROUP BY City


SELECT FirstName, LastName, OrderID
FROM Employees
JOIN Orders
ON Orders.EmployeeID = Employees.EmployeeID


SELECT OrderID, CompanyName
FROM Orders
JOIN Shippers
ON ShipVia = ShipperID


SELECT ShipCountry, COUNT(OrderID) AS OrdersNumbers
FROM Orders
GROUP BY ShipCountry


SELECT Orders.EmployeeID, FirstName, LastName, COUNT(OrderID) AS order_count
FROM Orders
JOIN Employees
ON Employees.EmployeeID = Orders.EmployeeID
GROUP BY Employees.EmployeeID
ORDER BY order_count DESC
LIMIT 1


SELECT Orders.CustomerID, COUNT(*) AS order_count, CompanyName
FROM Orders
JOIN Customers
ON Customers.CustomerID = Orders.CUstomerID
GROUP BY Customers.CustomerID
ORDER BY order_count DESC
LIMIT 1


SELECT Employees.EmployeeId, FirstName, LastName, Orders.ShipName, Customers.CompanyName
FROM Orders
JOIN Customers
ON Customers.CustomerID = Orders.CUstomerID
JOIN Employees
ON Employees.EmployeeID = Orders.EmployeeID


SELECT Customers.CompanyName AS Customer, Shippers.CompanyName AS Shipper
FROM Customers
JOIN Orders
ON Customers.CustomerID = Orders.CUstomerID
JOIN Shippers
ON ShipperID = ShipVia