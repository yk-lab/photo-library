from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class MastersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "masters"
    verbose_name = _("Masters")

    def ready(self):
        from . import signals  # noqa: F401
