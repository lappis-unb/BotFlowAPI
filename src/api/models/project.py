from django.db import models
from boogie.rest import rest_api

@rest_api()
class Project(models.Model):
    name = models.TextField()
    description = models.TextField()
