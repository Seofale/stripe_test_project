# Simple test django project using stripe api



## Installation


```bash
git clone https://github.com/Dert2/stripe_test_project

docker-compose up

docker-compose exec python manage.py migrate
docker-compose exec python manage.py collectstatic
docker-compose exec python createsuperuser
```

## Usage
Create your items and orders and discounts in admin panel django.

http://0.0.0.0:8000/items/item/<item_id>/ returns rendered html with form to redirect for stripe buy form.

http://0.0.0.0:8000/items/order/<order_id>/ returns rendered html with form to redirect for stripe buy form with all items in your order.
