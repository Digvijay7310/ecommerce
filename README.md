

# E-commerce Project (Django + Tailwind CDN)

## Project Overview
This is a Django-based e-commerce application with a simple, responsive front-end using Tailwind CSS via CDN. Users can browse products, view details, and search by name, description, or category. Admins have full CRUD access to manage products.

---

## Apps

1. **products**  
   - Manages product data.
   - Product details include main image and optional additional images.
   - Supports search functionality.

2. **accounts**  
   - Handles user authentication (login/logout/signup).

3. **cart**  
   - Allows logged-in users to add products to the cart.

---

## Features Implemented

### User (Customer)
- View all products and their details.
- View product images and thumbnails.
- Search products by name, description, or category.
- Add products to cart (login required).

### Admin
- Create, update, and delete products via Django Admin.
- Full CRUD access to manage the product catalog.

---

## Tailwind CSS
- Integrated via **CDN**, no Node.js required.
- Styles applied for responsive product pages and grids.

---

## Search Functionality
- Products are searchable by:
  - `name`
  - `description`
  - `category__name`
- Case-insensitive search using Django `icontains`.

---

## Setup Instructions (so far)
1. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   venv\Scripts\activate
