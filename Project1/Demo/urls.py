from django.urls import path
from .views import *

urlpatterns = [
path('users/create/', UserCreateAPIView.as_view(), name='user_create'),
path('clients/', ClientListAPIView.as_view(), name='client_list'),
path('clients/create/', ClientCreateAPIView.as_view(), name='client_create'),
path('clients/<int:pk>/', ClientUpdateDeleteAPIView.as_view(), name='client_update_delete'),
path('projects/create/', ProjectCreateAPIView.as_view(), name='project_create'),
path('projects/<int:pk>/', ProjectUpdateDeleteAPIView.as_view(), name='project_update_delete'),
path('projects/<int:pk>/assign-user/', ProjectAssignUserAPIView.as_view(), name='project_assign_user'),
path('user-projects/', UserProjectsListAPIView.as_view(), name='user_projects_list'),
]