from rest_framework.views import APIView

from django.shortcuts import get_object_or_404
from django.http import JsonResponse, Http404, HttpResponse
from django.utils.encoding import smart_str

from api.models import Project, Story, Intent
from api.parser import StoryParser, IntentParser, DomainParser
from api.utils import get_zipped_files

import os


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


class DomainFile(APIView):
    """
    Receives a get request with a project id and returns
    a json response with markdown string, containing all
    domain content, in the body.
    """

    def get(self, request, project_id):
        project = get_object_or_404(Project, pk=project_id)
        parser = DomainParser()
        markdown_str = parser.parse(project)

        return JsonResponse({'content': markdown_str})

class ZipFile(APIView):
    def get(self, request, project_id):
        project = get_object_or_404(Project, pk=project_id)
        intents = Intent.objects.filter(project=project)
        stories = Story.objects.filter(project=project)

        # Intent parsing
        if not intents:
            raise Http404

        intent_parser = IntentParser()
        intent_markdown_str = ''

        for intent in intents:
            intent_markdown_str += intent_parser.parse(intent)

        # Story parsing
        if not stories:
            raise Http404
        
        stories_parser = StoryParser()
        stories_markdown_str = ''

        for story in stories:
            stories_markdown_str += stories_parser.parse(story)

        # Domain parsing
        domain_parser = DomainParser()
        domain_markdown_str = domain_parser.parse(project)

        coach_files = {
            'intents.md': intent_markdown_str, 
            'stories.md': stories_markdown_str, 
            'domain.md': domain_markdown_str
        }

        file_name, file_path = get_zipped_files(project, coach_files)

        if os.path.exists(file_path):
            with open(file_path, 'rb') as f:
                response = HttpResponse(f.read(), content_type='application/zip')
                response['Content-Disposition'] = 'attachment; filename={0}'.format(smart_str(file_name))

                return response
        else:
            raise Http404