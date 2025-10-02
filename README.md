# Appointment Booking with Stripe Payment Gateway (Django)

This is a simple Django project that demonstrates:

- A model for **Appointment** with fields:
  - `provider_name`
  - `appointment_time`
  - `client_email`
- A form to create an appointment
- A mock **Stripe payment flow** using test keys (no webhooks, just PaymentIntent/CheckoutSession)
- Simple success and cancel pages

---

## Features

- Book an appointment online
- Store appointments in SQLite (default Django DB)
- Stripe test payments
- Bootstrap-styled UI (responsive and clean)

---

## 🚀 Quick Start with Docker (Recommended)

If you have Docker installed, you can run the entire project using one command.

### 1. Start the Project

```bash
docker-compose up --build
```

This will:

* Build the Docker image
* Install dependencies
* Apply migrations
* Start the Django development server on `http://localhost:8000`

### 2. Stop and Remove Containers

To shut everything down cleanly:

```bash
docker-compose down
```

---

## 🐍 Manual Setup (Without Docker)

If you prefer to run the project manually using Python and pip:

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd appointments
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv

# On macOS / Linux
source venv/bin/activate

# On Windows
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the root of your project directory:

```ini
STRIPE_SECRET_KEY=<paste your stripe secret key here>
STRIPE_PUBLISHABLE_KEY=<paste your stripe publishable key here>
```

Replace the keys above with your **actual** Stripe keys.

### 5. Apply Migrations

```bash
python manage.py migrate
```

### 6. Run the Development Server

```bash
python manage.py runserver
```

Visit [http://localhost:8000/](http://localhost:8000/) to book an appointment.

---

## 💳 Testing Stripe Payments

Use Stripe’s test card details:

* **Card Number**: `4242 4242 4242 4242`
* **Expiry**: Any future date (e.g. 12/34)
* **CVC**: Any 3 digits (e.g. 123)


More test cards available at [Stripe Testing Docs](https://stripe.com/docs/testing).

---


## ✅ Requirements

* Python 3.9+
* Django 5.x
* Stripe Python SDK
* python-dotenv
* pytest (for testing)


