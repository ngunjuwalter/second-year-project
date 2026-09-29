# ONSIGHT — KRA Integrity Reinforcement System

## Description

ONSIGHT is a backend fraud detection API designed to monitor financial transactions of officers by comparing transaction amounts against declared income.

The system flags suspicious transactions using rule-based logic (with future plans for machine learning integration).

This project is built as a modular, production-structured FastAPI application to simulate real-world backend engineering practices.

---

## Key Features

- Officer profile creation with income validation
- Fraud detection based on transaction vs declared income
- Modular and scalable backend architecture
- RESTful API design using FastAPI
- Database integration using SQLAlchemy
- Environment-based configuration management
- Automatic API documentation via Swagger UI

---

## Technologies Used

- Python 3.10+
- FastAPI
- SQLAlchemy
- MySQL
- Pydantic
- Uvicorn
- python-dotenv

---

## Installation Requirements

Make sure you have:

- Python 3.10+
- MySQL installed and running
- pip (Python package manager)
- Virtual environment tool (recommended)

---

## Installation Steps

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/onsight.git
cd onsight
```

### 2. Create and activate virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the root directory:

```env
DATABASE_URL=mysql+pymysql://user:password@localhost/fraud_db
```

### 5. Run the application

```bash
uvicorn app:app --reload
```

---

## API Usage

### Access API Docs

Open in browser:

http://127.0.0.1:8000/docs

---

### Create User (Officer Profile)

POST /users/

```json
{
  "national_id": "30303030",
  "name": "Mary Wanjiku",
  "basic_salary": 75000,
  "extra_income": 30000
}
```

---

### Check Fraud

GET /check-fraud/

```
/check-fraud/?national_id=30303030&amount=200000
```

---

### Example Response

```json
{
  "name": "Sheldon Afanda",
  "amount": 30000,
  "fraud": false,
  "reasons": []
}
```

---

## Configuration Options

| Variable     | Description                |
| ------------ | -------------------------- |
| DATABASE_URL | Database connection string |

Modify configurations in:

config.py

---

## Fraud Detection Logic

Current system uses rule-based logic:

- Transaction > total income → Suspicious
- Transaction > 2× income → Highly suspicious

Future upgrades:

- Machine Learning anomaly detection
- Behavioral profiling
- Risk scoring models

---

## Project Structure

```
fraud-detection/
│
│
├── config.py        # Environment & settings
│
├── db/
│   ├── base.py          # SQLAlchemy base
│   ├── session.py       # DB connection/session
│   └── seed.py          # Sample data
│
├── models/
│   └── user.py          # Database models
│
├── schemas/
│   └── user.py          # Request validation schemas
│
├── services/
│   └── fraud.py         # Fraud detection logic
│
└── routes/
│   └── users.py         # API endpoints
│
├── .env                     # Environment variables
├── requirements.txt
└── app.py                   # Application entry script
```

---

## Troubleshooting

### Database connection errors

- Ensure MySQL is running
- Verify credentials in `.env`
- Check database exists

### Tables not created

- Ensure Base.metadata.create_all() runs on startup
- Restart the server

### Import errors

- Check module paths (e.g. app. prefix)
- Ensure you're running from project root

### Changes not reflecting

- Use --reload with Uvicorn
- Restart server manually

---

## Contributing

Contributions are welcome.

Steps:

1. Fork the repository
2. Create a feature branch

```bash
git checkout -b feature-name
```

3. Commit changes

```bash
git commit -m "Add feature"
```

4. Push to GitHub

```bash
git push origin feature-name
```

5. Open a Pull Request

---

## License

This project is licensed under the MIT License.

---

## Disclaimer

This is a prototype system built for learning and demonstration purposes.  
Not production-ready for real financial fraud detection without further enhancements.

---
