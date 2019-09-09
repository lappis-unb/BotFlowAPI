from djongo import models
from boogie.rest import rest_api
from .project import Project

class Story(models.Model):
    name = models.TextField(default="")
    content = models.ListField(default=[])
    project = models.EmbeddedModelField(
        model_container=Project
    )

    objects = models.DjongoManager()
