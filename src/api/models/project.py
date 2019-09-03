from djongo import models
from boogie.rest import rest_api

class Project(models.Model):
    name = models.TextField()
    description = models.TextField()

    objects = models.DjongoManager()
