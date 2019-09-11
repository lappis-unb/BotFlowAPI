from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from api.models import Utter, UtterSerializer, Project
from api.utils import request_to_dict, validate_utter

class ListUtters(APIView):

    def get(self, request, project_id=None, utter_id=None, format=None):
        if not project_id:
            return Response(status=404)

        if utter_id:
            utter = get_object_or_404(Utter, pk=utter_id)

            return Response(UtterSerializer(utter).data)
        
        project = get_object_or_404(Project, pk=project_id)

        utters = UtterSerializer(
            Utter.objects.filter(project=project), 
            many=True
        ).data

        utters = sorted(utters, key=lambda x: x['name'])

        return Response(utters)

    def post(self, request, project_id=None, utter_id=None, format=None):
        if not project_id:
            return Response(status=404)
        
        data = request_to_dict(request)
        
        if not validate_utter(data):
            return Response({'error': 'Missing fields'}, status=400)


        project = get_object_or_404(Project, pk=project_id)

        utter = Utter.objects.create(
            name=data['name'],
            alternatives=data['alternatives'],
            project=project
        )

        return Response(UtterSerializer(utter).data, status=201)

    def delete(self, request, project_id=None, utter_id=None, format=None):
        utter = get_object_or_404(Utter, pk=utter_id)
        utter.delete()

        return Response(status=204)        

    def put(self, request, project_id=None, utter_id=None, format=None):
        utter = get_object_or_404(Utter, pk=utter_id)
        data = request_to_dict(request)

        if not validate_utter(data):
            return Response({'error': 'Missing fields'}, status=400)

        for attr in data:
            setattr(utter, attr, data[attr])

        utter.save()

        return Response(UtterSerializer(utter).data)