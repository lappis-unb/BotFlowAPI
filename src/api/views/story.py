from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from api.models import Story, StorySerializer, Project
from api.utils import request_to_dict, validate_content, story_content_formatter

class ListStories(APIView):

    def get(self, request, project_id=None, story_id=None, format=None):
        if not project_id:
            return Response(status=404)

        if story_id:
            story = get_object_or_404(Story, pk=story_id)

            return Response(StorySerializer(story).data)
        
        project = get_object_or_404(Project, pk=project_id)

        stories = StorySerializer(
            Story.objects.filter(project=project), 
            many=True
        ).data

        return Response(stories)

    def post(self, request, project_id=None, story_id=None, format=None):
        if not project_id:
            return Response(status=404)
        
        data = request_to_dict(request)
        
        project = get_object_or_404(Project, pk=project_id)

        if validate_content(data['content']):
            story = Story.objects.create(
                name=data['name'],
                content=story_content_formatter(data['content']),
                project=project
            )

            return Response(StorySerializer(story).data, status=201)
        else:
            return Response({'error': 'Invalid content array'}, status=400)

    def delete(self, request, project_id=None, story_id=None, format=None):
        story = get_object_or_404(Story, pk=story_id)
        story.delete()

        return Response(status=204)        

    def put(self, request, project_id=None, story_id=None, format=None):
        story = get_object_or_404(Story, pk=story_id)
        data = request_to_dict(request)

        if validate_content(data['content']):
            for attr in data:
                if attr == 'content':
                    setattr(story, attr, story_content_formatter(data[attr]))
                else:
                    setattr(story, attr, data[attr])

            story.save()

            return Response(StorySerializer(story).data)
        else:
            return Response({'error': 'Invalid content array'}, status=400)