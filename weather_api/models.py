from django.db import models

# Create your models here.

class Weather(models.Model):
    city = models.CharField(max_length=100)
    temperature = models.FloatField()
    humidity = models.FloatField()
    description = models.CharField(max_length=255)
    icon = models.CharField(max_length=100)

    def __str__(self):
        return self.city