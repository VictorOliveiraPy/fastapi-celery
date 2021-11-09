from project import create_app
from watchgod import run_process
import subprocess

app = create_app()

celery = app.celery_app


def celery_worker():
    def run_worker():
        subprocess.call(
            ["celery", "-A", "main.celery", "worker", "--loglevel=info"]
        )

    run_process("./project", run_worker)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@celery.task
def dividi(x, y):
    import time
    time.sleep(4)
    return x / y


if __name__ == "__main__":
    celery_worker()