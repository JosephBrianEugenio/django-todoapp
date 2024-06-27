from rest_framework import serializers
from mytodoapp.models.task_model import Task

class TaskDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Task
        fields = ["task_name", "task_description", "task_is_complete","task_due_date", "board"]
    
