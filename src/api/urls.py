from django.contrib import admin
from django.urls import path, include

from .views import *

urlpatterns = [
    path('projects/', ListProjects.as_view()),
    path('projects/<int:project_id>/', ListProjects.as_view()),
    path('projects/<int:project_id>/intents/', ListIntents.as_view()),
    path('projects/<int:project_id>/intents/<int:intent_id>', ListIntents.as_view()),
    path('projects/<int:project_id>/intents/<int:intent_id>/example', ListIntentExample.as_view()),
    path('projects/<int:project_id>/utters/', ListUtters.as_view()),
    path('projects/<int:project_id>/utters/<int:utter_id>', ListUtters.as_view()),  
    path('projects/<int:project_id>/utters/<int:utter_id>/example', ListUtterExample.as_view()),
    path('projects/<int:project_id>/stories/', ListStories.as_view()),
    path('projects/<int:project_id>/stories/<int:story_id>', ListStories.as_view()),
    path('files/<int:project_id>/stories/', StoriesFile.as_view(), name='stories-file'),
    path('files/<int:project_id>/intents/', IntentsFile.as_view(), name='intents-file'),
    path('files/<int:project_id>/domain/', DomainFile.as_view(), name='domain-file'),
    path('files/<int:project_id>/zip/', ZipFile.as_view(), name='zip-file')
]
