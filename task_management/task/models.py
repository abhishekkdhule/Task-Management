from django.db import models
from task.enums import TaskStatus
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=500)
    status = models.CharField(choices=[(ts.name, ts.value) for ts in TaskStatus], max_length=24, default='TO_DO', db_index=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.user.username} - {self.title}"

    