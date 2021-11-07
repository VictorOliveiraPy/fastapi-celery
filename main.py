from fastapi import FastAPI
from celery import Celery
from project import create_app

app = create_app()

celery = app.celery_app

celery = Celery(
    __name__,
    broker="redis://127.0.0.1:6379/0",
    backend="redis://127.0.0.1:6379/0"
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@celery.task
def dividi(x, y):
    import time
    time.sleep(5)
    return x / y