from djongo import models
from .project import Project
from .intent import Intent
from .utter import Utter
from rest_framework import serializers
import random

class Story(models.Model):
    name = models.TextField(default="")
    content = models.ListField(default=[])
    project = models.EmbeddedModelField(
        model_container=Project
    )

    objects = models.DjongoManager()

class StorySerializer(serializers.ModelSerializer):
    content = serializers.SerializerMethodField()

    def get_example(self, obj):
        intent_ids = [element['id'] for element in obj.content if element['type'] == 'intent']
        intents = Intent.objects.filter(pk__in=intent_ids)

        utter_ids = [element['id'] for element in obj.content if element['type'] == 'utter']
        utters = Utter.objects.filter(pk__in=utter_ids)

        elements = {}
        elements['intent'] = intents
        elements['utter'] = utters

        field = {}
        field['intent'] = 'samples'
        field['utter'] = 'alternatives'

        for i, element in enumerate(obj.content):
            element_obj = elements[element['type']].filter(pk=element['id']).first()
            obj.content[i]['example'] = random.choice(getattr(element_obj, field[element['type']]))

    def get_content(self, obj):
        self.get_example(obj)
        return [dict(content) for content in obj.content]

    class Meta:
        model = Story
        fields = ['id', 'name', 'content']

class StoryListSerializer(serializers.ModelSerializer):
    content = serializers.SerializerMethodField()

    def get_content(self, obj):
        return [{
            'name': content['name'],
            'type': content['type']
        } for content in obj.content]

    class Meta:
        model = Story
        fields = ['id', 'name', 'content']