import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookstore-api.settings')  # Substitua 'seu_projeto' pelo nome do seu projeto Django

application = get_wsgi_application()
