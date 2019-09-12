from rest_framework.views import APIView

from django.shortcuts import get_object_or_404
from django.http import JsonResponse, Http404

from api.models import Project, Story, Intent
from api.parser import StoryParser, IntentParser


class StoriesFile(APIView):
    """
    Receives a get request with a project id and returns
    a json response with the markdown string, containing
    all stories of the project, in the body.
    """

    def get(self, request, project_id):
        project = get_object_or_404(Project, pk=project_id)
        stories = Story.objects.filter(project=project)
        
        if not stories:
            raise Http404
        
        parser = StoryParser()
        markdown_str = ''

        for story in stories:
            markdown_str += parser.parse(story)
        
        return JsonResponse({'content': markdown_str})  


class IntentsFile(APIView):
    """
    Receives a get request with a project id and returns
    a json response with the markdown string, containing
    all intents of the project, in the body.
    """

    def get(self, request, project_id):
        project = get_object_or_404(Project, pk=project_id)
        intents = Intent.objects.filter(project=project)

        if not intents:
            raise Http404

        parser = IntentParser()
        markdown_str = ''

        for intent in intents:
            markdown_str += parser.parse(intent)

        return JsonResponse({'content': markdown_str})

