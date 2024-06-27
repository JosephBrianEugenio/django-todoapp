from rest_framework import serializers
from mytodoapp.models.task_model import Task
from datetime import datetime

def convert_date_format(date_str):
    try:
        # Convert the date string to a date object in 'yyyy-mm-dd' format
        date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()
        # Format the date object as a string in 'yyyy-mm-dd' format
        formatted_date = date_obj.strftime('%Y-%m-%d')
        return formatted_date
    except ValueError:
        raise serializers.ValidationError("Invalid date format. Date must be in 'yyyy-mm-dd' format.")
    
class CustomDateField(serializers.DateField):
    def to_internal_value(self, value):
        if not value:
            return None
        return convert_date_format(value)

class CreateTaskSerializer(serializers.ModelSerializer):
    task_due_date = CustomDateField(required=False, allow_null=True)

    class Meta:
        model = Task
        fields = ["task_name", "task_description", "task_is_complete", "task_due_date", "board"]
        extra_kwargs = {
            'task_name': {'required': True},
            'task_description': {'required': True},
            'task_is_complete': {'required': False},
            'board': {'required': False},
        }
