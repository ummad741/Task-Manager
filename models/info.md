# models/

- ### UZ: SQLAlchemy ORM klasslari (jadval strukturalari).
- ### EN: SQLAlchemy ORM models (table definitions).

## 1. DDL — Data Definition Language
### CREATE
```sql
CREATE DATABASE db_name;
CREATE TABLE table_name (...);
CREATE SCHEMA schema_name;
CREATE INDEX idx_name ON tbl(col);
CREATE UNIQUE INDEX idx_name ON tbl(col);
CREATE VIEW view_name AS SELECT ...;
CREATE MATERIALIZED VIEW mv AS SELECT ...;
CREATE FUNCTION ...;
CREATE TRIGGER ...;
CREATE EXTENSION "uuid-ossp";
```

### ALTER
```sql
ALTER TABLE table_name ADD COLUMN col datatype;
ALTER TABLE table_name DROP COLUMN col;
ALTER TABLE table_name RENAME TO new_name;
ALTER COLUMN col TYPE new_type;
```

### DROP
```sql
DROP TABLE table_name;
DROP DATABASE db_name;
DROP INDEX idx_name;
DROP VIEW view_name;
DROP FUNCTION func_name;
DROP TRIGGER trigger_name;
```


## 2. DML — Data Manipulation Language
### SELECT
```sql
SELECT * FROM table_name;
```

### INSERT
```sql
INSERT INTO table_name (col1, col2) VALUES (val1, val2);
INSERT INTO table_name (id, name) VALUES (1, 'Ali')
ON CONFLICT (id) DO UPDATE SET name = EXCLUDED.name;
```

### UPDATE
```sql
UPDATE table_name SET col = value WHERE id = 1;
```

### DELETE
```sql
DELETE FROM table_name WHERE id = 1;
```