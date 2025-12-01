# api/
- ### UZ: FastAPI routerlari, endpointlar va HTTP-layer.
- ### EN: FastAPI routers and HTTP endpoints.
## API Layer (FastAPI routers/controllers)
### Nima uchun javob beradi?

- #### HTTP qabul qilish (GET, POST…)
- #### Request → Pydantic → Service → Response jarayoni
- #### Auth middleware
- #### Response formatting
- #### Error handling (HTTPException)
  
### API hech qachon:
- #### ❌ Database bilmaydi
- #### ❌ SQL yozmaydi
- #### ❌ Business rule bilmaydi

### ➡️ Faqat kirish/chiqish interfeysi.

### Routing qismi.

- #### endpoints/ → Endpointlar (/users, /tasks, /auth)

- #### deps.py → Depends funksiyalar (current_user, db_session, role check)

- #### v1/router.py → API versioning