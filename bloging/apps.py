from django.apps import AppConfig
from .views import BlogDetailView


class BlogingConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "bloging"

    def ready(self):
        from .startup import send_congratulation_mail
        if BlogDetailView.model.view_count == 100:
            send_congratulation_mail()
