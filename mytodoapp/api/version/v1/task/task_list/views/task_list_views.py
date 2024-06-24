from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..serializers.task_list_serializers import ListTaskSerializer
from mytodoapp.models.task_model import Task

class ListTaskAPI(APIView):
    def get(self, request):
        tasks = Task.objects.all()
        serializer = ListTaskSerializer(tasks, many=True)

        return Response({'message': 'Task Fetched Successfully', 'data': serializer.data}, status=status.HTTP_200_OK)