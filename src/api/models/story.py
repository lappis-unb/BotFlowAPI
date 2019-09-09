from djongo import models
from . import Project, Intent

class Story(models.Model):
    name = models.TextField()
    intents = models.ArrayModelField(
        model_container=Intent
    )
    project = models.EmbeddedModelField(
        model_container=Project
    )

    objects = models.DjongoManager()
