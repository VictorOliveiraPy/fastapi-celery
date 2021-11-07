from celery import shared_task
import time

"""Muitos recursos na web recomendam o uso celery.task. Isso pode causar importações circulares, pois você terá que 
importar a instância do Celery.

Costumávamos shared_tasktornar nosso código reutilizável, o que, novamente, 
requer current_appem em create_celery vez de criar uma nova instância do Celery. Agora, podemos copiar esse arquivo 
para qualquer lugar do aplicativo e ele funcionará conforme o esperado. 

"""


@shared_task
def divide(x, y):
    time.sleep(5)
    return x / y
