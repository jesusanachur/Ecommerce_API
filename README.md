# Ecommerce API (Django + DRF + PostgreSQL)

Basic scaffold for an ecommerce API with:
- Users (register, JWT auth)
- Products (CRUD)
- Cart (per-user)
- Orders
- Roles: `admin` / `client`

Setup (local):

1. Create a virtualenv and install dependencies:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

2. Configure environment variables (example `.env`):

```
DJANGO_SECRET_KEY=replace-me
DJANGO_DEBUG=True
POSTGRES_DB=ecommerce_db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
```

3. Run migrations and create a superuser:

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

API endpoints (examples):
- `POST /api/accounts/register/` - register
- `POST /api/auth/token/` - obtain JWT
- `GET /api/accounts/me/` - profile
- `GET/POST /api/products/` - list/create (create requires admin)
- `GET/POST /api/cart/` - view cart / add item
- `POST /api/orders/` - create order
