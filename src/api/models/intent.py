from djongo import models
from .project import Project
from rest_framework import serializers

class Intent(models.Model):
    name = models.TextField()
    samples = models.ListField(default=[])
    project = models.EmbeddedModelField(
        model_container=Project
    )

    objects = models.DjongoManager()

class IntentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intent
        fields = ['id', 'name', 'samples']
