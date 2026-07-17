# QueryMind Evaluation Report

Generated on: 2026-07-17 14:43:53

## Performance Summary

| Metric | Value |
| --- | --- |
| **Total Queries** | 35 |
| **Strict Passed** | 21 |
| **Partial Passed** | 3 |
| **Failed** | 11 |
| **Strict Accuracy** | **60.00%** |
| **Semantic / Partial Match Accuracy** | **68.57%** |
| **Average Latency** | 12.97s |

## Difficulty Breakdown

| Difficulty | Total | Strict Passed | Partial Passed | Semantic Pass Rate |
| --- | --- | --- | --- | --- |
| Simple | 10 | 8 | 0 | 80.00% |
| Medium | 10 | 7 | 1 | 80.00% |
| Hard | 10 | 6 | 2 | 80.00% |
| Very hard | 5 | 0 | 0 | 0.00% |

## Failure Analysis Details

### Failure / Projection Categorization Breakdown

| Category | Count |
| --- | --- |
| **Aggregation** | 7 |
| **Prompt** | 2 |
| **Join** | 3 |
| **Projection** | 1 |
| **Condition** | 1 |

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
FROM (
    SELECT Track.AlbumId, MAX(Track.Milliseconds) AS MaxMilliseconds
    FROM Track
    GROUP BY Track.AlbumId
) AS TopTracks
JOIN Album ON TopTracks.AlbumId = Album.AlbumId
JOIN Track ON Track.AlbumId = TopTracks.AlbumId AND Track.Milliseconds = TopTracks.MaxMilliseconds
ORDER BY Track.Milliseconds DESC
LIMIT 5;
```

**Expected Row Count:** 5 | **Actual Row Count:** 5

---

### Test ID 9 (Simple) - [FAIL]
**Question:** `Show all employees ordered by their HireDate.`

**Failure Category:** **Prompt**

**Failure Reason:** *Data content mismatch*

**Expected SQL:**
```sql
SELECT FirstName, LastName, HireDate FROM Employee ORDER BY HireDate ASC;
```

**Generated SQL:**
```sql
SELECT HireDate
FROM Employee
ORDER BY HireDate ASC;
```

**Expected Row Count:** 8 | **Actual Row Count:** 8

---

### Test ID 12 (Medium) - [FAIL]
**Question:** `List the Name of tracks and their genre.`

**Failure Category:** **Join**

**Failure Reason:** *Row count mismatch (Expected: 3503, Actual: 20)*

**Expected SQL:**
```sql
SELECT Track.Name, Genre.Name FROM Track JOIN Genre ON Track.GenreId = Genre.GenreId;
```

**Generated SQL:**
```sql
SELECT Track.Name, Genre.Name
FROM Track
JOIN Genre ON Track.GenreId = Genre.GenreId
LIMIT 20;
```

**Expected Row Count:** 3503 | **Actual Row Count:** 20

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

### Test ID 17 (Medium) - [FAIL]
**Question:** `Show the employee and the customers assigned to them.`

**Failure Category:** **Join**

**Failure Reason:** *Row count mismatch (Expected: 59, Actual: 20)*

**Expected SQL:**
```sql
SELECT e.FirstName, e.LastName, c.FirstName, c.LastName FROM Employee e JOIN Customer c ON e.EmployeeId = c.SupportRepId;
```

**Generated SQL:**
```sql
SELECT DISTINCT Employee.FirstName AS EmployeeFirstName, Employee.LastName AS EmployeeLastName, Customer.FirstName AS CustomerFirstName, Customer.LastName AS CustomerLastName
FROM Employee
JOIN Customer ON Customer.SupportRepId = Employee.EmployeeId
LIMIT 20;
```

**Expected Row Count:** 59 | **Actual Row Count:** 20

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

### Test ID 23 (Hard) - [PARTIAL PASS]
**Question:** `Find the genre with the highest number of purchases.`

**Failure Category:** **Aggregation**

**Failure Reason:** *Data content mismatch*

**Expected SQL:**
```sql
SELECT Genre.Name, SUM(InvoiceLine.Quantity) AS TotalPurchased FROM Genre JOIN Track ON Genre.GenreId = Track.GenreId JOIN InvoiceLine ON Track.TrackId = InvoiceLine.TrackId GROUP BY Genre.GenreId, Genre.Name ORDER BY TotalPurchased DESC LIMIT 1;
```

**Generated SQL:**
```sql
SELECT Genre.Name
FROM InvoiceLine
JOIN Track ON InvoiceLine.TrackId = Track.TrackId
JOIN Genre ON Track.GenreId = Genre.GenreId
GROUP BY Genre.Name
ORDER BY COUNT(InvoiceLine.TrackId) DESC
LIMIT 1;
```

**Expected Row Count:** 1 | **Actual Row Count:** 1

---

### Test ID 26 (Hard) - [FAIL]
**Question:** `Show the most purchased track.`

**Failure Category:** **Aggregation**

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
ORDER BY COUNT(InvoiceLine.InvoiceId) DESC
LIMIT 1;
```

**Expected Row Count:** 1 | **Actual Row Count:** 1

---

### Test ID 27 (Hard) - [FAIL]
**Question:** `Find the average track price for each genre.`

**Failure Category:** **Prompt**

**Failure Reason:** *Data content mismatch*

**Expected SQL:**
```sql
SELECT Genre.Name, AVG(Track.UnitPrice) AS AvgPrice FROM Genre JOIN Track ON Genre.GenreId = Track.GenreId GROUP BY Genre.GenreId, Genre.Name;
```

**Generated SQL:**
```sql
SELECT Genre.GenreId, AVG(Track.UnitPrice) AS AverageUnitPrice
FROM Track
JOIN Genre ON Track.GenreId = Genre.GenreId
GROUP BY Genre.GenreId
ORDER BY Genre.GenreId ASC;
```

**Expected Row Count:** 25 | **Actual Row Count:** 25

---

### Test ID 31 (Very hard) - [FAIL]
**Question:** `Find the employee who manages the customers with the highest total spending.`

**Failure Category:** **Aggregation**

**Failure Reason:** *Data content mismatch*

**Expected SQL:**
```sql
SELECT e.FirstName, e.LastName, SUM(i.Total) AS TotalSpending FROM Employee e JOIN Customer c ON e.EmployeeId = c.SupportRepId JOIN Invoice i ON c.CustomerId = i.CustomerId GROUP BY e.EmployeeId, e.FirstName, e.LastName ORDER BY TotalSpending DESC LIMIT 1;
```

**Generated SQL:**
```sql
SELECT Employee.FirstName, Employee.LastName
FROM Customer
JOIN Invoice ON Customer.CustomerId = Invoice.CustomerId
JOIN Employee ON Customer.SupportRepId = Employee.EmployeeId
WHERE Invoice.Total = (
    SELECT MAX(Total)
    FROM Invoice
)
ORDER BY Employee.EmployeeId ASC;
```

**Expected Row Count:** 1 | **Actual Row Count:** 1

---

### Test ID 32 (Very hard) - [FAIL]
**Question:** `List the top 3 artists by number of tracks sold.`

**Failure Category:** **Aggregation**

**Failure Reason:** *Data content mismatch*

**Expected SQL:**
```sql
SELECT Artist.Name, SUM(InvoiceLine.Quantity) AS TracksSold FROM Artist JOIN Album ON Artist.ArtistId = Album.ArtistId JOIN Track ON Album.AlbumId = Track.AlbumId JOIN InvoiceLine ON Track.TrackId = InvoiceLine.TrackId GROUP BY Artist.ArtistId, Artist.Name ORDER BY TracksSold DESC LIMIT 3;
```

**Generated SQL:**
```sql
SELECT Artist.Name
FROM Artist
JOIN Album ON Album.ArtistId = Artist.ArtistId
JOIN Track ON Track.AlbumId = Album.AlbumId
GROUP BY Artist.Name
ORDER BY COUNT(Track.TrackId) DESC
LIMIT 3;
```

**Expected Row Count:** 3 | **Actual Row Count:** 3

---

### Test ID 33 (Very hard) - [FAIL]
**Question:** `Show playlists that contain tracks from more than 5 genres.`

**Failure Category:** **Join**

**Failure Reason:** *Row count mismatch (Expected: 3, Actual: 2)*

**Expected SQL:**
```sql
SELECT Playlist.Name FROM Playlist JOIN PlaylistTrack ON Playlist.PlaylistId = PlaylistTrack.PlaylistId JOIN Track ON PlaylistTrack.TrackId = Track.TrackId GROUP BY Playlist.PlaylistId, Playlist.Name HAVING COUNT(DISTINCT Track.GenreId) > 5;
```

**Generated SQL:**
```sql
SELECT Playlist.Name
FROM Playlist
JOIN PlaylistTrack ON PlaylistTrack.PlaylistId = Playlist.PlaylistId
JOIN Track ON PlaylistTrack.TrackId = Track.TrackId
JOIN Genre ON Track.GenreId = Genre.GenreId
GROUP BY Playlist.Name
HAVING COUNT(DISTINCT Genre.GenreId) > 5;
```

**Expected Row Count:** 3 | **Actual Row Count:** 2

---

### Test ID 34 (Very hard) - [FAIL]
**Question:** `Find customers who purchased every track from a specific album.`

**Failure Category:** **Condition**

**Failure Reason:** *Row count mismatch (Expected: 49, Actual: 0)*

**Expected SQL:**
```sql
SELECT DISTINCT c.FirstName, c.LastName, alb.Title FROM Customer c JOIN Invoice i ON c.CustomerId = i.CustomerId JOIN InvoiceLine il ON i.InvoiceId = il.InvoiceId JOIN Track t ON il.TrackId = t.TrackId JOIN Album alb ON t.AlbumId = alb.AlbumId GROUP BY c.CustomerId, alb.AlbumId HAVING COUNT(DISTINCT t.TrackId) = (SELECT COUNT(TrackId) FROM Track WHERE AlbumId = alb.AlbumId);
```

**Generated SQL:**
```sql
SELECT DISTINCT Customer.CustomerId, Customer.FirstName, Customer.LastName
FROM Customer
JOIN Invoice ON Invoice.CustomerId = Customer.CustomerId
JOIN InvoiceLine ON InvoiceLine.InvoiceId = Invoice.InvoiceId
JOIN Track ON InvoiceLine.TrackId = Track.TrackId
JOIN Album ON Track.AlbumId = Album.AlbumId
WHERE Album.Title = 'Specific Album Title'
GROUP BY Customer.CustomerId, Customer.FirstName, Customer.LastName
HAVING COUNT(DISTINCT Track.TrackId) = (SELECT COUNT(*) FROM Track WHERE Track.AlbumId = Album.AlbumId);
```

**Expected Row Count:** 49 | **Actual Row Count:** 0

---

### Test ID 35 (Very hard) - [FAIL]
**Question:** `Find artists that have never had a track purchased.`

**Failure Category:** **Aggregation**

**Failure Reason:** *Row count mismatch (Expected: 110, Actual: 170)*

**Expected SQL:**
```sql
SELECT Artist.Name FROM Artist LEFT JOIN Album ON Artist.ArtistId = Album.ArtistId LEFT JOIN Track ON Album.AlbumId = Track.AlbumId LEFT JOIN InvoiceLine ON Track.TrackId = InvoiceLine.TrackId GROUP BY Artist.ArtistId, Artist.Name HAVING COUNT(InvoiceLine.InvoiceLineId) = 0;
```

**Generated SQL:**
```sql
SELECT DISTINCT Artist.Name
FROM Artist
JOIN Album ON Album.ArtistId = Artist.ArtistId
JOIN Track ON Track.AlbumId = Album.AlbumId
LEFT JOIN InvoiceLine ON InvoiceLine.TrackId = Track.TrackId
WHERE InvoiceLine.InvoiceLineId IS NULL;
```

**Expected Row Count:** 110 | **Actual Row Count:** 170

---

