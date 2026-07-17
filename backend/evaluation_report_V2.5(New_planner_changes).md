# QueryMind Evaluation Report

Generated on: 2026-07-17 13:00:51

## Performance Summary

| Metric | Value |
| --- | --- |
| **Total Queries** | 50 |
| **Strict Passed** | 44 |
| **Partial Passed** | 3 |
| **Failed** | 3 |
| **Strict Accuracy** | **88.00%** |
| **Semantic / Partial Match Accuracy** | **94.00%** |
| **Average Latency** | 12.68s |

## Difficulty Breakdown

| Difficulty | Total | Strict Passed | Partial Passed | Semantic Pass Rate |
| --- | --- | --- | --- | --- |
| Simple | 15 | 14 | 0 | 93.33% |
| Medium | 20 | 18 | 0 | 90.00% |
| Hard | 15 | 12 | 3 | 100.00% |

## Failure Analysis Details

### Failure / Projection Categorization Breakdown

| Category | Count |
| --- | --- |
| **Join** | 2 |
| **Condition** | 2 |
| **Projection** | 2 |

---

### Test ID 12 (Simple) - [FAIL]
**Question:** `List the Name of all products ordered by their name alphabetically`

**Failure Category:** **Join**

**Failure Reason:** *Row count mismatch (Expected: 295, Actual: 542)*

**Expected SQL:**
```sql
SELECT Name FROM Product ORDER BY Name ASC;
```

**Generated SQL:**
```sql
SELECT P.Name
FROM Product AS P
JOIN SalesOrderDetail AS SOD ON SOD.ProductID = P.ProductID
ORDER BY P.Name ASC;
```

**Expected Row Count:** 295 | **Actual Row Count:** 542

---

### Test ID 22 (Medium) - [FAIL]
**Question:** `Find the AddressLine1, City, and StateProvince of all customer addresses for the customer named Orlando Gee`

**Failure Category:** **Condition**

**Failure Reason:** *Row count mismatch (Expected: 1, Actual: 0)*

**Expected SQL:**
```sql
SELECT a.AddressLine1, a.City, a.StateProvince FROM Customer c JOIN CustomerAddress ca ON c.CustomerID = ca.CustomerID JOIN Address a ON ca.AddressID = a.AddressID WHERE c.FirstName = 'Orlando' AND c.LastName = 'Gee';
```

**Generated SQL:**
```sql
SELECT Address.AddressLine1, Address.City, Address.StateProvince
FROM Customer
JOIN SalesOrderHeader ON SalesOrderHeader.CustomerID = Customer.CustomerID
JOIN Address ON SalesOrderHeader.BillToAddressID = Address.AddressID
WHERE Customer.FirstName = 'Orlando' AND Customer.LastName = 'Gee';
```

**Expected Row Count:** 1 | **Actual Row Count:** 0

---

### Test ID 34 (Medium) - [FAIL]
**Question:** `List the City of all distinct customer addresses`

**Failure Category:** **Join**

**Failure Reason:** *Row count mismatch (Expected: 256, Actual: 269)*

**Expected SQL:**
```sql
SELECT DISTINCT a.City FROM Address a JOIN CustomerAddress ca ON a.AddressID = ca.AddressID;
```

**Generated SQL:**
```sql
SELECT DISTINCT City
FROM Address;
```

**Expected Row Count:** 256 | **Actual Row Count:** 269

---

### Test ID 42 (Hard) - [PARTIAL PASS]
**Question:** `List the CustomerID, FirstName, LastName, and count of shipping addresses for the customer with the most shipping addresses`

**Failure Category:** **Condition**

**Failure Reason:** *Data content mismatch*

**Expected SQL:**
```sql
SELECT c.CustomerID, c.FirstName, c.LastName, COUNT(ca.AddressID) AS AddressCount FROM Customer c JOIN CustomerAddress ca ON c.CustomerID = ca.CustomerID WHERE ca.AddressType = 'Shipping' GROUP BY c.CustomerID, c.FirstName, c.LastName ORDER BY AddressCount DESC LIMIT 1;
```

**Generated SQL:**
```sql
SELECT Customer.CustomerID, Customer.FirstName, Customer.LastName, COUNT(DISTINCT CustomerAddress.AddressType) AS AddressCount
FROM Customer
JOIN CustomerAddress ON CustomerAddress.CustomerID = Customer.CustomerID
GROUP BY Customer.CustomerID, Customer.FirstName, Customer.LastName
ORDER BY AddressCount DESC
LIMIT 1;
```

**Expected Row Count:** 1 | **Actual Row Count:** 1

---

### Test ID 48 (Hard) - [PARTIAL PASS]
**Question:** `Find the total quantity of products sold in each year`

**Failure Category:** **Projection**

**Failure Reason:** *Data content mismatch*

**Expected SQL:**
```sql
SELECT strftime('%Y', soh.OrderDate) AS SalesYear, SUM(sod.OrderQty) AS TotalQty FROM SalesOrderHeader soh JOIN SalesOrderDetail sod ON soh.SalesOrderID = sod.SalesOrderID GROUP BY SalesYear;
```

**Generated SQL:**
```sql
SELECT SUM(SalesOrderDetail.OrderQty) AS TotalQuantitySold, strftime('%Y', SalesOrderHeader.OrderDate) AS OrderYear
FROM SalesOrderDetail
JOIN SalesOrderHeader ON SalesOrderDetail.SalesOrderID = SalesOrderHeader.SalesOrderID
GROUP BY OrderYear
ORDER BY OrderYear DESC;
```

**Expected Row Count:** 1 | **Actual Row Count:** 1

---

### Test ID 49 (Hard) - [PARTIAL PASS]
**Question:** `Show the Name of products that have been sold more than 5 times total`

**Failure Category:** **Projection**

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
HAVING SUM(SalesOrderDetail.OrderQty) > 5
ORDER BY SUM(SalesOrderDetail.OrderQty) DESC;
```

**Expected Row Count:** 105 | **Actual Row Count:** 105

---

