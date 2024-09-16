from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("core_apps.users.urls")),
    path("proxy/", include("core_apps.proxy.urls")),
]
