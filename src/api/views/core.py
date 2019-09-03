from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from api.models import Project
import json

def request_to_dict(request):
    str_args = request.body.decode('utf-8')
    json_data = json.loads(str_args)
    return json_data

class ListProjects(APIView):

    def get(self, request, project_id=None, format=None):
        if project_id:
            project = get_object_or_404(Project, pk=project_id)
            return Response({'name': project.name, 'description': project.description})

        return Response({'projects': None})

    def post(self, request, project_id=None, format=None):
        data = request_to_dict(request)
        
        Project.objects.create(name=data['name'], description=data['description'])

        return Response(status=201)

    def delete(self, request, project_id=None, format=None):
        project = get_object_or_404(Project, pk=project_id)
        project.delete()

        return Response(status=204)        

    def put(self, request, project_id=None, format=None):
        project = get_object_or_404(Project, pk=project_id)
        data = request_to_dict(request)

        for attr in data:
            setattr(project, attr, data[attr])

        return Response({'name': project.name, 'description': project.description})