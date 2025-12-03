# Project-Loyiha

- ### Loyihada quyidagi qatlamlar bo‘lishi kerak:Domain, Repository, Service, API, Schema, Infrastructure, Core Config.

- ### API → Service → Repository → Database ketma-ketligida ishlaydi.

- ### Har bir qatlam faqat o‘z vazifasi uchun javob beradi va yuqoriga bog‘lanadi, pastga emas.

## Technologies

- ### Database: PostgreSQL

- ### ORM: SQLAlchemy

- ### Web Framework: FastAPI

- ### Migration Tool: Alembic

## Alembic Config

1. ### Alembic init buyrug‘i / alembic init usage

```bash
alembic init <migrations_dir>
# misol:
alembic init database/migrations
```

2. ### alembic.ini ga sqlalchemy.url qo‘yish

```python
# mirgrations/env.py
config.set_main_option("sqlalchemy.url", yourDSN)
```

3. ### env.py va target_metadata (autogenerate uchun)

```python
# env.py ichida siz ORM Base.metadata ni target_metadata sifatida berishingiz kerak, shunda alembic --autogenerate jadvallarni aniqlaydi.
from myproject.database.base import Base  # sizning Declarative base

target_metadata = Base.metadata
```

4. ### ModuleNotFoundError: No module named 'database' — sabab va tuzatish

- **init**.py — papkani Python package ga aylantiradi (oldingi Python versiyalarida muhim, hozir ham tavsiya qilinadi).

- Module — bitta .py fayl (masalan models.py).

- Package — ichida bir yoki bir nechta modul bo‘lgan papka (masalan database/).
6. ### Alembic bilan migratsiya quick start (summary + commands)

1. Init: alembic init database/migrations

2. alembic.ini ni sozla yoki env.py da DSN fallback qo‘sh.

3. Autogenerate: alembic revision --autogenerate -m "init"

4. Apply: alembic upgrade head

5. Rollback: alembic downgrade -1 yoki alembic downgrade <revision_id>
```bash
alembic init database/migrations
alembic revision --autogenerate -m "init"
alembic upgrade head
alembic downgrade -1
```
## File structure 
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
├── database/
│   ├── __init__.py
│   ├── config.py
│   ├── session.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── workers.py
│   │   └── tasks.py
│   ├── migrations/
│   │    ├── env.py
│   │    ├── README
│   │    ├── versions/
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
