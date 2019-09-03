from djongo import models
from rest_framework import serializers


class Project(models.Model):
    name = models.TextField()
    description = models.TextField()

    objects = models.DjongoManager()


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'description']
