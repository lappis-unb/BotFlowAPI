from django.test import TestCase
from django.urls import reverse, resolve
from rest_framework import status
from rest_framework.test import APIRequestFactory
from rest_framework.test import APIClient
from api.models import project, story, intent
from .views import story

class StoriesFileTest(TestCase):
    def setUp(self):
        self.story = Story.objects.create(id = '10', name = 'teste', content = [
            {
                "name": "content name",
                "type": "intent"
            },
            {
                "name": "content name 2",
                "type": "utter"
            },
            {
                "name": "content name 3",
                "type": "utter"
            }
        ])
        self.factory = APIRequestFactory()
        self.view = StoriesFile.as_view()
        self.client = APIClient()
        self.data = {'id':'10', 'name':'teste', 'content': [
            {
                "name": "content name",
                "type": "intent"
            },
            {
                "name": "content name",
                "type": "utter"
            },
            {
                "name": "content name",
                "type": "utter"
            }
        ]}

    def test_story_view_success_status_code(self):
        url = reverse('api:story', kwargs={'pk': self.story.pk})
        request = self.factory.get(url)
        response = self.view(request, pk=self.story.pk)
        self.assertEquals(response.status_code, 200)