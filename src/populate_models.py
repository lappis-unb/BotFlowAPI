import json
import os

from api.models import Intent, Utter, Project

json_path = './api/fixtures/initial.json'

models_dict = {}
models_dict['api.project'] = []
models_dict['api.utter'] = []
models_dict['api.intent'] = []

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
else:
    print("Database already contains objects. Skipping database seeding...")