# QueryMind Evaluation Report

Generated on: 2026-07-15 17:54:39

## Performance Summary

| Metric | Value |
| --- | --- |
| **Total Queries** | 50 |
| **Passed** | 42 |
| **Failed** | 8 |
| **Overall Pass Rate** | **84.00%** |
| **Average Latency** | 12.24s |

## Difficulty Breakdown

| Difficulty | Total | Passed | Pass Rate |
| --- | --- | --- | --- |
| Simple | 15 | 14 | 93.33% |
| Medium | 20 | 17 | 85.00% |
| Hard | 15 | 11 | 73.33% |

## Failure Analysis Details

Below are the details of the failed queries. Review them to identify the root cause category: **Ambiguity**, **Join**, **Planner**, or **Prompt**.

### Test ID 5 (Simple)
**Question:** `Show the FirstName, LastName, CompanyName, EmailAddress, and Phone of the customer named Orlando Gee`

**Failure Reason:** *Row count mismatch (Expected: 2, Actual: 0)*

**Expected SQL:**
```sql
SELECT FirstName, LastName, CompanyName, EmailAddress, Phone FROM Customer WHERE FirstName = 'Orlando' AND LastName = 'Gee';
```

**Generated SQL:**
```sql
SELECT FirstName, LastName, CompanyName, EmailAddress, Phone
FROM Customer
WHERE Title = 'Mr.' AND FirstName = 'Orlando' AND Suffix = 'Gee'
LIMIT 20;
```

**Expected Row Count:** 2 | **Actual Row Count:** 0

---

### Test ID 22 (Medium)
**Question:** `Find the AddressLine1, City, and StateProvince of all customer addresses for the customer named Orlando Gee`

**Failure Reason:** *Data content mismatch*

**Expected SQL:**
```sql
SELECT a.AddressLine1, a.City, a.StateProvince FROM Customer c JOIN CustomerAddress ca ON c.CustomerID = ca.CustomerID JOIN Address a ON ca.AddressID = a.AddressID WHERE c.FirstName = 'Orlando' AND c.LastName = 'Gee';
```

**Generated SQL:**
```sql
SELECT Customer.CustomerID, Address.AddressLine1, Address.City, Address.StateProvince
FROM Customer
JOIN CustomerAddress ON Customer.CustomerID = CustomerAddress.CustomerID
JOIN Address ON CustomerAddress.AddressID = Address.AddressID
WHERE Customer.FirstName = 'Orlando' AND Customer.LastName = 'Gee';
```

**Expected Row Count:** 1 | **Actual Row Count:** 1

---

### Test ID 30 (Medium)
**Question:** `Show the Name of all product models that have a description in the CatalogDescription`

**Failure Reason:** *Row count mismatch (Expected: 128, Actual: 762)*

**Expected SQL:**
```sql
SELECT Name FROM ProductModel WHERE CatalogDescription IS NOT NULL;
```

**Generated SQL:**
```sql
SELECT ProductModel.Name
FROM ProductModel
JOIN ProductModelProductDescription ON ProductModel.ProductModelID = ProductModelProductDescription.ProductModelID
WHERE ProductModelProductDescription.Culture IS NOT NULL;
```

**Expected Row Count:** 128 | **Actual Row Count:** 762

---

### Test ID 33 (Medium)
**Question:** `What is the highest unit price paid for a product in any order?`

**Failure Reason:** *Row count mismatch (Expected: 1, Actual: 142)*

**Expected SQL:**
```sql
SELECT MAX(UnitPrice) FROM SalesOrderDetail;
```

**Generated SQL:**
```sql
SELECT MAX(SalesOrderDetail.UnitPrice)
FROM SalesOrderDetail
GROUP BY SalesOrderDetail.ProductID;
```

**Expected Row Count:** 1 | **Actual Row Count:** 142

---

### Test ID 40 (Hard)
**Question:** `Find the month and year of orders with the highest total sales`

**Failure Reason:** *Data content mismatch*

**Expected SQL:**
```sql
SELECT strftime('%Y-%m', OrderDate) AS OrderMonth, SUM(TotalDue) AS MonthlySales FROM SalesOrderHeader GROUP BY OrderMonth ORDER BY MonthlySales DESC LIMIT 1;
```

**Generated SQL:**
```sql
SELECT strftime('%Y-%m', SalesOrderHeader.OrderDate) AS OrderMonthYear
FROM SalesOrderHeader
JOIN SalesOrderDetail ON SalesOrderDetail.SalesOrderID = SalesOrderHeader.SalesOrderID
GROUP BY OrderMonthYear
ORDER BY SUM(SalesOrderDetail.LineTotal) DESC
LIMIT 1;
```

**Expected Row Count:** 1 | **Actual Row Count:** 1

---

### Test ID 42 (Hard)
**Question:** `List the CustomerID, FirstName, LastName, and count of shipping addresses for the customer with the most shipping addresses`

**Failure Reason:** *Data content mismatch*

**Expected SQL:**
```sql
SELECT c.CustomerID, c.FirstName, c.LastName, COUNT(ca.AddressID) AS AddressCount FROM Customer c JOIN CustomerAddress ca ON c.CustomerID = ca.CustomerID WHERE ca.AddressType = 'Shipping' GROUP BY c.CustomerID, c.FirstName, c.LastName ORDER BY AddressCount DESC LIMIT 1;
```

**Generated SQL:**
```sql
SELECT Customer.CustomerID, Customer.FirstName, Customer.LastName, COUNT(DISTINCT CustomerAddress.AddressID) AS AddressCount
FROM Customer
JOIN CustomerAddress ON Customer.CustomerID = CustomerAddress.CustomerID
GROUP BY Customer.CustomerID, Customer.FirstName, Customer.LastName
ORDER BY AddressCount DESC
LIMIT 1;
```

**Expected Row Count:** 1 | **Actual Row Count:** 1

---

### Test ID 45 (Hard)
**Question:** `Show the FirstName and LastName of all customers who have ordered products from a ProductCategory with name containing 'Bikes'`

**Failure Reason:** *Row count mismatch (Expected: 22, Actual: 32)*

**Expected SQL:**
```sql
SELECT DISTINCT c.FirstName, c.LastName FROM Customer c JOIN SalesOrderHeader soh ON c.CustomerID = soh.CustomerID JOIN SalesOrderDetail sod ON soh.SalesOrderID = sod.SalesOrderID JOIN Product p ON sod.ProductID = p.ProductID JOIN ProductCategory pc ON p.ProductCategoryID = pc.ProductCategoryID WHERE pc.Name LIKE '%Bikes%';
```

**Generated SQL:**
```sql
SELECT DISTINCT Customer.FirstName, Customer.LastName
FROM Customer
JOIN SalesOrderHeader ON SalesOrderHeader.CustomerID = Customer.CustomerID
JOIN SalesOrderDetail ON SalesOrderDetail.SalesOrderID = SalesOrderHeader.SalesOrderID
JOIN Product ON Product.ProductID = SalesOrderDetail.ProductID
JOIN ProductCategory ON ProductCategory.ProductCategoryID = Product.ProductCategoryID
WHERE EXISTS (SELECT 1 FROM Product INNER JOIN ProductCategory ON Product.ProductCategoryID = ProductCategory.ProductCategoryID WHERE ProductCategory.Name LIKE '%Bikes%');
```

**Expected Row Count:** 22 | **Actual Row Count:** 32

---

### Test ID 46 (Hard)
**Question:** `List the Name of all product categories along with the count of products in that category, including categories with no products`

**Failure Reason:** *Data content mismatch*

**Expected SQL:**
```sql
SELECT pc.Name, COUNT(p.ProductID) AS ProductCount FROM ProductCategory pc LEFT JOIN Product p ON pc.ProductCategoryID = p.ProductCategoryID GROUP BY pc.Name ORDER BY ProductCount DESC;
```

**Generated SQL:**
```sql
SELECT PC.Name, COUNT(P.ProductID)
FROM ProductCategory PC
LEFT JOIN Product P ON PC.ProductCategoryID = P.ProductCategoryID
GROUP BY PC.Name;
```

**Expected Row Count:** 41 | **Actual Row Count:** 41

---









# QueryMind Evaluation Report

Generated on: 2026-07-17 12:22:42

## Performance Summary

| Metric | Value |
| --- | --- |
| **Total Queries** | 50 |
| **Passed** | 44 |
| **Failed** | 6 |
| **Overall Pass Rate** | **88.00%** |
| **Average Latency** | 12.63s |

## Difficulty Breakdown

| Difficulty | Total | Passed | Pass Rate |
| --- | --- | --- | --- |
| Simple | 15 | 13 | 86.67% |
| Medium | 20 | 19 | 95.00% |
| Hard | 15 | 12 | 80.00% |

## Failure Analysis Details

Below are the details of the failed queries. Review them to identify the root cause category: **Ambiguity**, **Join**, **Planner**, or **Prompt**.

### Test ID 4 (Simple)
**Question:** `List the Name and ListPrice of the top 5 most expensive products`

**Failure Reason:** *Row count mismatch (Expected: 5, Actual: 1)*

**Expected SQL:**
```sql
SELECT Name, ListPrice FROM Product ORDER BY ListPrice DESC LIMIT 5;
```

**Generated SQL:**
```sql
SELECT Name, MAX(ListPrice)
FROM Product
ORDER BY ListPrice DESC
LIMIT 5;
```

**Expected Row Count:** 5 | **Actual Row Count:** 1

---

### Test ID 10 (Simple)
**Question:** `Show the FirstName, LastName, and CompanyName of all customers whose sales person is 'adventure-works\pamela0'`

**Failure Reason:** *Row count mismatch (Expected: 74, Actual: 0)*

**Expected SQL:**
```sql
SELECT FirstName, LastName, CompanyName FROM Customer WHERE SalesPerson = 'adventure-works\pamela0';
```

**Generated SQL:**
```sql
SELECT Customer.FirstName, Customer.LastName, Customer.CompanyName
FROM Customer
WHERE Customer.SalesPerson = 'adventure-works\\pamela0';
```

**Expected Row Count:** 74 | **Actual Row Count:** 0

---

### Test ID 30 (Medium)
**Question:** `Show the Name of all product models that have a description in the CatalogDescription`

**Failure Reason:** *Row count mismatch (Expected: 128, Actual: 762)*

**Expected SQL:**
```sql
SELECT Name FROM ProductModel WHERE CatalogDescription IS NOT NULL;
```

**Generated SQL:**
```sql
SELECT ProductModel.Name 
FROM ProductModel 
JOIN ProductModelProductDescription ON ProductModel.ProductModelID = ProductModelProductDescription.ProductModelID
WHERE ProductModel.CatalogDescription IS NOT NULL;
```

**Expected Row Count:** 128 | **Actual Row Count:** 762

---

### Test ID 45 (Hard)
**Question:** `Show the FirstName and LastName of all customers who have ordered products from a ProductCategory with name containing 'Bikes'`

**Failure Reason:** *Row count mismatch (Expected: 22, Actual: 0)*

**Expected SQL:**
```sql
SELECT DISTINCT c.FirstName, c.LastName FROM Customer c JOIN SalesOrderHeader soh ON c.CustomerID = soh.CustomerID JOIN SalesOrderDetail sod ON soh.SalesOrderID = sod.SalesOrderID JOIN Product p ON sod.ProductID = p.ProductID JOIN ProductCategory pc ON p.ProductCategoryID = pc.ProductCategoryID WHERE pc.Name LIKE '%Bikes%';
```

**Generated SQL:**
```sql
SELECT Customer.FirstName, Customer.LastName
FROM Customer
JOIN SalesOrderHeader ON SalesOrderHeader.CustomerID = Customer.CustomerID
JOIN SalesOrderDetail ON SalesOrderDetail.SalesOrderID = SalesOrderHeader.SalesOrderID
JOIN Product ON Product.ProductID = SalesOrderDetail.ProductID
JOIN ProductCategory ON ProductCategory.ProductCategoryID = Product.ProductCategoryID
WHERE EXISTS (
    SELECT 1 FROM Product p JOIN ProductCategory pc ON p.ProductCategoryID = pc.ProductCategoryID 
    WHERE p.Name LIKE '%Bikes%'
);
```

**Expected Row Count:** 22 | **Actual Row Count:** 0

---

### Test ID 46 (Hard)
**Question:** `List the Name of all product categories along with the count of products in that category, including categories with no products`

**Failure Reason:** *Data content mismatch*

**Expected SQL:**
```sql
SELECT pc.Name, COUNT(p.ProductID) AS ProductCount FROM ProductCategory pc LEFT JOIN Product p ON pc.ProductCategoryID = p.ProductCategoryID GROUP BY pc.Name ORDER BY ProductCount DESC;
```

**Generated SQL:**
```sql
SELECT ProductCategory.Name, COUNT(Product.ProductCategoryID) AS CategoryProductCount
FROM ProductCategory
LEFT JOIN Product ON Product.ProductCategoryID = ProductCategory.ProductCategoryID
GROUP BY ProductCategory.Name;
```

**Expected Row Count:** 41 | **Actual Row Count:** 41

---

### Test ID 49 (Hard)
**Question:** `Show the Name of products that have been sold more than 5 times total`

**Failure Reason:** *Data content mismatch*

**Expected SQL:**
```sql
SELECT p.Name, SUM(sod.OrderQty) AS TotalSold FROM Product p JOIN SalesOrderDetail sod ON p.ProductID = sod.ProductID GROUP BY p.Name HAVING TotalSold > 5;
```

**Generated SQL:**
```sql
SELECT Product.Name
FROM SalesOrderDetail
JOIN Product ON SalesOrderDetail.ProductID = Product.ProductID
GROUP BY Product.Name
HAVING SUM(SalesOrderDetail.OrderQty) > 5;
```

**Expected Row Count:** 105 | **Actual Row Count:** 105

---

