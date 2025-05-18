# app/seeder/category.py
from sqlalchemy.orm import Session
from .models import Category
from .models import AdminUser
from app.core.security import get_password_hash  # Assuming you have a hash_password function

def seed_admin_users(db: Session):
    if db.query(AdminUser).first():
        return  # Table already has data, skip

    default_admins = [
        {"username": "admin", "password": "admin123"},
        {"username": "superuser", "password": "superuser123"},
    ]

    for admin in default_admins:
        hashed_password = get_password_hash(admin["password"])  # Assuming you have a hash_password function
        db.add(AdminUser(username=admin["username"], hashed_password=hashed_password))

    db.commit()

def seed_categories(db: Session):
    if db.query(Category).first():
        return  # Table already has data, skip

    default_categories = ["Haircut", "Massage", "Plumbing", "Car Wash"]

    for name in default_categories:
        db.add(Category(name=name))

    db.commit()
