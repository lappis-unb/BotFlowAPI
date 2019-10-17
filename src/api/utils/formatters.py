import json
from api.models import Utter, Intent, Story
from django.shortcuts import get_object_or_404


def request_to_dict(request):
    str_args = request.body.decode('utf-8')
    json_data = json.loads(str_args)
    return json_data

def story_content_formatter(content):
    new_content = []
    for element in content:
        if element['type'] == 'intent':
            intent = get_object_or_404(Intent, pk=element['id'])
            element['name'] = intent.name
            new_content.append(element)
        elif element['type'] == 'utter':
            utter = get_object_or_404(Utter, pk=element['id'])
            element['name'] = utter.name
            new_content.append(element)
        elif element['type'] == 'checkpoint':
            checkpoint = get_object_or_404(Story, pk=element['id'])
            element['name'] = checkpoint.name
            new_content.append(element)
    return new_content
