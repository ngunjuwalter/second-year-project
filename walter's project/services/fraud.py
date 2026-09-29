from typing import Tuple, List
from models.user import User

def detect_fraud(amount: float, user: User) -> Tuple[bool, List[str]]:
    """
    Evaluates whether a transaction is fraudulent based on the officer's income.

    Args:
        amount (float): Transaction amount.
        user (User): Officer profile.

    Returns:
        Tuple[bool, List[str]]: Fraud flag and reasons.
    """
    reasons = []

    if amount > 2 * user.total_income:
        reasons.append(
            "Extremely suspicious transaction: exceeds double declared income"
        )
    elif amount > user.total_income:
        reasons.append(
            "Suspicious transaction: exceeds declared income"
        )

    return len(reasons) > 0, reasons
