from django.db import models

class City(models.Model):
    name = models.CharField(max_length=50)
    short = models.CharField(max_length=5)
    delivery_date = models.DateTimeField(auto_now_add=False)