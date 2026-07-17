# QueryMind Evaluation Report

Generated on: 2026-07-17 16:34:49

## Performance Summary

| Metric | Value |
| --- | --- |
| **Total Queries** | 30 |
| **Strict Passed** | 23 |
| **Partial Passed** | 4 |
| **Failed** | 3 |
| **Strict Accuracy** | **76.67%** |
| **Semantic / Partial Match Accuracy** | **90.00%** |
| **Average Latency** | 13.13s |

## Difficulty Breakdown

| Difficulty | Total | Strict Passed | Partial Passed | Semantic Pass Rate |
| --- | --- | --- | --- | --- |
| Simple | 10 | 7 | 2 | 90.00% |
| Medium | 10 | 9 | 1 | 100.00% |
| Hard | 10 | 7 | 1 | 80.00% |

## Failure Analysis Details

### Failure / Projection Categorization Breakdown

| Category | Count |
| --- | --- |
| **Aggregation** | 2 |
| **Projection** | 3 |
| **Execution** | 1 |
| **Prompt** | 1 |

---

### Test ID 2 (Simple) - [FAIL]
**Question:** `Show the Title of the top 5 longest tracks.`

**Failure Category:** **Aggregation**

**Failure Reason:** *Data content mismatch*

**Expected SQL:**
```sql
SELECT Name FROM Track ORDER BY Milliseconds DESC LIMIT 5;
```

**Generated SQL:**
```sql
SELECT Album.Title
FROM Album
JOIN Track ON Track.AlbumId = Album.AlbumId
GROUP BY Album.Title, Track.TrackId
ORDER BY MAX(Track.Milliseconds) DESC
LIMIT 5;
```

**Expected Row Count:** 5 | **Actual Row Count:** 5

---

### Test ID 8 (Simple) - [PARTIAL PASS]
**Question:** `List the top 10 most expensive tracks.`

**Failure Category:** **Projection**

**Failure Reason:** *Data content mismatch*

**Expected SQL:**
```sql
SELECT Name, UnitPrice FROM Track ORDER BY UnitPrice DESC LIMIT 10;
```

**Generated SQL:**
```sql
SELECT Track.Name
FROM Track
ORDER BY Track.UnitPrice DESC
LIMIT 10;
```

**Expected Row Count:** 10 | **Actual Row Count:** 10

---

### Test ID 9 (Simple) - [PARTIAL PASS]
**Question:** `Show all employees ordered by their HireDate.`

**Failure Category:** **Projection**

**Failure Reason:** *Data content mismatch*

**Expected SQL:**
```sql
SELECT FirstName, LastName, HireDate FROM Employee ORDER BY HireDate ASC;
```

**Generated SQL:**
```sql
SELECT LastName, FirstName, HireDate
FROM Employee
ORDER BY HireDate ASC;
```

**Expected Row Count:** 8 | **Actual Row Count:** 8

---

### Test ID 13 (Medium) - [PARTIAL PASS]
**Question:** `Find the customers who have placed invoices worth more than $10.`

**Failure Category:** **Aggregation**

**Failure Reason:** *Data content mismatch*

**Expected SQL:**
```sql
SELECT DISTINCT c.FirstName, c.LastName FROM Customer c JOIN Invoice i ON c.CustomerId = i.CustomerId WHERE i.Total > 10;
```

**Generated SQL:**
```sql
SELECT DISTINCT Customer.CustomerId, Customer.FirstName, Customer.LastName
FROM Invoice
JOIN Customer ON Invoice.CustomerId = Customer.CustomerId
GROUP BY Customer.CustomerId, Customer.FirstName, Customer.LastName
HAVING SUM(Invoice.Total) > 10;
```

**Expected Row Count:** 59 | **Actual Row Count:** 59

---

### Test ID 22 (Hard) - [PARTIAL PASS]
**Question:** `Show the artist whose tracks generated the highest revenue.`

**Failure Category:** **Projection**

**Failure Reason:** *Data content mismatch*

**Expected SQL:**
```sql
SELECT Artist.Name, SUM(InvoiceLine.UnitPrice * InvoiceLine.Quantity) AS Revenue FROM Artist JOIN Album ON Artist.ArtistId = Album.ArtistId JOIN Track ON Album.AlbumId = Track.AlbumId JOIN InvoiceLine ON Track.TrackId = InvoiceLine.TrackId GROUP BY Artist.ArtistId, Artist.Name ORDER BY Revenue DESC LIMIT 1;
```

**Generated SQL:**
```sql
SELECT Artist.Name
FROM InvoiceLine
JOIN Track ON InvoiceLine.TrackId = Track.TrackId
JOIN Album ON Track.AlbumId = Album.AlbumId
JOIN Artist ON Album.ArtistId = Artist.ArtistId
GROUP BY Artist.Name
ORDER BY SUM(InvoiceLine.UnitPrice * InvoiceLine.Quantity) DESC
LIMIT 1;
```

**Expected Row Count:** 1 | **Actual Row Count:** 1

---

### Test ID 24 (Hard) - [FAIL]
**Question:** `List customers who purchased tracks from more than 3 different genres.`

**Failure Category:** **Execution**

**Failure Reason:** *QueryMind failed: Both queries failed:
Gen: ambiguous column name: GenreId
Ref: no such column: GenreId*

**Expected SQL:**
```sql
SELECT c.FirstName, c.LastName FROM Customer c JOIN Invoice i ON c.CustomerId = i.CustomerId JOIN InvoiceLine il ON i.InvoiceId = il.InvoiceId JOIN Track t ON il.TrackId = t.TrackId GROUP BY c.CustomerId, c.FirstName, c.LastName HAVING COUNT(DISTINCT t.GenreId) > 3;
```

**Generated SQL:**
```sql
None
```

**Expected Row Count:** 59 | **Actual Row Count:** 0

---

### Test ID 26 (Hard) - [FAIL]
**Question:** `Show the most purchased track.`

**Failure Category:** **Prompt**

**Failure Reason:** *Data content mismatch*

**Expected SQL:**
```sql
SELECT Track.Name, SUM(InvoiceLine.Quantity) AS TotalPurchased FROM Track JOIN InvoiceLine ON Track.TrackId = InvoiceLine.TrackId GROUP BY Track.TrackId, Track.Name ORDER BY TotalPurchased DESC LIMIT 1;
```

**Generated SQL:**
```sql
SELECT Track.Name
FROM InvoiceLine
JOIN Track ON InvoiceLine.TrackId = Track.TrackId
GROUP BY Track.Name
ORDER BY SUM(InvoiceLine.Quantity) DESC
LIMIT 1;
```

**Expected Row Count:** 1 | **Actual Row Count:** 1

---

