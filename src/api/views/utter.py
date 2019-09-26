from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from api.models import Utter, UtterSerializer, Project, UtterListSerializer, UtterExampleSerializer
from api.utils import request_to_dict, validate_utter, delete_related_stories
from api.webhook import intents_delete_hook, stories_delete_hook, domain_delete_hook


class ListUtters(APIView):

    def get(self, request, project_id=None, utter_id=None, format=None):
        if not project_id:
            return Response(status=404)

        if utter_id:
            utter = get_object_or_404(Utter, pk=utter_id)

            return Response(UtterSerializer(utter).data)
        
        project = get_object_or_404(Project, pk=project_id)

        utters = UtterListSerializer(
            Utter.objects.filter(project=project), 
            many=True
        ).data

        utters = sorted(utters, key=lambda x: x['name'])

        return Response(utters)

    def post(self, request, project_id=None, utter_id=None, format=None):
        if not project_id:
            return Response(status=404)
        
        data = request_to_dict(request)
        
        is_valid, error_messages = validate_utter(data, project_id)

        if not is_valid:
            return Response({'errors': error_messages}, status=400)


        project = get_object_or_404(Project, pk=project_id)

        utter = Utter.objects.create(
            name=data['name'],
            alternatives=data['alternatives'],
            multiple_alternatives=data['multiple_alternatives'],
            project=project
        )

        return Response(UtterSerializer(utter).data, status=201)

    def delete(self, request, project_id=None, utter_id=None, format=None):
        utter = get_object_or_404(Utter, pk=utter_id)
        delete_related_stories(utter, 'utter')
        utter.delete()
        intents_delete_hook(project_id)
        stories_delete_hook(project_id)
        domain_delete_hook(project_id)

        return Response(status=204)        

    def put(self, request, project_id=None, utter_id=None, format=None):
        utter = get_object_or_404(Utter, pk=utter_id)
        project = Project.objects.get(pk=project_id)
        data = request_to_dict(request)

        is_valid, error_messages = validate_utter(data, project_id)

        if not is_valid:
            return Response({'errors': error_messages}, status=400)

        for attr in data:
            setattr(utter, attr, data[attr])
        
        utter.project = project
        utter.save()

        return Response(UtterSerializer(utter).data)

class ListUtterExample(APIView):

    def get(self, request, project_id=None, utter_id=None, format=None):
        if not project_id:
            return Response(status=404)

        if utter_id:
            utter = get_object_or_404(Utter, pk=utter_id)
            return Response(UtterExampleSerializer(utter).data)
