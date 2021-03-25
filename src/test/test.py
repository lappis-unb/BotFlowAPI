from django.test import TestCase
from django.urls import reverse, resolve
from rest_framework import status
from rest_framework.test import APIRequestFactory
from rest_framework.test import APIClient
from api.models import Project, Story, Intent, Utter, StorySerializer, UtterSerializer, ProjectSerializer, IntentSerializer
from api.views import ListUtters, ListProjects, ListIntents

class StoriesTests(TestCase):
    
    def test_model_story(self):
        testStory = Story.objects.create(
            name = "Default Name",
            content = story_content_formatter('content test', 'utter'),
            project = 1
        )
        testStory.name = "Diálogo_Teste_{0}".format(story.id)
        testStory.save()

    def test_model_story_get(self):
        getTestStory = Story.objects.get(pk = self.testStory.pk)
        serializer = StorySerializer(getTestStory)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
class UtterTests(TestCase):
    def test_model_utter(self):
        testUtter = Utter.objects.create(
            name = 'Utter test name',
            alternatives = 'alternatives',
            multiple_alternatives = 'multiple_alternatives',
            project = 1
        )
        testUtter.save()

    def test_model_utter_get(self):
        getTestUtter = Utter.objects.get(pk = self.testUtter.pk)
        serializer = UtterSerializer(getTestUtter)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class ProjectTests(TestCase):
    def test_model_project(self):
        testProject = Project.objects.create(
            name = 'Project Test Name', 
            description = 'description'
        )
        testProject.save()

    def test_model_project_get(self):
        getTestProject = Project.objects.get(pk = self.testProject.pk)
        serializer = ProjectSerializer(getTestProject)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class IntentTests(TestCase):
    def test_model_intent(self):
        testIntent = Intent.objects.create(
            name = 'Intent Test Name',
            samples = 'samples',
            project=1
        )
        testIntent.save()

    def test_model_intent_get(self):
        getTestIntent = Intent.objects.get(pk = self.testIntent.pk)
        serializer = IntentSerializer(getTestIntent)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)