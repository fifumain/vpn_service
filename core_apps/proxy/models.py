from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models

User = get_user_model()


class Site(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    url = models.URLField()

    def __str__(self):
        return self.name


# statistics for visited websites
class UsageStats(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    page_visits = models.PositiveIntegerField(default=0)
    data_sent = models.BigIntegerField(default=0)
    data_received = models.BigIntegerField(default=0)

    def __str__(self):
        return f"Stats for {self.site.name}"
