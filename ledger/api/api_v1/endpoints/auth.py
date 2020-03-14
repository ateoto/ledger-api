from fastapi import APIRouter, Body
from pydantic.networks import EmailStr

router = APIRouter()


@router.get("/login")
def login():
    return {"detail": "Login Not Implemented"}


@router.post("/signup")
def signup(
    email: EmailStr = Body(...),
    name: str = Body(...),
    password: str = Body(...)
):
    return {"detail": f"SignUp Not Implemented {name}"}


@router.get("/logout")
def logout():
    return {"detail": "Logout Not Implemented"}
