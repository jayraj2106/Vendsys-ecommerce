#  E-commerce Web Application

A full-stack Django e-commerce application with server-rendered UI and dynamic cart functionality using JSON responses.

---

## Features

- User authentication (Login/Register)
- Product listing and detail pages
- Add to cart (dynamic, JSON-based)
- Update/remove items from cart
- Order placement system
- Server-rendered HTML pages (Django templates)

---

## 🛠 Tech Stack

- Python
- Django
- HTML, CSS (Django Templates)
- JavaScript (AJAX for cart)
- SQLite / PostgreSQL

---
## Base URL

https://vendsys-ecommerce.onrender.com


## 📘 API Endpoints

### Authentication

- `POST /api/register/` - Register new user  
- `POST /api/login/` - Login user (JWT) & Obtain access & refresh tokens  
 
---

### Products

- `GET /products/` — List all products

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
