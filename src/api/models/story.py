from djongo import models
from . import Project, Intent

class Story(models.Model):
    name = models.TextField(default="")
    content = models.ListField(default=[])
    project = models.EmbeddedModelField(
        model_container=Project
    )

    objects = models.DjongoManager()
