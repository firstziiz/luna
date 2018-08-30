from django.db import models
from django.conf import settings

from core.models import Timestamp


# Create your models here.
class Account(Timestamp):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=140, default='')

    facebook_token = models.CharField(max_length=140, default='')

    def __str__(self):
        return f'User: {self.user.username}'

    @property
    def role(self):
        user_group = self.user.groups.first()
        return user_group.name.capitalize() if user_group else None
