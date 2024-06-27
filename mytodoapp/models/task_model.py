from django.db import models
from mytodoapp.models.board_model import Board
from django.contrib.auth.models import User
class Task(models.Model):
    task_name = models.CharField(max_length=255, null=True)
    task_description = models.TextField(null=True)
    task_is_complete = models.BooleanField(default=False)
    task_due_date = models.DateField(null=True, blank=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='tasks')
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    class Meta:
        verbose_name_plural = "Tasks"

    def __str__(self):
        return self.task_name