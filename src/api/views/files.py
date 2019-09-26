from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser

from django.shortcuts import get_object_or_404
from django.http import JsonResponse, Http404, HttpResponse
from django.utils.encoding import smart_str

from api.models import Project, Story, Intent, Utter
from api.parser import StoryParser, IntentParser, DomainParser
from api.utils.handlers import handle_uploaded_file
from api.utils import get_zipped_files
from api.decoder import decode_story_file

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

    """
    Receives a put request with a project id and a Markdown file with story specs as arguments. Then parse and add this file into DB 
    """
    def put(self, request, project_id, format=None):
        project = get_object_or_404(Project, pk=project_id)

        try:
            # Handle file from request
            file_obj = request.data['file']
            
            with handle_uploaded_file(file_obj) as file_tmp:
                file_content = file_tmp.read().decode('utf-8')

                stories_dicts = decode_story_file(file_content)
                
                stories = []
                for story in stories_dicts:
                    content = []
                    for intent in story['intents']:
                        content.append(
                            {
                                "id": Intent.objects.get(name=intent['intent']).id,
                                "type": "intent" 
                            }
                        )
                        for utter in intent['utters']:
                            content.append(
                                {
                                    "id": Utter.objects.get(name=utter).id,
                                    "type": "utter" 
                                }
                            )

                    print(content)
                    stories.append(
                        {
                            "name": story['story'],
                            "content": content,
                            "project": project
                        }
                    )


            # Story.objects.bulk_create(stories)


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

        file_obj = request.data['file']
        with handle_uploaded_file(file_obj) as file_tmp:
            # Handle file from request
            file_content = file_tmp.read().decode('utf-8')

            # Parser markdown to html 
            md = markdown.Markdown()
            html = md.convert(file_content)
            html = BeautifulSoup(html, features="html.parser")
            names = html.findAll('h2')
            list_samples = html.findAll('ul')

            # Extract data
            intents = []
            for name, samples in zip(names, list_samples):
                if name.string is not None and "intent" in name.string:                    
                    name = name.string.split("intent:")[-1]
                    intents.append(Intent(
                        name=name,
                        samples=[
                            li.string or html2markdown.convert(innerHTML(li)).replace('# ', '#') 
                            for li in samples.findAll('li')],
                        project=project,
                    ))

        bulk_update_unique(intents, 'name')
        return JsonResponse({'content': "File has been successfully uploaded"})


def bulk_update_unique(items, attr='name'):
    """
    Save a list of elements that have a new value for the given attribute.
    """
    if not items:
        return []

    objects = type(items[0]).objects
    query = {attr + '__in': [x.name for x in items]}
    repeated = objects.filter(**query).values_list(attr, flat=True)
    
    # Check the database
    if repeated:
        print(f'Repeated values for {attr}:', ', '.join(repeated))
        repeated = set(repeated)
        items = [x for x in items if getattr(x, attr) not in repeated]
    
    # Check internal consistency
    values = set()
    items_final = []
    for item in items:
        value = getattr(item, attr)
        if value in values:
            print(f'Duplicated entry:', value)
        else:
            items_final.append(item)
    
    return objects.bulk_create(items)


def innerHTML(element):
    return element.decode_contents(formatter="html")

class UttersFile(APIView):
    """
    Receives a put request with a project id and a YML file with utter specs as arguments. Then parse and add this file into DB 
    """

    def put(self, request, project_id, format=None):
        project = get_object_or_404(Project, pk=project_id)

        # Handle file from request
        file_obj = request.data['file']
        file_tmp = handle_uploaded_file(file_obj)

        with handle_uploaded_file(file_obj) as file_tmp:
            # Handle yaml
            yaml=YAML(typ="safe")
            domain = yaml.load(file_tmp)
            
            utters_list = domain['templates']
            utters = []
            
            for utter_name in utters_list.keys():
                alternatives = [x['text'].split("\n\n") for x in utters_list[utter_name]]

                utters.append(Utter(
                    name= utter_name,
                    alternatives=[alternatives],
                    multiple_alternatives=True if len(alternatives) > 1 else False,
                    project=project
                ))
                

        bulk_update_unique(utters, 'name')
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

