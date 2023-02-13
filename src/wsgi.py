import os

from configurations.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_CONFIGURATION", "Prod")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "src.settings")

application = get_wsgi_application()
