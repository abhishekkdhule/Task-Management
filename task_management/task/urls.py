from django.contrib import admin
from django.urls import path
from task.views import TaskView, TasksListView


urlpatterns = [
   path('task/<int:id>/', TaskView.as_view(), name='task'),
   path('task/', TasksListView.as_view(), name='tasks')

]
