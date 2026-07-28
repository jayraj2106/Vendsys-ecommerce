# Vendsys — Production-Style E-commerce Backend (Django + DRF + Stripe)

Backend-focused Django system with real payment workflow, authentication, and scalable API design.

A production-oriented e-commerce backend built with **Django** and **Django REST Framework**, focused on real-world system design rather than basic CRUD.

Designed to handle **user authentication, cart management, order processing, and payment workflows**, with clean API architecture and optimized database interactions.

---

## Live Demo

https://vendsys-ecommerce.onrender.com

---

## Core Highlights

*  **JWT Authentication** (secure, API-ready for mobile/frontend clients)
*  **Session-Based Cart System** (lightweight, no DB overhead for guests)
*  **Order Management Flow** (cart → order → payment lifecycle)
*  **Stripe Integration** (checkout session + webhook handling)
*  **Search, Filtering & Pagination** (scalable product browsing)
*  **Optimized Queries** using `prefetch_related`
*  **Hybrid Architecture** (Django templates + REST APIs)

---

##  System Design Decisions

* **Session Cart vs DB Cart**
  Used session-based cart to reduce database load and simplify guest user flow.

* **JWT over Session Auth (for APIs)**
  Enables scalability for future mobile or React frontend integration.

* **Multiple Serializers Strategy**
  Separate serializers for list/detail views to optimize payload and performance.

* **Decoupled App Structure**
  Modular apps (`products`, `cart`, `orders`, `payments`) for maintainability and scalability.

---

## Tech Stack

* **Backend:** Django, Django REST Framework
* **Auth:** JWT (JSON Web Tokens)
* **Database:** PostgreSQL
* **Payments:** Stripe API
* **Frontend:** Django Templates + JavaScript (AJAX)

---

## Key API Endpoints

### Authentication

* `POST /api/register/` — Register user
* `POST /api/login/` — Obtain JWT tokens

---

### Products

* `GET /products/` — List products

Supports:

* `?search=` keyword search
* `?category=` filter
* `?min_price=`, `?max_price=` range filtering
* `?page=`, `?page_size=` pagination

---

### Cart

* `GET /api/cart/` — View cart
* `POST /api/cart/add/<product_id>/` — Add item
* `POST /api/cart/increase/<product_id>/` — Increase quantity
* `POST /api/cart/decrease/<product_id>/` — Decrease quantity

---

### Orders

* `GET /api/orders/` — List user orders
* `POST /api/orders/` — Create order
* `GET /api/orders/<id>/` — Order details

---

### Payments

* `POST /api/payments/create/` — Create Stripe checkout session
* `POST /api/payments/webhook/` — Handle Stripe events

---

## Project Structure

```bash
Vendsys/
├── users/
├── products/
├── cart/
├── orders/
├── payments/
├── api/
└── manage.py
```

---

## What This Project Demonstrates

* Designing **scalable REST APIs** with Django REST Framework
* Handling **stateful (session) vs stateless (JWT)** systems
* Implementing **real-world payment workflows (Stripe)**
* Structuring backend systems with **clean architecture principles**
* Writing efficient queries and managing **relational data models**

---

## Author

**Jayraj Parmar**
GitHub: https://github.com/jayraj2106
