# repositories/

- ### UZ: DB bilan past darajadagi CRUD (SQLlar, transaction scope). Bitta, CRUD funksiyalari shu yerda bo‘ladi.

- ### EN: Low-level DB access (CRUD), transaction-aware repository functions.

## Repository Layer (Data Access)
### Nima uchun javob beradi?
- #### Database bilan ishlash
- #### CRUD (create, read, update, delete)
- #### SQLAlchemy ORM/Core orqali transaction
- #### Query building

### Repository hech qaerda:
- #### ❌ HTTP chaqirmaydi
- #### ❌ FastAPI haqida bilmaydi
- #### ❌ Service logikasini aralashtirmaydi

### ➡️ Faqat data olish va yozish.

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

## For example how it's work:

```python 
class UserRepository:
    async def create(self, db, obj):
        db.add(obj)
        await db.commit()
        await db.refresh(obj)
        return obj
```