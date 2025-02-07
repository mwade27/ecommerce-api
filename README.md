# ecommerce-api

Frontend- React
Backend- Flask (Python)
Authentication- JWT
Payment Gateway- Stripe API
API testing- Postman
Deployment- Docker + AWS/Heroku

Phase 1: Project Setup
Goal: Set up the basic project structure and environment.
🔹 Tasks:

Initialize a Git repository (git init) for version control.
Set up a virtual environment in Python (venv or conda).
Install necessary Flask dependencies (pip install flask flask-jwt-extended flask-sqlalchemy flask-bcrypt flask-cors).
Set up MySQL database and create a connection in db.py.
Write a basic Flask API with /ping route to test.
🔹 Completion Criteria:

Run flask run successfully.
/ping endpoint returns "pong" when accessed via Postman


Phase 2: User Authentication System
Goal: Implement JWT-based authentication (Signup, Login, Logout).
🔹 Tasks:

Create User model in models.py (username, email, password hash, is_admin).
Implement password hashing using bcrypt.
Create register & login routes (auth.py).
Implement JWT authentication using flask-jwt-extended.
Test with Postman:
Register a user (POST /register).
Login and receive JWT token (POST /login).
Protect a test route (GET /protected).
🔹 Completion Criteria:

JWT token returned on successful login.
Protected routes reject unauthorized requests.

Phase 3: Product Management API
Goal: Create CRUD operations for Product management.
🔹 Tasks:

Create Product model in models.py (name, description, price, stock).
Implement CRUD routes in product.py:
GET /products → Fetch all products.
POST /products (Admin only) → Add new product.
PUT /products/:id (Admin only) → Update product details.
DELETE /products/:id (Admin only) → Delete a product.
Implement admin-only access using JWT role-based authentication.
Test all endpoints via Postman.
🔹 Completion Criteria:

Admins can add, update, delete products.
Users can view products but not modify them

Phase 4: Shopping Cart Functionality
Goal: Allow users to add, remove, and view items in their shopping cart.
🔹 Tasks:

Create Cart model in models.py (user_id, product_id, quantity).
Implement Cart routes (cart.py):
POST /cart → Add item to cart.
GET /cart → View user’s cart.
DELETE /cart/:id → Remove item from cart.
Ensure cart is linked to the logged-in user (JWT authentication).
🔹 Completion Criteria:

Users can add/remove items.
Cart updates correctly

Phase 5: Checkout & Stripe Payment
Goal: Implement payment processing using Stripe.
🔹 Tasks:

Install Stripe SDK (pip install stripe).
Create Order model (models.py) to store order details.
Implement checkout route (checkout.py):
Calculate total price.
Create Stripe Payment Intent.
Return Stripe client_secret to frontend.
Update order status on success.
Test Stripe integration in Postman.
🔹 Completion Criteria:

Users can make payments.
Orders get recorded in the database

Phase 6: Build a Simple Frontend
Goal: Create a minimal frontend using React.
🔹 Tasks:

Set up a React project (npx create-react-app).
Install dependencies (axios, react-router-dom).
Build Authentication Pages:
Login.js
Register.js
Create Product Listing Page (ProductList.js).
Implement Cart UI and integrate API.
🔹 Completion Criteria:

Users can view products, log in, add to cart.

Phase 7: Admin Panel
Goal: Create a protected admin dashboard.
🔹 Tasks:

Build Admin UI (AdminDashboard.js).
Implement:
Add Products
Edit Products
Manage Orders
Secure it using JWT role-based authentication.
🔹 Completion Criteria:

Only admins can manage products/orders.

Final Phase: Deployment
Goal: Deploy to AWS/Heroku and secure the project.
🔹 Tasks:

Containerize app using Docker.
Deploy backend on AWS EC2/Heroku.
Deploy frontend on Netlify/Vercel.
Set up production database (AWS RDS).
Secure API with CORS & HTTPS.
🔹 Completion Criteria:

Users can access the platform online.
Stripe payments work in production.