from django.db import models
from boogie.rest import rest_api

import jsonfield

@rest_api()
class Intent(models.Model):
    name = models.TextField()
    examples = jsonfield.JSONField()
