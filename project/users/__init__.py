from fastapi import APIRouter

from . import views, models, tasks  # noqa

users_router = APIRouter(
    prefix="/users",
)
