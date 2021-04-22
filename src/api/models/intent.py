from djongo import models
from .project import Project
from rest_framework import serializers
import random

class Intent(models.Model):
    name = models.TextField()
    samples = models.ListField(default=[])
    project = models.EmbeddedModelField(
        model_container=Project
    )

    objects = models.DjongoManager()

class IntentSerializer(serializers.ModelSerializer):
    samples = serializers.ListField()
    class Meta:
        model = Intent
        fields = ['id', 'name', 'samples']

class IntentListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Intent
        fields = ['id', 'name']

class IntentExampleSerializer(serializers.ModelSerializer):
    example = serializers.SerializerMethodField()

    def to_representation(self, obj):
        ret = super().to_representation(obj)
        ret['type'] = 'intent'
        return ret

    def get_example(self, obj):
        return random.choice(obj.samples)

    class Meta:
        model = Intent
        fields = ['id', 'name', 'example']
