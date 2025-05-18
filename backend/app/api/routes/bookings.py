from fastapi import FastAPI, APIRouter, Depends, HTTPException
from fastapi_utils.cbv import cbv
from sqlalchemy.orm import Session
from app.core.deps import get_db, get_current_admin
from app.schemas import BookingCreate, BookingOut
from app.controllers.bookings import BookingController

router = APIRouter() # Create a new router instance

@cbv(router)
class BookingRouter:
    db: Session = Depends(get_db)

    @router.post("/", response_model=BookingCreate)
    def create_booking(self, booking: BookingCreate):
        """
        Create a new Booking.
        """
        booking_controller = BookingController(self.db)
        return booking_controller.create_booking(booking)
    
    @router.get("/", response_model=list[BookingOut])
    def get_bookings(self, offset: int = 0, limit: int = 10, current_admin = Depends(get_current_admin)):
        """
        Get all bookings.
        Bearer token is required for admin authorization.
        """
        booking_controller = BookingController(self.db)
        bookings = booking_controller.list_bookings(skip=offset, limit=limit)
        if not bookings:
            raise HTTPException(status_code=404, detail="No bookings found")
        return bookings

    @router.get("/{booking_id}/status")
    def get_booking_status(self, booking_id: int):
        """
        Get booking status.
        """
        booking_controller = BookingController(self.db)
        status = booking_controller.get_booking_status(booking_id)
        return {'status': status}