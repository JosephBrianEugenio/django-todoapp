from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from mytodoapp.models.task_model import Task
from mytodoapp.models.board_model import Board
from mytodoapp.api.version.v1.task.create_task.serializers.create_task_serializers import CreateTaskSerializer

class CreateTaskAPI(APIView):
    def post(self, request, *args, **kwargs):
        serializer = CreateTaskSerializer(data=request.data)
        if serializer.is_valid():
            id = request.query_params['id']
            print("board id here================================", id)
            board_id = Board.objects.get(id=id)
            task_due_date = serializer.data['task_due_date']
            Task.objects.create(
                board = board_id,
                task_due_date = task_due_date,
                task_name = request.data['task_name'],
                task_description = request.data['task_description'],
                # task_is_complete = request.data['task_is_complete'],
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)