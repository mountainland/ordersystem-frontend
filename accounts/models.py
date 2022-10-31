from django.db import models

class Code(models.Model):
    code = models.CharField(max_length=8)
    created = models.DateTimeField(auto_now_add=True)
    used = models.BooleanField(default=False)

    def __str__(self):
        return 

    def __unicode__(self):
        return 

    def used(self, *args, **kwargs)
        if not self.used:
            self.used = True
        super(Code, self).save(*args, **kwargs)