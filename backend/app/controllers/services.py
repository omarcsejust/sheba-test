from sqlalchemy.orm import Session, joinedload
from fastapi import HTTPException, status
from app.db.models import Service, Category
from app.schemas import ServiceCreate, ServiceUpdate


class ServiceController:
    def __init__(self, db: Session):
        self.db = db

    def create_service(self, data: ServiceCreate):
        category = self.db.query(Category).filter(Category.id == data.category_id).first()
        if not category:
            raise HTTPException(status_code=404, detail="Category not found")

        service = Service(
            name=data.name,
            description=data.description,
            price=data.price,
            category_id=data.category_id
        )
        self.db.add(service)
        self.db.commit()
        self.db.refresh(service)
        return service

    def get_service(self, service_id: int):
        service = self.db.query(Service).filter(Service.id == service_id).first()
        if not service:
            raise HTTPException(status_code=404, detail="Service not found")
        return service

    def list_services(self, skip: int = 0, limit: int = 10):
        """
        Get all services with pagination.
        """
        return (
            self.db.query(Service)
            .options(joinedload(Service.category))  #loads category with service
            .offset(skip)
            .limit(limit)
            .all()
        )

    def update_service(self, service_id: int, data: ServiceUpdate):
        service = self.get_service(service_id)

        if data.category_id:
            category = self.db.query(Category).filter(Category.id == data.category_id).first()
            if not category:
                raise HTTPException(status_code=404, detail="Category not found")

        for key, value in data.model_dump(exclude_unset=True).items():
            setattr(service, key, value)

        self.db.commit()
        self.db.refresh(service)
        return service

    def delete_service(self, service_id: int):
        service = self.get_service(service_id)
        if not service:
            raise HTTPException(status_code=404, detail="Service not found")
        self.db.delete(service)
        self.db.commit()
