from djongo import models
from .project import Project

class Intent(models.Model):
    name = models.TextField()
    samples = models.DictField(default={'list':[]})
    project = models.EmbeddedModelField(
        model_container=Project
    )

    objects = models.DjongoManager()
