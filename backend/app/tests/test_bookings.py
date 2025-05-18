import pytest
from datetime import datetime
from app.db.models import Booking, Service
from app.db.seeds import seed_categories

@pytest.mark.asyncio
async def test_create_booking(client, db):
    # Seed a service first
    seed_categories(db)
    service = Service(name="Test Service 1", price=100, description="This is a nice service!", category_id=1)
    db.add(service)
    db.commit()
    db.refresh(service)

    payload = {
        "customer_name": "John",
        "customer_phone": "01765708783",
        "service_id": service.id,
        "schedule_time": "2025-05-15T14:00:00"
    }
    response = await client.post("/api/v1/bookings/", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["customer_name"] == "John"
    assert data["service_id"] == service.id

@pytest.mark.asyncio
async def test_get_booking_status(client, db):
    booking = Booking(customer_name="Alice", customer_phone="01765708783", service_id=1, schedule_time=datetime.now(), status="pending")
    db.add(booking)
    db.commit()
    db.refresh(booking)

    response = await client.get(f"/api/v1/bookings/{booking.id}/status")
    assert response.status_code == 200
    assert response.json()["status"] == "pending"
