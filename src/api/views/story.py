from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from api.models import Story, StorySerializer, Project, StoryListSerializer
from api.utils import request_to_dict, validate_content, story_content_formatter, validate_story

class ListStories(APIView):

    def get(self, request, project_id=None, story_id=None, format=None):
        if not project_id:
            return Response(status=404)

        if story_id:
            story = get_object_or_404(Story, pk=story_id)

            return Response(StorySerializer(story).data)
        
        project = get_object_or_404(Project, pk=project_id)

        stories = StoryListSerializer(
            Story.objects.filter(project=project), 
            many=True
        ).data

        return Response(stories)

    def post(self, request, project_id=None, story_id=None, format=None):
        if not project_id:
            return Response(status=404)
        
        data = request_to_dict(request)

        if not validate_story(data):
            return Response({'errors': ['Invalid data']}, status=400)
        
        project = get_object_or_404(Project, pk=project_id)

        if validate_content(data['content']):
            story = Story.objects.create(
                name="Default Name",
                content=story_content_formatter(data['content']),
                project=project
            )
            story.name = "Diálogo_{0}_{1}".format(story.project.name, story.id)
            story.save()

            return Response(StorySerializer(story).data, status=201)
        else:
            return Response({'errors': ['Invalid content array']}, status=400)

    def delete(self, request, project_id=None, story_id=None, format=None):
        story = get_object_or_404(Story, pk=story_id)
        story.delete()

        return Response(status=204)        

    def put(self, request, project_id=None, story_id=None, format=None):
        story = get_object_or_404(Story, pk=story_id)
        data = request_to_dict(request)

        if not validate_story(data):
            return Response({'errors': ['Invalid data']}, status=400)

        if validate_content(data['content']):
            for attr in data:
                if attr == 'content':
                    setattr(story, attr, story_content_formatter(data[attr]))
                else:
                    setattr(story, attr, data[attr])

            story.save()

            return Response(StorySerializer(story).data)
        else:
            return Response({'errors': ['Invalid content array']}, status=400)