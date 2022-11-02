from django.apps import AppConfig
from .signals import save_mail_track_object

class MailtrackingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'MailTracking'

    # def ready(self) -> None:
    #     save_mail_track_object()
