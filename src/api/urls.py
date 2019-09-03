from django.contrib import admin
from django.urls import path, include

from .views import ListProjects

urlpatterns = [
    path('projects/', ListProjects.as_view()),
    path('projects/<int:project_id>/', ListProjects.as_view())
]
