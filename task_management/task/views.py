from datetime import datetime
from django.http import Http404
from django.shortcuts import render
from rest_framework.views import APIView
from task.models import Task
from task.serializer import TaskCreateSerializer, TaskSerializer, TasksListSerializer
from rest_framework import status
from rest_framework.response import Response

class TaskView(APIView):

    def get_task(self, task_id) -> Task:
        try:
            task = Task.objects.get(id=task_id)
            return task
        except Task.DoesNotExist:
            raise Http404()
    
    def get(self, request, id:int):
        task = self.get_task(task_id=id)
        serializer = TaskSerializer(task) 
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, id:int):
        user_id = request.user.id
        task_data = {**request.data, 'user':user_id}
        task = self.get_task(task_id=id)
        serializer = TaskSerializer(task, data=task_data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.validated_data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id:int):
        task = self.get_task(task_id=id)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TasksListView(APIView):

    def get(self, request):
        user_id = request.user.id
        dateStr = request.GET.get('date', None)
        date = datetime.strptime(dateStr, '%d/%m/%Y')
        filterObject = {
            'user_id':user_id, 
            'created_date__date':date
        }
        task_status = request.GET.get('status', None)
        if task_status:
            task_status = task_status.split(',')
            filterObject['status__in'] = task_status
       
        tasks = Task.objects.filter(**filterObject)
        serializer = TasksListSerializer(tasks, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
        

    def post(self, request):
        user_id = request.user.id
        task_data = {**request.data, 'user':user_id}
        serializer = TaskCreateSerializer(data=task_data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    
