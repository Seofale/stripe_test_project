# Simple test django project using stripe api



## Installation
Clone repository
```bash
git clone https://github.com/Dert2/stripe_test_project
```

Create file .env in the root directory, and put these variables there
```bash
SECRET_KEY=...
DEBUG=...
STRIPE_API_SECRET_KEY=...
DB_ENGINE=...
DB_NAME=...
POSTGRES_USER=...
POSTGRES_PASSWORD=...
DB_HOST=...
DB_PORT=...
```
Then run the containers

```bash
docker-compose up

docker-compose exec python manage.py migrate
docker-compose exec python manage.py collectstatic
docker-compose exec python createsuperuser
```

## Usage
Create your items and orders and discounts in admin panel django.

http://0.0.0.0:8000/items/item/<item_id>/ returns rendered html with form to redirect for stripe buy form.

http://0.0.0.0:8000/items/order/<order_id>/ returns rendered html with form to redirect for stripe buy form with all items in your order.
