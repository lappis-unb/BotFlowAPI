import json
import os
import random

from api.models import Intent, Utter, Project, Story
from api.utils import story_content_formatter, validate_content

json_path = './api/fixtures/initial.json'

models_dict = {}
models_dict['api.project'] = []
models_dict['api.utter'] = []
models_dict['api.intent'] = []
models_dict['api.story'] = []

if Project.objects.count() < 1:
    print("No default project found. Seeding database...")
    with open(json_path) as json_file:
        data = json.load(json_file)
        for each in data:
            models_dict[each['model']].append(each)

    for each in models_dict['api.project']:
        Project.objects.create(
            name=each['fields']['name'],
            description=each['fields']['description']
        )

    for each in models_dict['api.intent']:
        Intent.objects.create(
            name=each['fields']['name'],
            samples=each['fields']['samples'],
            project=Project.objects.all().first()
        )

    for each in models_dict['api.utter']:
        Utter.objects.create(
            name=each['fields']['name'],
            multiple_alternatives=each['fields']['multiple_alternatives'],
            alternatives=each['fields']['alternatives'],
            project=Project.objects.all().first()
        )

    cls_dict = {}
    cls_dict['intent'] = Intent
    cls_dict['utter'] = Utter
    cls_dict['checkpoint'] = Story

    for each in models_dict['api.story']:
        contents = []

        for content in each['fields']['content']:
            obj = cls_dict[content['type']].objects.filter(name=content['name']).first()

            if not obj:
                print("=========== MISSING DATA TO CREATE STORY ===========")
                print(content, "WAS NOT DECLARED BEFORE")
                print("====================================================")
                continue

            new_obj = {
                'type': content['type'],
                'id': obj.id
            }

            if content['type'] == "checkpoint":
                for i, element in enumerate(obj.content):
                    if element['type'] == 'utter':
                        element_obj = Utter.objects.filter(pk=element['id']).first()
                        obj.content[i]['example'] = random.choice(getattr(element_obj, 'alternatives'))
                    elif element['type'] == 'intent':
                        element_obj = Intent.objects.filter(pk=element['id']).first()
                        obj.content[i]['example'] = random.choice(getattr(element_obj, 'samples'))

                new_obj['content'] = obj.content

            contents.append(new_obj)


        if validate_content(contents):
            story = Story.objects.create(
                name="Default Name",
                content=story_content_formatter(contents),
                is_checkpoint= True if 'is_checkpoint' in each else False,
                project=Project.objects.all().first()
            )
            story.name = "Diálogo_{0}_{1}".format(story.project.name, story.id)
            story.save()
else:
    print("Database already contains objects. Skipping database seeding...")
