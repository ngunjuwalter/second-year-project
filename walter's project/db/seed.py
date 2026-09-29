from db.session import SessionLocal
from models.user import User

def insert_sample_data():
    """
    Inserts initial sample data into the database if not already present.
    """
    db = SessionLocal()

    try:
        sample_officers = [
            ("30303030", "Mary",      75_000,  30_000),
            ("87654321", "Joseph",   120_000,  33_000),
            ("21314151", "Catherine", 180_000, 70_000),
        ]

        for uid, name, salary, extra in sample_officers:
            existing = db.query(User).filter(User.national_id == uid).first()
            if not existing:
                total = salary + extra
                db.add(User(
                    national_id=uid,
                    name=name,
                    basic_salary=salary,
                    extra_income=extra,
                    total_income=total,
                ))
        db.commit()
    finally:
        db.close()
