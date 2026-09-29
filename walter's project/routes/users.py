from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from schemas.user import CreateUserRequest
from models.user import User
from db.session import get_db
from services.fraud import detect_fraud

router = APIRouter()



@router.get("/")
def root():
    return {"message": "ONSIGHT Fraud Detection API is running"}


@router.post("/users/", status_code=status.HTTP_201_CREATED)
def create_user(payload: CreateUserRequest, db: Session = Depends(get_db)):
    """
    Creates a new officer profile.
    """
    existing = db.query(User).filter(User.national_id == payload.national_id).first()
    if existing:
        raise HTTPException(
            status_code=400,
            detail="User already exists"
        )

    total = payload.basic_salary + payload.extra_income

    user = User(
        national_id=payload.national_id,
        name=payload.name,
        basic_salary=payload.basic_salary,
        extra_income=payload.extra_income,
        total_income=total,
    )

    db.add(user)
    db.commit()

    return {
        "message": "Officer profile created successfully.",
        "name": payload.name,
        "total_income": total,
    }


@router.get("/check-fraud/")
def check_fraud(national_id: str, amount: float, db: Session = Depends(get_db)):
    """
    Checks whether a transaction is fraudulent.
    """
    user = db.query(User).filter(User.national_id == national_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    is_fraud, reasons = detect_fraud(amount, user)

    return {
        "name":    user.name,
        "amount":  amount,
        "fraud":   is_fraud,
        "reasons": reasons,
    }