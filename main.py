import subprocess

from watchgod import run_process

from project import create_app

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


if __name__ == "__main__":
    celery_worker()
