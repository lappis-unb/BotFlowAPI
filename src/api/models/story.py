from djongo import models
from . import Project, Intent, Utter
from rest_framework import serializers
import random


class Story(models.Model):
    name = models.TextField(default="")
    content = models.ListField(default=[])
    project = models.EmbeddedModelField(
        model_container=Project
    )
    is_checkpoint = models.BooleanField(default=False)

    objects = models.DjongoManager()

class StorySerializer(serializers.ModelSerializer):
    content = serializers.SerializerMethodField()

    def get_example(self, obj):

        for i, element in enumerate(obj.content):

            if element['type'] == 'utter':
                element_obj = Utter.objects.filter(pk=element['id']).first()
                obj.content[i]['example'] = random.choice(getattr(element_obj, 'alternatives'))
                obj.content[i]['name'] = getattr(element_obj, 'name')
            elif element['type'] == 'intent':
                element_obj = Intent.objects.filter(pk=element['id']).first()
                obj.content[i]['example'] = random.choice(getattr(element_obj, 'samples'))
                obj.content[i]['name'] = getattr(element_obj, 'name')
            elif element['type'] == 'checkpoint':
                element_obj = Story.objects.filter(pk=element['id']).first()
                obj.content[i]['name'] = getattr(element_obj, 'name')



    def get_content(self, obj):
        self.get_example(obj)
        return [dict(content) for content in obj.content]

    class Meta:
        model = Story
        fields = ['id', 'name', 'content', 'is_checkpoint']

class StoryListSerializer(serializers.ModelSerializer):
    content = serializers.SerializerMethodField()

    def get_content(self, obj):
        StorySerializer.get_example(self, obj)

        return [{
            'name': content['name'],
            'type': content['type']
        } for content in obj.content]

    class Meta:
        model = Story
        fields = ['id', 'name', 'content']


class CheckpointSerializer(serializers.ModelSerializer):
    content = serializers.SerializerMethodField()

    def get_content(self, obj):
        StorySerializer.get_example(self, obj)

        return [{
            'id': content['id'],
            'name': content['name'],
            'example': content['example'],
            'type': content['type']
        } for content in obj.content]

    class Meta:
        model = Story
        fields = ['id', 'name', 'content']


class CheckpointListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Story
        fields = ['id', 'name']
