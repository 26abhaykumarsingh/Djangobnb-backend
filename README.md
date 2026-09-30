# Djangobnb

A full-stack property rental application featuring a decoupled Next.js frontend and a Django REST Framework backend. This project includes secure JWT authentication, real-time messaging via WebSockets, property bookings, and a robust production deployment architecture.

**🌍 Live Demo:** [django-bnb-cd22.vercel.app](https://django-bnb-cd22.vercel.app/)

**🖥️ Frontend Repository:** [github.com/26abhaykumarsingh/DjangoBnb](https://github.com/26abhaykumarsingh/DjangoBnb)

**⚙️ Backend Repository:** [github.com/26abhaykumarsingh/Djangobnb-backend](https://github.com/26abhaykumarsingh/Djangobnb-backend)

---

## 🛠 Tech Stack

### Frontend
Built with **Next.js 16** and **React 19**, styled using **Tailwind CSS 4**.
* **Language:** TypeScript
* **State Management:** Zustand
* **Authentication:** HTTP-only cookies with JWT token refreshing via Next.js Edge Middleware
* **Real-time / WebSockets:** `socket.io-client` & `react-use-websocket`
* **UI Components:** `react-date-range` (booking calendars), `react-hot-toast` (notifications), `react-select`, `world-countries`

### Backend
Built with **Django 5** and **Django REST Framework (DRF)**.
* **Database:** PostgreSQL (`psycopg2-binary`) hosted on **Neon**
* **Authentication:** `djangorestframework-simplejwt`, `dj-rest-auth`, `django-allauth`
* **Real-time / WebSockets:** Django Channels with ASGI (`daphne`)
* **Media Handling:** `pillow` for image uploads

### Infrastructure & Deployment
* **Frontend Hosting:** Vercel
* **Backend Hosting:** Oracle Cloud Infrastructure (Ubuntu VM)
* **Database Hosting:** Neon
* **Containerization:** Docker & Docker Compose
* **Reverse Proxy & SSL:** Nginx with Let's Encrypt (Certbot) and DuckDNS

---

## ✨ Key Features
* **Stateless Authentication:** Secure JWT implementation with access and refresh tokens handled seamlessly by Next.js middleware to prevent session drops.
* **Property Listings & Bookings:** Browse properties, select date ranges, and calculate pricing dynamically.
* **Real-Time Chat:** Integrated WebSockets allowing hosts and guests to communicate instantly.
* **Resilient API Handling:** Frontend API service layer designed to intercept backend errors gracefully without crashing the client UI.
* **Cloud Object Storage / Media:** Seamless handling of property images from the Django backend to the Next.js frontend.
* **Advanced Search & Filtering:** Dynamic property search including geographical filtering (using world-countries) and precise date-availability checks (using react-date-range).

---

## 🚀 Local Setup Instructions

To run this project locally, you will need two terminal windows open—one for the backend and one for the frontend.

### 1. Backend Setup
Navigate to the backend directory and set up the Python environment:

```bash
# Create and activate virtual environment
python -m venv env
source env/bin/activate  # On Windows use: env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
# Create a .env.dev file and add your DATABASE_URL and SECRET_KEY

# Run migrations
python manage.py migrate

# Start the development server (uses Daphne for WebSockets)
python manage.py runserver
```


### 2. Frontend Setup

```bash
# Install dependencies
npm install

# Set up environment variables
# Create a .env.local file and add:
# NEXT_PUBLIC_API_HOST=http://localhost:8000

# Start the development server
npm run dev
