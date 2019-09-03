from djongo import models
from boogie.rest import rest_api
from .utter import Utter
from .story import Story
from .intent import Intent

class Project(models.Model):
    name = models.TextField()
    description = models.TextField()
    utters = models.ArrayReferenceField(to=Utter, on_delete=models.CASCADE, default=None)
    intents = models.ArrayReferenceField(to=Intent, on_delete=models.CASCADE, default=None)
    stories = models.ArrayReferenceField(to=Story, on_delete=models.CASCADE, default=None)
    # entities = models.ArrayReferenceField(to=Entity, on_delete=models.CASCADE)

    objects = models.DjongoManager()
