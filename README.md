# Project-Loyiya
- ### Loyihada quyidagi qatlamlar bo‘lishi kerak:Domain, Repository, Service, API, Schema, Infrastructure, Core Config.

- ### API → Service → Repository → Database ketma-ketligida ishlaydi.

- ### Har bir qatlam faqat o‘z vazifasi uchun javob beradi va yuqoriga bog‘lanadi, pastga emas.


```bash 
project/
│
├── src/
│   ├── api/
│   │   ├── v1/
│   │   │   ├── endpoints/
│   │   │   │   ├── user.py
│   │   │   │   ├── task.py
│   │   │   │   └── auth.py
│   │   │   └── router.py
│   │   └── deps.py
│   │
│   ├── core/
│   │   ├── config.py
│   │   ├── security.py
│   │   └── exceptions.py
│   │
│   ├── db/
│   │   ├── base.py
│   │   ├── session.py
│   │   ├── init_db.py
│   │   └── migrations/   ← Alembic
│   │
│   ├── models/
│   │   ├── user.py
│   │   ├── task.py
│   │   └── __init__.py
│   │
│   ├── schemas/
│   │   ├── user.py
│   │   ├── task.py
│   │   └── auth.py
│   │
│   ├── repository/
│   │   ├── user_repo.py
│   │   ├── task_repo.py
│   │   └── base.py
│   │
│   ├── services/
│   │   ├── user_service.py
│   │   ├── task_service.py
│   │   └── auth_service.py
│   │
│   ├── main.py
│   └── __init__.py
│
├── tests/
│   ├── api/
│   ├── services/
│   └── repository/
│
├── alembic.ini
├── requirements.txt
├── docker-compose.yml
├── Dockerfile
└── README.md
```

## 3. DQL — Data Query Language
### SELECT
```sql
SELECT col1, col2 FROM table_name;
SELECT * FROM table_name;
```

### Filtering
```sql
WHERE col = 10;
WHERE col BETWEEN 10 AND 20;
WHERE col LIKE 'A%';
WHERE col ILIKE '%test';
WHERE col IN (1,2,3);
WHERE col IS NULL;
WHERE col IS NOT NULL;
```

### Sorting / Limit
```sql
ORDER BY col ASC;
ORDER BY col DESC;
LIMIT 10;
OFFSET 20;
```

### GROUP BY & HAVING
```sql
GROUP BY col;
HAVING COUNT(*) > 1;
```

### JOINs
```sql
INNER JOIN
LEFT JOIN
RIGHT JOIN
FULL JOIN
CROSS JOIN
LATERAL JOIN
```

## 4. SQL Functions
### Aggregate
```sql
COUNT(col)
SUM(col)
AVG(col)
MIN(col)
MAX(col)
```

### String
```sql
LOWER(col)
UPPER(col)
CONCAT(a, b)
TRIM(col)
SUBSTRING(col FROM 1 FOR 3)
REPLACE(col, 'a', 'b')
LENGTH(col)
```

### Numeric
```sql
ROUND(col)
CEIL(col)
FLOOR(col)
ABS(col)
RANDOM()
```

### Date/Time
```sql
NOW()
CURRENT_DATE
CURRENT_TIMESTAMP
AGE(timestamp)
DATE_TRUNC('day', ts)
EXTRACT(YEAR FROM ts)
```

## 5. Constraints
```sql
PRIMARY KEY
FOREIGN KEY
UNIQUE
CHECK
NOT NULL
DEFAULT
ON DELETE CASCADE
ON UPDATE CASCADE
```

## 6. Index Types
```sql
CREATE INDEX idx ON table(col);
CREATE INDEX idx_gin ON table USING GIN(jsonb_col);
CREATE INDEX idx_gist ON table USING GIST(geo_col);
CREATE INDEX idx_brin ON table USING BRIN(date_col);
```

## 7. Advanced SQL
### Window Functions
```sql
ROW_NUMBER() OVER (PARTITION BY col ORDER BY id)
RANK() OVER (...)
DENSE_RANK() OVER (...)
LEAD(col, 1) OVER (...)
LAG(col, 1) OVER (...)
```

### Subqueries
```sql
SELECT * FROM users WHERE id IN (SELECT user_id FROM orders);
SELECT EXISTS(SELECT 1 FROM orders WHERE amount > 100);
```

### CTE
```sql
WITH top_users AS (
    SELECT * FROM users WHERE score > 90
)
SELECT * FROM top_users;
```

### Transactions
```sql
BEGIN;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;
```

## 8. PostgreSQL Specific
```sql
SERIAL, BIGSERIAL
JSON, JSONB
ARRAY
COALESCE()
NULLIF()
TO_CHAR(timestamp, 'YYYY-MM-DD')
UNNEST(array)
GENERATED ALWAYS AS IDENTITY
```
