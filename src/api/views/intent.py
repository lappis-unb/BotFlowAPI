from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from api.models import Intent, IntentSerializer, Project
from api.utils import request_to_dict

class ListIntents(APIView):

    def get(self, request, project_id=None, intent_id=None, format=None):
        if not project_id:
            return Response(status=404)

        if intent_id:
            intent = get_object_or_404(Intent, pk=intent_id)
            return Response(IntentSerializer(intent).data)
        
        project = get_object_or_404(Project, pk=project_id)

        intents = IntentSerializer(
            Intent.objects.filter(project=project), 
            many=True
        ).data

        return Response({'intents': intents})

    def post(self, request, project_id=None, intent_id=None, format=None):
        if not project_id:
            return Response(status=404)
        
        data = request_to_dict(request)
        
        project = get_object_or_404(Project, pk=project_id)

        intent = Intent.objects.create(
            name=data['name'],
            samples=data['samples'],
            project=project
        )

        return Response(IntentSerializer(intent).data, status=201)

    def delete(self, request, project_id=None, intent_id=None, format=None):
        intent = get_object_or_404(Intent, pk=intent_id)
        intent.delete()

        return Response(status=204)        

    def put(self, request, project_id=None, intent_id=None, format=None):
        intent = get_object_or_404(Intent, pk=intent_id)
        data = request_to_dict(request)

        for attr in data:
            setattr(intent, attr, data[attr])

        intent.save()

        return Response(IntentSerializer(intent).data)