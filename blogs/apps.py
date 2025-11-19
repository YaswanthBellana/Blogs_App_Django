from django.apps import AppConfig

class BlogsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blogs'

from django.core.signals import request_finished
from django.dispatch import receiver

@receiver(request_finished)
def handle_errors(sender, **kwargs):
    # Handle custom logic
    pass