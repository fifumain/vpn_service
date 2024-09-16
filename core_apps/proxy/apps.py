from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ProxyConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core_apps.proxy"
    verbose_name = _("Proxy")
