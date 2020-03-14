import os
from pathlib import Path

from fastapi import APIRouter, Body
from pydantic.networks import EmailStr
import boto3

router = APIRouter()

cwd = Path(__file__).resolve().parent

env_file = Path(cwd.parent.parent.parent.parent, "local.env")

with env_file.open() as env_file_obj:
    for line in env_file_obj:
        key, value = line.split(":")
        os.environ[key.strip()] = value.strip()


cognito_id = os.environ.get('COGNITO_CLIENT_ID')


@router.get("/login")
def login():
    return {"detail": "Login Not Implemented"}


@router.post("/signup")
def signup(
    email: EmailStr = Body(...),
    name: str = Body(...),
    password: str = Body(...)
):
    client = boto3.client('cognito-idp', 'us-east-1')

    response = client.sign_up(
        ClientId=cognito_id,
        Username=email,
        Password=password,
        UserAttributes=[
            {
                'Name': 'name',
                'Value': name
            },
        ],
    )
    print(response)
    return {"detail": f"{name}"}


@router.post("/confirm")
def confirm(
    email: EmailStr = Body(...),
    confirmation_code: str = Body(...)
):
    client = boto3.client('cognito-idp', 'us-east-1')

    response = client.confirm_sign_up(
        ClientId=cognito_id,
        Username=email,
        ConfirmationCode=confirmation_code
    )
    print(response)
    return {"detail": f"{email} confirmed"}


@router.get("/logout")
def logout():
    return {"detail": "Logout Not Implemented"}
