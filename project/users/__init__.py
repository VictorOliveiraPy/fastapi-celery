from fastapi import APIRouter
from . import models, tasks # noqa

users_router = APIRouter(
    prefix="/users",
)
