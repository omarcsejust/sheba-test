from pydantic import BaseModel, Field, ConfigDict, field_validator, ValidationError
from typing import Optional
from datetime import datetime, timezone

'''
Right now, we are keeping all the schemas in this file.
In the future, we can split them into different files based on their functionality.
For example:
- auth.py: for authentication related schemas
- services.py: for service related schemas
- bookings.py: for booking related schemas
- categories.py: for category related schemas

'''

# Schemas for Admin Authentication
################################
class AdminLogin(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

# Services related schemas
###########################
class ServiceCreate(BaseModel):
    # Add validation based on requirements
    name: str
    description: str
    price: float
    category_id: int

class ServiceUpdate(BaseModel):
    # Add validation based on requirements
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    category_id: Optional[int] = None

class CategorySimple(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
    )
    id: int
    name: str

class ServiceOut(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
    )
    id: int
    name: str
    price: float
    description: str
    category: CategorySimple

# Bookings related schemas
###########################
class BookingCreate(BaseModel):
    customer_name: str = Field(..., example="John Doe", type='string')
    customer_phone: str # Need to add custom validation based on requirements
    service_id: int = Field(..., example=1, gt=0, type='integer')
    schedule_time: datetime

    @field_validator('customer_phone')
    def validate_phone(cls, v):
        if not v.isdigit():
            raise ValueError('Phone number must contain only digits')
        if len(v) < 10 or len(v) > 15:
            raise ValueError('Phone number must be between 10 and 15 digits')
        return v
    
    # @field_validator("schedule_time")
    # def validate_schedule_time(cls, v: datetime):
    #     if v.tzinfo is None:
    #         v = v.replace(tzinfo=timezone.utc)  # Make it aware by assuming UTC
    #     if v < datetime.now(timezone.utc):
    #         raise ValueError("Schedule time cannot be in the past")
    #     return v

class BookingOut(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
    )
    id: int
    customer_name: str
    customer_phone: str
    service: ServiceOut
    schedule_time: datetime
    status: str
    created_at: datetime
    updated_at: datetime
