from django.db import models
from django.contrib.auth.models import User

class account(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name
