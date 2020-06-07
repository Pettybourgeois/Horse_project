from django.db import models

# Create your models here.
class Contact(models.Model):
    title = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField(max_length=1000)
    def __str__(self):
        return self.username
