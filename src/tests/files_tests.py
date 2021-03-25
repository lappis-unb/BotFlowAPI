from django.test import TestCase
from django.urls import reverse, resolve
from rest_framework import status
from rest_framework.test import APIRequestFactory
from rest_framework.test import APIClient
from api.models import projectModel, storyModel, intentModel, utterModel
from api.views import utterView, projectView, intentView

class StoriesTest(TestCase):
    
    def testModelStory(self):
        storyModel.objects.create(
            id = 50, name = 'Teste', content = [
                {name: 'TesteContent',
                 type: 'utter'}]
        )

    def testModelStoryGet(self):
        idStory = storyModel.objects.get(id = 50)
        self.assertEqual(storyModel.object.get_content, 50)

class UtterTest(TestCase):
    def testModelUtter(self):
        utterModel.objects.create(
            id = 49, name = 'Teste'
        )

    def testModelUtterGet(self):
        idUtter = utterModel.objects.get(id = 49)
        self.assertEqual(utter.object.utterView.get, 49)

class ProjectTest(TestCase):
    def testModelProject(self):
        projectModel.objects.create(
            id = 3, name = 'Teste', description = "This is a Rasa bot!"
        )

    def testModelProjectGet(self):
        idProject= projectModel.objects.get(id = 3)
        self.assertEqual(utter.object.projectView.get, 3)

class IntentTest(TestCase):
    def testModelIntent(self):
        intentModel.objects.create(
            id = 52, name = 'Teste'
        )

    def testModelIntentGet(self):
        idIntent = intentModel.objects.get(id = 3)
        self.assertEqual(utter.object.intentView.get, 3)

