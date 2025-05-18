from sqlalchemy.orm import Session, joinedload
from fastapi import HTTPException, status
from app.db.models import Service, Booking
from app.schemas import BookingCreate


class BookingController:
    def __init__(self, db: Session):
        self.db = db

    def create_booking(self, data: BookingCreate):
        service = self.db.query(Service).filter(Service.id == data.service_id).first()
        if not service:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Service not found")
        
        booking = Booking(
            service_id=data.service_id,
            customer_name=data.customer_name,
            customer_phone=data.customer_phone,
            schedule_time=data.schedule_time,
        )

        self.db.add(booking)
        self.db.commit()
        self.db.refresh(service)
        return booking

    def get_booking_status(self, booking_id: int):
        booking = self.db.query(Booking).filter(Booking.id == booking_id).first()
        if not booking:
            raise HTTPException(status_code=404, detail="Booking not found!")
        return booking.status

    def list_bookings(self, skip: int = 0, limit: int = 10):
        """
        Get all services with pagination.
        """
        return (
            self.db.query(Booking)
            .options(joinedload(Booking.service))  #loads category with service
            .offset(skip)
            .limit(limit)
            .all()
        )
