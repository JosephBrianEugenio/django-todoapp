from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from mytodoapp.models.task_model import Task
from mytodoapp.api.version.v1.task.edit_task.serializers.edit_task_serializers import UpdateTaskSerializer

class EditTaskAPI(APIView):
    def put(self, request, *args, **kwargs):
        data = {}
        status = None
        message = None
        errors = {}

        try: 
            id = request.query_params['id']
            task_id = Task.objects.get(id=id)
        except Task.DoestNotExist:
            message = 'Task does not exist'
            status = status.HTTP_400_BAD_REQUEST
            return Response({"status": status, "message": message, "errors": errors})
        
        serializerTask = UpdateTaskSerializer(task_id, data=request.data)

        if serializerTask.is_valid():
            serializerTask.save()
            status = 200
            message = 'Successfully updated Board'
            data = serializerTask.data
        else:
            status = 400
            message = 'Invalid Value'
            errors = serializerTask.errors
        
        return Response({"status": status, "message": message, "data": data, "errors": errors})
