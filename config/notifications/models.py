from django.db import models

from config.tasks.models import Task

# Create your models here.
class TaskReminder(models.Model):
    task = models.ForeignKey(
        Task, 
        on_delete=models.CASCADE, 
        related_name='reminders'
    )
    remind_at = models.DateTimeField()
    notified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    