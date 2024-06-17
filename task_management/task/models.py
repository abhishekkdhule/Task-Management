from django.db import models
from task.enums import TaskStatus

# class Task(models.Model):
#     user = models.CharField()
#     title = models.CharField(max_length=120)
#     description = models.CharField(max_length=500)
#     status = models.CharField(choices=[(ts.name, ts.value) for ts in TaskStatus], default='TO_DO', db_index=True)


    