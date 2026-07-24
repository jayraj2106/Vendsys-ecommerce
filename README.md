#  E-commerce Web Application

Built a full-stack e-commerce web application using Django and Django REST Framework with features like JWT authentication, product search & filtering, dynamic cart management, order processing, and Stripe payment integration. Implemented RESTful APIs with pagination and optimized database queries for performance.

---

## Features

- User authentication (Login/Register with JWT)
- Product listing and detail pages
- Product search functionality
- Category-based product filtering
- Pagination support (page count & item count)
- Add to cart (dynamic, JSON-based)
- Update/remove items from cart
- Order placement system
- Stripe payment integration
- Server-rendered HTML pages (Django templates)

---

## Tech Stack

- Python
- Django
- HTML, CSS (Django Templates)
- JavaScript (AJAX for cart)
- PostgreSQL

---
## Base URL

https://vendsys-ecommerce.onrender.com


## API Endpoints

### Authentication

- `POST /api/register/` - Register new user  
- `POST /api/login/` - Login user (JWT) & Obtain access & refresh tokens  
 
---

### Products

- `GET /products/` — List all products
    - Supports:
    - `?search=<query>` — Search products
    - `?category=<category_name>` — Filter by category
    - `?min_price=<value>` — Filter products with price ≥ value  
    - `?max_price=<value>` — Filter products with price ≤ value  
    - `?page=<number>` — Pagination page
    - `?page_size=<count>` — Items per page

---

### Cart

- `GET /api/cart/` - View cart (Auth required)  
- `POST /api/cart/add/<product_id>/` - Add product to cart  
- `POST /api/cart/increase/<product_id>/` - Increase product quantity  
- `POST /api/cart/decrease/<product_id>/` - Decrease product quantity  

---

### Orders
- `GET /api/orders/` - Get user's all orders
- `POST /api/orders/` - Create a new order
- `GET /api/orders/<product_id>/` - Get a specefic order

---

### Payments

- `POST /api/payments/create/` - Create Stripe checkout session  
- `POST /api/payments/webhook/` - Stripe webhook (no auth required)  

---

## Project Structure

```bash
Vendsys/
├── users/
├── products/
├── cart/
├── orders/
├── api/
├── manage.py
```

---

## What I Learned

- Structuring Django projects into modular apps
- Designing REST APIs using DRF
- Working with relational models (Order, OrderItem, Product)
- Using different serializers for list and detail views
- Optimizing database queries for better performance
- Handling user-based data securely

---

## Author

Jayraj Parmar
GitHub: https://github.com/jayraj2106

---
