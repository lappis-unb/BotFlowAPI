from django.db import models
from boogie.rest import rest_api

from .intent import Inter

@rest_api()
class Story(models.Model):
    intents = models.ManyToManyField(Intent)
