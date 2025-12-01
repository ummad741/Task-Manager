

## Core Layer (Common utilities)

### Bunda quyidagilar bo‘ladi:
- #### Common exceptions
- #### Base repository
- #### Base service
- #### Base model (timestamp, id)
- #### .env loading
- #### Settings (Pydantic BaseSettings)
- #### Constants
- #### Application level configs

### ➡️ Loyihada ko‘p marta qayta ishlatiladigan narsa shu yerda.


### Umumiy konfiguratsiya.
- #### config.py → Settings (ENV, DB_URL, JWT_SECRET)
- #### security.py → Password hashing, token validation
- #### exceptions.py → global errors