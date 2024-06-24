from rest_framework import serializers
from mytodoapp.models.task_model import Task
class ListTaskSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Task
        fields = ["id", "task_name", "task_description", "task_is_complete", "task_due_date", "board_id"]



        
