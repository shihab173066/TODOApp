from django.contrib import admin
from django.urls import path, include
from .views import TaskDetail, TaskList

urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task')
]
