# webapp/utils/validators.py
import re

def validate_email(email):
    pattern = r'^[\w._%+-]+@[\w.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_password(password):
    return len(password) >= 8

# webapp/utils/formatters.py
from datetime import datetime

def format_date(date_string, format='%Y-%m-%d'):
    return datetime.strptime(date_string, '%Y-%m-%d').strftime(format)

def format_currency(amount, currency='USD'):
    if currency == 'USD':
        return f"${amount:.2f}"
    elif currency == 'EUR':
        return f"€{amount:.2f}"
    return f"{amount:.2f} {currency}"

# webapp/models/user.py
class User:
    def __init__(self, id, username, email):
        self.id = id
        self.username = username
        self.email = email
    
    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email
        }
