
from django.urls import path
from .views import * 

urlpatterns = [
    path('', about_me, name="about-me"),
    path('signup', signup),
    path('about-me', about_me, name='about-me'),
    path('projects', projects, name='projects'),
    path('contact', contact, name='contact'),
    path('project-details/<id>', projects_details, name="project_details")
]
