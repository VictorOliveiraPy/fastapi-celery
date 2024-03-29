import time

from celery import shared_task
# from celery.contrib import rdb

from project.users.views import api_call

"""Muitos recursos na web recomendam o uso celery.task. Isso pode causar importações circulares, pois você terá que 
importar a instância do Celery.

Costumávamos shared_tasktornar nosso código reutilizável, o que, novamente, 
requer current_appem em create_celery vez de criar uma nova instância do Celery. Agora, podemos copiar esse arquivo 
para qualquer lugar do aplicativo e ele funcionará conforme o esperado. 

"""


@shared_task
def divide(x, y):
    #    rdb.set_trace() debug
    time.sleep(4)
    return x / y


@shared_task()
def sample_task(email):
    api_call(email)
