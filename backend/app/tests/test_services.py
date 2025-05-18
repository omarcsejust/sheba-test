import pytest
from app.db.models import Service, Category
from app.db.seeds import seed_categories

def seed_services(db):
    seed_categories(db)
    s1 = Service(name="Test Service 1", price=100, description="This is a nice service!", category_id=1)
    s2 = Service(name="Test Service 2", price=200, description="This is a nice service!", category_id=1)
    db.add_all([s1, s2])
    db.commit()
    db.refresh(s1)
    db.refresh(s2)

@pytest.mark.asyncio
async def test_list_services(client, db):
    seed_services(db)
    response = await client.get("/api/v1/services/")
    assert response.status_code == 200
    services = response.json()
    assert isinstance(services, list)
    assert len(services) >= 2
    assert services[0]["name"] == "Test Service 1"
    assert services[1]["name"] == "Test Service 2"
    assert services[0]["price"] == 100
    assert services[1]["price"] == 200
