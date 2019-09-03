from djongo import models
from boogie.rest import rest_api

class Story(models.Model):
    content = models.DictField(default={'list':[]})
    project = models.ObjectIdField(blank=False)

    objects = models.DjongoManager()
