from datetime import datetime
from app import db

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=False, nullable=False)
    first_name = db.Column(db.String(64), index=True, unique=False, nullable=False)
    phone = db.Column(db.String(20), index=True, unique=False, nullable=True)
    address = db.Column(db.String(120), index=True, unique=False, nullable=True)
    city = db.Column(db.String(64), index=True, unique=False, nullable=True)
    position = db.Column(db.String(120), index=True, nullable=False)
    created_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return f'<Employee {self.name} {self.first_name}>'
