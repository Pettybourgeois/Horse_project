from django.db import models
from datetime import datetime

# Create your models here.
class Machine(models.Model):
    title = models.CharField(max_length=100)
    function = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    main_photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    machine_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.title