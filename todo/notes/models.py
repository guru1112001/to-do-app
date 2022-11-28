from django.db import models

# Create your models here.
class todo(models.Model):
    title=models.CharField(max_length=600)
    description=models.TextField()
    status=models.BooleanField(default=False)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return self.title
