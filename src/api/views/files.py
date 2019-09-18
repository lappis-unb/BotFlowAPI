from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser

from django.shortcuts import get_object_or_404
from django.http import JsonResponse, Http404

from api.models import Project, Story, Intent
from api.parser import StoryParser, IntentParser
from api.utils.handlers import handle_uploaded_file

import markdown
import html2markdown
from ruamel.yaml import YAML
from bs4 import BeautifulSoup

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


    def put(self, request, project_id, format=None):
        project = get_object_or_404(Project, pk=project_id)

        try:
            # Handle file from request
            file_obj = request.data['file']
            file_tmp = handle_uploaded_file(file_obj)
            file_content = file_tmp.read().decode('utf-8')

            # Parser markdown to html 
            md = markdown.Markdown()
            html = md.convert(file_content)
            print("MD", md)
            md.reset()
            html = BeautifulSoup(html, features="html.parser")
            intent_names = html.findAll('h2')
            intent_list_samples = html.findAll('ul')

            # Extract data
            intents = []
            for intent_name, intent_samples in zip(intent_names, intent_list_samples):
                if intent_name.string is not None:
                    if "intent" in intent_name.string:                    
                        intent_name = intent_name.string.split("intent:")[-1]
                        s = BeautifulSoup(str(intent_samples), features="html.parser").findAll('li')
                        
                        samples = []
                        for sample in s:
                            sample_string = ""
                            if sample.string is None:
                                s = str(sample)
                                s = s.replace("<li>", "")
                                s = s.replace("</li>", "")
                                sample_string = html2markdown.convert(s)
                            else:
                                sample_string = sample.string

                            samples.append(sample_string)

                        intent = {"name" : intent_name,
                                "samples" : samples,
                                "project" : project }
                        intents.append(Intent(**intent))
            
            Intent.objects.bulk_create(intents)
            file_tmp.close()

        except Exception as e:
            raise e
            return JsonResponse({'content': "File had problems during upload"})

        return JsonResponse({'content': "File has been successfully uploaded"})