from django.db import models


# Create your models here.

class UserTask(models.Model):
    task_name = models.CharField(max_length=100)
    task_complete = models.BooleanField(default=False)
    task_created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task_name
