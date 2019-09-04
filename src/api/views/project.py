from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from api.models import Project
from api.models.project import ProjectSerializer
from api.utils import request_to_dict

class ListProjects(APIView):

    def get(self, request, project_id=None, format=None):
        if project_id:
            project = get_object_or_404(Project, pk=project_id)
            return Response(ProjectSerializer(project).data)
        
        projects = ProjectSerializer(Project.objects.all(), many=True).data
        return Response({'projects': projects})

    def post(self, request, project_id=None, format=None):
        data = request_to_dict(request)
        
        project = Project.objects.create(
            name=data['name'], 
            description=data['description']
        )

        return Response(ProjectSerializer(project).data, status=201)

    def delete(self, request, project_id=None, format=None):
        project = get_object_or_404(Project, pk=project_id)
        project.delete()

        return Response(status=204)        

    def put(self, request, project_id=None, format=None):
        project = get_object_or_404(Project, pk=project_id)
        data = request_to_dict(request)

        for attr in data:
            setattr(project, attr, data[attr])

        project.save()

        return Response(ProjectSerializer(project).data)
