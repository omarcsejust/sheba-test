from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_utils.cbv import cbv
from sqlalchemy.orm import Session
from app.core.deps import get_db
from app.schemas import Token, AdminLogin
from app.db.models import AdminUser
from app.core.security import create_access_token, verify_password

router = APIRouter() # Create a new router instance

# Note: The OAuth2PasswordRequestForm expects a username and password in application/x-www-form-urlencoded format

@cbv(router)
class AuthRouter:
    @router.post("/admin-login", response_model=Token)
    def login(self, form: OAuth2PasswordRequestForm=Depends(), db: Session = Depends(get_db)):
        admin = db.query(AdminUser).filter(AdminUser.username == form.username).first()
        if not admin or not verify_password(form.password, admin.hashed_password):
            raise HTTPException(status_code=401, detail="Incorrect credentials")

        token = create_access_token(data={"sub": admin.username})
        return {"access_token": token, "token_type": "bearer"}
