from djongo import models
from rest_framework import serializers
from .project import Project

class Utter(models.Model):
    name = models.TextField()
    alternatives = models.ListField(default=[])
    multiple_alternatives = models.BooleanField(blank=False, default=False)
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
        fields = ['id', 'name', 'multiple_alternatives', 'alternatives']
