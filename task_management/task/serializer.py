from rest_framework.serializers import ModelSerializer

from task.models import Task


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status']

class TaskCreateSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class TasksListSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"