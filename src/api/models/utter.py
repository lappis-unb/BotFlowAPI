from djongo import models
from rest_framework import serializers
from .project import Project
import random

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

class UtterListSerializer(serializers.ModelSerializer):
    def to_representation(self, obj):
        ret = super().to_representation(obj)
        ret['type'] = 'utter'
        return ret
    
    class Meta:
        model = Utter
        fields = ['id', 'name']

class UtterExampleSerializer(serializers.ModelSerializer):
    example = serializers.SerializerMethodField()

    def to_representation(self, obj):
        ret = super().to_representation(obj)
        ret['type'] = 'utter'
        return ret

    def get_example(self, obj):
        return random.choice(obj.alternatives)

    class Meta:
        model = Utter
        fields = ['id', 'name', 'example']
