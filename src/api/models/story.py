from djongo import models
from boogie.rest import rest_api
from .project import Project

class Story(models.Model):
    content = models.DictField(default={'list':[]})
    project = models.EmbeddedModelField(
        model_container=Project
    )

    objects = models.DjongoManager()
