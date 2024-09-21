from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "atsuko_clone.settings")

celery_app = Celery("atsuko_clone")  # Replace 'your_project' with your project's name.

# Configure Celery using settings from Django settings.py.
celery_app.config_from_object("django.conf:settings", namespace="CELERY")

# Celery beat settings
celery_app.conf.beat_schedule = {}

# Load tasks from all registered Django app configs.
celery_app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
