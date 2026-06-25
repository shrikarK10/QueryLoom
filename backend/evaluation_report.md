# QueryMind Evaluation Report

Generated on: 2026-06-16 17:30:04

## Performance Summary

| Metric | Value |
| --- | --- |
| **Total Queries** | 50 |
| **Passed** | 41 |
| **Failed** | 9 |
| **Overall Pass Rate** | **82.00%** |
| **Average Latency** | 13.30s |

## Difficulty Breakdown

| Difficulty | Total | Passed | Pass Rate |
| --- | --- | --- | --- |
| Simple | 15 | 15 | 100.00% |
| Medium | 20 | 18 | 90.00% |
| Hard | 15 | 8 | 53.33% |

## Failure Analysis Details

Below are the details of the failed queries. Review them to identify the root cause category: **Ambiguity**, **Join**, **Planner**, or **Prompt**.

### Test ID 30 (Medium)
**Question:** `Show the Name of all product models that have a description in the CatalogDescription`

**Failure Reason:** *Row count mismatch (Expected: 128, Actual: 762)*

**Expected SQL:**
```sql
SELECT Name FROM ProductModel WHERE CatalogDescription IS NOT NULL;
```

**Generated SQL:**
```sql
SELECT pm.Name
FROM ProductModel pm
JOIN ProductModelProductDescription pmpd ON pm.ProductModelID = pmpd.ProductModelID;
```

**Expected Row Count:** 128 | **Actual Row Count:** 762

---

### Test ID 31 (Medium)
**Question:** `Show all customer CompanyNames and the SalesOrderIDs they placed`

**Failure Reason:** *Row count mismatch (Expected: 32, Actual: 542)*

**Expected SQL:**
```sql
SELECT c.CompanyName, soh.SalesOrderID FROM Customer c JOIN SalesOrderHeader soh ON c.CustomerID = soh.CustomerID;
```

**Generated SQL:**
```sql
SELECT Customer.CompanyName, SalesOrderHeader.SalesOrderID
FROM SalesOrderHeader
JOIN Customer ON SalesOrderHeader.CustomerID = Customer.CustomerID
JOIN SalesOrderDetail ON SalesOrderDetail.SalesOrderID = SalesOrderHeader.SalesOrderID;
```

**Expected Row Count:** 32 | **Actual Row Count:** 542

---

### Test ID 37 (Hard)
**Question:** `Show product descriptions for the product 'Classic Vest, S' in English`

**Failure Reason:** *Row count mismatch (Expected: 0, Actual: 6)*

**Expected SQL:**
```sql
SELECT pd.Description FROM Product p JOIN ProductModel pm ON p.ProductModelID = pm.ProductModelID JOIN ProductModelProductDescription pmpd ON pm.ProductModelID = pmpd.ProductModelID JOIN ProductDescription pd ON pmpd.ProductDescriptionID = pd.ProductDescriptionID WHERE p.Name = 'Classic Vest, S' AND pmpd.Culture = 'en';
```

**Generated SQL:**
```sql
SELECT ProductModel.ProductModelID, ProductDescription.Description
FROM ProductModel
JOIN ProductModelProductDescription ON ProductModel.ProductModelID = ProductModelProductDescription.ProductModelID
JOIN ProductDescription ON ProductModelProductDescription.ProductDescriptionID = ProductDescription.ProductDescriptionID
JOIN Product ON ProductModel.ProductModelID = Product.ProductModelID AND Product.Name = 'Classic Vest, S'
LIMIT 20;
```

**Expected Row Count:** 0 | **Actual Row Count:** 6

---

### Test ID 38 (Hard)
**Question:** `Find the Name and sum of LineTotal as category revenue for each product category ordered by category revenue descending`

**Failure Reason:** *Data content mismatch*

**Expected SQL:**
```sql
SELECT c.Name, SUM(sod.LineTotal) AS CategoryRevenue FROM SalesOrderDetail sod JOIN Product p ON sod.ProductID = p.ProductID JOIN ProductCategory c ON p.ProductCategoryID = c.ProductCategoryID GROUP BY c.Name ORDER BY CategoryRevenue DESC;
```

**Generated SQL:**
```sql
SELECT pc.ProductCategoryID, SUM(sod.LineTotal) AS CategoryRevenue
FROM Product p
JOIN SalesOrderDetail sod ON p.ProductID = sod.ProductID
JOIN ProductCategory pc ON p.ProductCategoryID = pc.ProductCategoryID
GROUP BY pc.ProductCategoryID
ORDER BY CategoryRevenue DESC;
```

**Expected Row Count:** 26 | **Actual Row Count:** 26

---

### Test ID 41 (Hard)
**Question:** `For each product, list its Name, ProductCategory Name as category name, and ProductModel Name as model name`

**Failure Reason:** *Data content mismatch*

**Expected SQL:**
```sql
SELECT p.Name AS ProductName, c.Name AS CategoryName, pm.Name AS ModelName FROM Product p JOIN ProductCategory c ON p.ProductCategoryID = c.ProductCategoryID LEFT JOIN ProductModel pm ON p.ProductModelID = pm.ProductModelID;
```

**Generated SQL:**
```sql
SELECT 
    P.ProductID, 
    P.Name AS ProductName, 
    PC.Name AS CategoryName, 
    PM.Name AS ModelName
FROM 
    Product P
JOIN 
    ProductCategory PC ON P.ProductCategoryID = PC.ProductCategoryID
JOIN 
    ProductModel PM ON P.ProductModelID = PM.ProductModelID;
```

**Expected Row Count:** 295 | **Actual Row Count:** 295

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
SELECT Customer.CustomerID, Customer.FirstName, Customer.LastName, COUNT(CustomerAddress.AddressID) AS AddressCount
FROM Customer
JOIN CustomerAddress ON CustomerAddress.CustomerID = Customer.CustomerID
GROUP BY Customer.CustomerID, Customer.FirstName, Customer.LastName
ORDER BY AddressCount DESC
LIMIT 1;
```

**Expected Row Count:** 1 | **Actual Row Count:** 1

---

### Test ID 45 (Hard)
**Question:** `Show the FirstName and LastName of all customers who have ordered products from a ProductCategory with name containing 'Bikes'`

**Failure Reason:** *Row count mismatch (Expected: 22, Actual: 200)*

**Expected SQL:**
```sql
SELECT DISTINCT c.FirstName, c.LastName FROM Customer c JOIN SalesOrderHeader soh ON c.CustomerID = soh.CustomerID JOIN SalesOrderDetail sod ON soh.SalesOrderID = sod.SalesOrderID JOIN Product p ON sod.ProductID = p.ProductID JOIN ProductCategory pc ON p.ProductCategoryID = pc.ProductCategoryID WHERE pc.Name LIKE '%Bikes%';
```

**Generated SQL:**
```sql
SELECT Customer.FirstName, Customer.LastName
FROM Customer
JOIN SalesOrderHeader ON Customer.CustomerID = SalesOrderHeader.CustomerID
JOIN SalesOrderDetail ON SalesOrderHeader.SalesOrderID = SalesOrderDetail.SalesOrderID
JOIN Product ON SalesOrderDetail.ProductID = Product.ProductID
JOIN ProductCategory ON Product.ProductCategoryID = ProductCategory.ProductCategoryID
WHERE ProductCategory.Name LIKE '%Bikes%';
```

**Expected Row Count:** 22 | **Actual Row Count:** 200

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
SELECT ProductCategory.Name, COUNT(Product.ProductID) AS ProductCount
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
GROUP BY Product.ProductID
HAVING SUM(SalesOrderDetail.OrderQty) > 5;
```

**Expected Row Count:** 105 | **Actual Row Count:** 105

---

