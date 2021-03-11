from django.db import models
from django.conf import settings


class UserProfile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    USER_TYPE_1 = 1
    USER_TYPE_2 = 2
    USER_TYPE_CHOICES = (
        (USER_TYPE_1, 'Type 1'),
        (USER_TYPE_2, 'Type 2'),
    )
    user_type = models.IntegerField(choices=USER_TYPE_CHOICES)

    def __str__(self):
        return f'{self.user.email} ({self.user_type})'
