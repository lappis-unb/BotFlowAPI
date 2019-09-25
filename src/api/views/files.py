from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser

from django.shortcuts import get_object_or_404
from django.http import JsonResponse, Http404, HttpResponse
from django.utils.encoding import smart_str

from api.models import Project, Story, Intent, Utter
from api.parser import StoryParser, IntentParser, DomainParser
from api.utils.handlers import handle_uploaded_file
from api.utils import get_zipped_files

import os
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

    def clean_str(string):
        string = string.replace(" ", "")
        string = string.replace("\n", "")        

        return string


    def markdown_parser(self, markdown_file):
        stories = []
        stories_file = markdown_file.split("## ")[1:]

        for story in stories_file:
            story = story.split("\n*")
            story_name = story[0]
            intents = story[1:]

            content = []
            for intent in intents:
                intent = intent.split("\n    -")
               
                intent_name = StoriesFile.clean_str(intent[0])
                utters = intent[1:]

                intent = Intent.objects.get(name=intent_name)
                content.append({"id": intent.id,
                                "type": "intent"})


                for utter in utters:
                    utter_name = StoriesFile.clean_str(utter)
                    utter = Utter.objects.get(name=utter_name)

                content.append({"id": utter.id,
                                "type": "utter"})

            stories.append({"name": story_name,
             "content": content})

        return stories


    """
    Receives a put request with a project id and a Markdown file with story specs as arguments. Then parse and add this file into DB 
    """
    def put(self, request, project_id, format=None):
        project = get_object_or_404(Project, pk=project_id)

        try:
            # Handle file from request
            file_obj = request.data['file']
            file_tmp = handle_uploaded_file(file_obj)
            file_content = file_tmp.read().decode('utf-8')
            
            stories_dicts = StoriesFile().markdown_parser(file_content)

            stories = []
            for story in stories_dicts:
                story.update({"project": project})
                print(story)
                stories.append(Story(**story))

            Story.objects.bulk_create(stories)

            file_tmp.close()

        except Exception as e:
            raise e
            return JsonResponse({'content': "File had problems during upload"})

        return JsonResponse({'content': "File has been successfully uploaded"})



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

    """
    Receives a put request with a project id and a Markdown file with intents specs as arguments. Then parse and add this file into DB 
    """
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



class UttersFile(APIView):
    """
    Receives a put request with a project id and a YML file with utter specs as arguments. Then parse and add this file into DB 
    """

    def put(self, request, project_id, format=None):
        project = get_object_or_404(Project, pk=project_id)

        try:
            # Handle file from request
            file_obj = request.data['file']
            file_tmp = handle_uploaded_file(file_obj)

            # Handle yaml
            yaml=YAML(typ="safe")
            domain = yaml.load(file_tmp)
            
            utters_list = domain['templates']
            utters = []
            for utter_name in utters_list.keys():
                alternatives = []

                for alternative in utters_list[utter_name]:
                    alternatives.append(alternative['text'].split("\n\n"))

                utter = {"name" : utter_name,
                         "alternatives" : [alternatives],
                         "multiple_alternatives": True if len(alternatives) > 1 else False,
                         "project" : project }

                utters.append(Utter(**utter))
            
            Utter.objects.bulk_create(utters)

            file_tmp.close()

        except Exception as e:
            raise e
            return JsonResponse({'content': "File had problems during upload"})

        return JsonResponse({'content': "File has been successfully uploaded"})

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
            'domain.yml': domain_markdown_str
        }

        file_name, file_path = get_zipped_files(project, coach_files)

        if os.path.exists(file_path):
            with open(file_path, 'rb') as f:
                response = HttpResponse(f.read(), content_type='application/zip')
                response['Content-Disposition'] = 'attachment; filename={0}'.format(smart_str(file_name))

                return response
        else:
            raise Http404