from celery import current_app as current_celery_app

from project.config import settings


def create_celery():
    """
    é uma função de fábrica que configura e retorna uma instância do aplicativo Celery. Em vez de criar uma nova
    instância do Celery, usamos current_app para que as tarefas compartilhadas funcionem conforme o esperado.

    celery_app.config_from_object(settings, namespace="CELERY")significa que todas as chaves de configuração
    relacionadas ao celery devem ser prefixadas com CELERY_. Por exemplo, para configurar o broker_url,
    devemos usarCELERY_BROKER_URL
    """
    celery_app = current_celery_app
    celery_app.config_from_object(settings, namespace="CELERY")

    return celery_app
