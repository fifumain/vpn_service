from django.urls import path

from . import views

urlpatterns = [
    path("create/", views.create_site, name="create_site"),  # Создание сайта
    path(
        "site/<int:site_id>/statistics/", views.site_statistics, name="site_statistics"
    ),
    path("<str:site_name>/<path:path>/", views.proxy_site, name="proxy_site_with_path"),
    path("<str:site_name>/", views.proxy_site, name="proxy_site"),
]
