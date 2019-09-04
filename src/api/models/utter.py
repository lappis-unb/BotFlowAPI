from djongo import models
from rest_framework import serializers
from .project import Project

class Utter(models.Model):
    name = models.TextField()
    multiple_alternatives = models.BooleanField(default=False)
    alternatives = models.ListField(default=[])
    project = models.EmbeddedModelField(
        model_container=Project
    )

    objects = models.DjongoManager()

class UtterSerializer(serializers.ModelSerializer):
    alternatives = serializers.ListField()
    class Meta:
        model = Utter
        fields = ['id', 'name', 'multiple_alternatives', 'alternatives']
