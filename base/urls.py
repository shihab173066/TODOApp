from django.contrib import admin
from django.urls import path, include
from .views import TaskList

urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
]
