from djongo import models
from rest_framework import serializers
from .project import Project

class Utter(models.Model):
    name = models.TextField()
    alternatives = models.ListField(default=[])
    project = models.EmbeddedModelField(
        model_container=Project
    )

    objects = models.DjongoManager()

class UtterSerializer(serializers.ModelSerializer):
    alternatives = serializers.ListField(
        child=serializers.ListField()
    )
    class Meta:
        model = Utter
        fields = ['id', 'name', 'alternatives']
