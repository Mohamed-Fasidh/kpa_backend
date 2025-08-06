# KPA Form Backend

This is a backend API built using **FastAPI** and **PostgreSQL** for managing **Wheel Specification Form** submissions. It allows users to submit wheel specifications and retrieve them via RESTful endpoints.

---

## 🛠 Tech Stack

- **FastAPI** (Python)
- **SQLAlchemy** (ORM)
- **PostgreSQL**
- **Pydantic**
- **Uvicorn** (for development server)
- **dotenv** (for environment variables)

---

## 📦 Project Structure

kpa_backend/
│
├── app/
│ ├── init.py
│ ├── main.py # FastAPI app entry point
│ ├── database.py # DB connection setup
│ ├── models.py # SQLAlchemy models
│ ├── schemas.py # Pydantic schemas
│ ├── crud.py # CRUD operations
│ └── routes/
│ └── wheel_specification.py # API router
│
├── .env # Environment variables
├── requirements.txt
└── README.md

---

## 📄 .env Example

Create a `.env` file in the root:

.env

DATABASE_URL=postgresql://username:password@localhost:5432/your_db_name
🐍 Install Dependencies

pip install -r requirements.txt


🚀 Run the Server

uvicorn app.main:app --reload
The server will start at http://127.0.0.1:8000

📬 API Endpoints
1. Create Wheel Specification
POST /api/forms/wheel-specifications

Request JSON:


{
  "wheel_number": "W123",
  "diameter": 850.0,
  "thickness": 35.5,
  "pressure": 100.0,
  "remarks": "Initial inspection"
}
Response:

{
  "wheel_number": "W123",
  "diameter": 850.0,
  "thickness": 35.5,
  "pressure": 100.0,
  "remarks": "Initial inspection",
  "id": 1
}
2. Get All Wheel Specifications
GET /api/forms/wheel-specifications

Response:


[
  {
    "wheel_number": "W123",
    "diameter": 850.0,
    "thickness": 35.5,
    "pressure": 100.0,
    "remarks": "Initial inspection",
    "id": 1
  },
  
