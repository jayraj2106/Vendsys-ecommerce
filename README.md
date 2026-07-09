# E-Commerce Backend API (Django + DRF)

This project is a backend implementation of a basic e-commerce system built using Django and Django REST Framework. It includes core features like product management, cart handling, and order processing, designed with clean structure and efficient database usage.

---

## Features

- Product list and detail APIs
- Cart system with add/update functionality
- Order creation from cart
- User-specific order history
- Separate order list and order detail APIs
- Nested serializers for order items
- Optimized queries using `prefetch_related`

---

## Tech Stack

- Python
- Django
- Django REST Framework
- SQLite

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

## Future Improvements

- JWT authentication
- Search and filtering
- Pagination
- Payment integration

---

## Author

Jayraj Parmar
GitHub: https://github.com/jayraj2106

---
