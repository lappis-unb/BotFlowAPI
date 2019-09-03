from djongo import models
from boogie.rest import rest_api

class Utter(models.Model):
    name = models.TextField()
    possibilities = models.DictField(default={'list':[]})
    project = models.ObjectIdField(blank=False)

    objects = models.DjongoManager()
