from fastapi import FastAPI, APIRouter, Depends, HTTPException
from fastapi_utils.cbv import cbv
from sqlalchemy.orm import Session
from app.core.deps import get_db, get_current_admin
from app.schemas import ServiceCreate, ServiceUpdate, ServiceOut
from app.controllers.services import ServiceController

router = APIRouter() # Create a new router instance

@cbv(router)
class ServiceRouter:
    db: Session = Depends(get_db)

    @router.post("/", response_model=ServiceOut)
    def create_service(self, service: ServiceCreate, current_admin = Depends(get_current_admin)):
        """
        Create a new service.
        Bearer token is required for admin authorization.
        """
        service_controller = ServiceController(self.db)
        return service_controller.create_service(service)

    @router.get("/", response_model=list[ServiceOut])
    def get_services(self, offset: int = 0, limit: int = 10):
        """
        Get all services.
        """
        services = ServiceController(self.db).list_services(skip=offset, limit=limit)
        if not services:
            raise HTTPException(status_code=404, detail="No services found")
        return services

    @router.put("/{service_id}", response_model=ServiceOut)
    def update_service(self, service_id: int, service: ServiceUpdate, current_admin = Depends(get_current_admin)):
        """
        Update a service.
        Bearer token is required for admin authorization.
        """
        service_controller = ServiceController(self.db)
        return service_controller.update_service(service_id, service)
    
    @router.delete("/{service_id}")
    def delete_service(self, service_id: int, current_admin = Depends(get_current_admin)):
        """
        Delete a service.
        Bearer token is required for admin authorization.
        """
        service_controller = ServiceController(self.db)
        service_controller.delete_service(service_id)
        return {"message": "Service deleted successfully"}