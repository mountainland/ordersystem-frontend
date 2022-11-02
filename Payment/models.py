from django.db import models

class Payment_method(models.Model):
    name = models.CharField(max_length=10)
    display_name = models.CharField(max_length=10)
    info = models.CharField(max_length=30)
    
    def __str__(self):
        return u'%s' % self.name
    