from django.db import models


class Code(models.Model):
    code = models.CharField(max_length=8)
    created = models.DateTimeField(auto_now_add=True)
    used = models.BooleanField(default=False)
