from django.db import models
from boogie.rest import rest_api

from . import Project

import jsonfield


@rest_api()
class Utter(models.Model):
    name = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    possibilities = jsonfield.JSONField()
