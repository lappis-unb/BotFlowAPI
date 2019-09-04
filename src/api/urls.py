from django.contrib import admin
from django.urls import path, include

from .views import ListProjects, ListIntents, ListUtters

urlpatterns = [
    path('projects/', ListProjects.as_view()),
    path('projects/<int:project_id>/', ListProjects.as_view()),
    path('projects/<int:project_id>/intents/', ListIntents.as_view()),
    path('projects/<int:project_id>/intents/<int:intent_id>', ListIntents.as_view()),
    path('projects/<int:project_id>/utters/', ListUtters.as_view()),
    path('projects/<int:project_id>/utters/<int:utter_id>', ListUtters.as_view()),
]
