from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from api.models import Intent, IntentSerializer, Project, IntentListSerializer, IntentExampleSerializer
from api.utils import request_to_dict, validate_intent
from api.webhook import stories_delete_hook, intents_delete_hook


class ListIntents(APIView):

    def get(self, request, project_id=None, intent_id=None, format=None):
        if not project_id:
            return Response(status=404)

        if intent_id:
            intent = get_object_or_404(Intent, pk=intent_id)
            return Response(IntentSerializer(intent).data)
        
        project = get_object_or_404(Project, pk=project_id)

        intents = IntentListSerializer(
            Intent.objects.filter(project=project), 
            many=True
        ).data

        intents = sorted(intents, key=lambda x: x['name'])

        return Response(intents)

    def post(self, request, project_id=None, intent_id=None, format=None):
        if not project_id:
            return Response(status=404)
        
        data = request_to_dict(request)
        
        is_valid, error_messages = validate_intent(data, project_id)

        if not is_valid:
            return Response({'errors': error_messages}, status=400)

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

        stories_delete_hook(project_id)
        intents_delete_hook(project_id)

        return Response(status=204) 

    def put(self, request, project_id=None, intent_id=None, format=None):
        intent = get_object_or_404(Intent, pk=intent_id)
        project = get_object_or_404(Project, pk=project_id)
        data = request_to_dict(request)

        is_valid, error_messages = validate_intent(data, project_id)

        if not is_valid:
            return Response({'errors': error_messages}, status=400)
 
        for attr in data:
            setattr(intent, attr, data[attr])

        intent.project = project
        intent.save()

        return Response(IntentSerializer(intent).data)

class ListIntentExample(APIView):

    def get(self, request, project_id=None, intent_id=None, format=None):
        if not project_id:
            return Response(status=404)

        if intent_id:
            intent = get_object_or_404(Intent, pk=intent_id)
            return Response(IntentExampleSerializer(intent).data)
