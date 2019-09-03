from djongo import models
from boogie.rest import rest_api
from .utter import Utter
from .story import Story
from .intent import Intent

class Project(models.Model):
    name = models.TextField()
    description = models.TextField()

    objects = models.DjongoManager()

    class Meta:
        model = Blog
        fields = (
            'name'
        )
