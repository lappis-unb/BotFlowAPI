from djongo import models
from . import Project, Intent
from rest_framework import serializers


class Story(models.Model):
    name = models.TextField(default="")
    content = models.ListField(default=[])
    project = models.EmbeddedModelField(
        model_container=Project
    )

    objects = models.DjongoManager()

class StorySerializer(serializers.ModelSerializer):
    formatted_content = serializers.SerializerMethodField()

    def get_formatted_content(self, obj):
        return [dict(content) for content in obj.content]

    class Meta:
        model = Story
        fields = ['id', 'name', 'formatted_content']
