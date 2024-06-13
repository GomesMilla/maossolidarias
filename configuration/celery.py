import os
from celery import Celery
from django.conf import settings

# Substitua 'your_project_name' pelo nome do seu projeto Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'configuration.settings')

app = Celery('configuration')

# Configurações do Celery a partir das configurações do Django
app.config_from_object('django.conf:settings', namespace='CELERY')

# Descobre e carrega automaticamente as tarefas definidas nos apps do Django
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')