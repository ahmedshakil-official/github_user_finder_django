from django.urls import path
from github_api import views

app_name: 'git_api'
urlpatterns = [
    path('', views.index, name='home'),
]