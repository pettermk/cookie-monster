from django.db import models


# Create your models here.

class Cookie(models.Model):
    time_sent = models.DateTimeField(auto_now_add=True)
    cookie = models.TextField()

    class Meta:
        ordering = ['time_sent']