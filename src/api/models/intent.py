from djongo import models
from boogie.rest import rest_api

class Intent(models.Model):
    name = models.TextField()
    samples = models.DictField(default={'list':[]})

    objects = models.DjongoManager()
