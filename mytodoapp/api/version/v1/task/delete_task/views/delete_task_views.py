from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from mytodoapp.models.task_model import Task
from mytodoapp.api.version.v1.task.delete_task.serializers.delete_task_serializers import DeleteTaskSerializer

class DeleteTaskAPI(APIView):
    def delete(self, request, *args, **kwargs):
        data = {}
        status = None
        message = None
        errors = {}

        if "id" in request.query_params:
            id = request.query_params["id"]
            try: 
                task = Task.objects.get(id=id)
            except Task.DoesNotExist:
                message = 'Board does not exist'
                status = 400
                return Response({"status": status, "message": message, "errors": errors})
            
            task.delete()
            message = 'Successfully Deleted'
            status = 200
        
        else:
            message = 'Invalid Value'
            status = 'status.HTTP_400_BAD_REQUEST'
            errors = DeleteTaskSerializer.errors

        return Response({"status": status, "message": message, "data": data, "errors": errors})