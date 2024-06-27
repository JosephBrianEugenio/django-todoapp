from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User 
from ..serializers.task_list_serializers import ListTaskSerializer
from mytodoapp.models.task_model import Task
from rest_framework.permissions import IsAuthenticated
class ListTaskAPI(APIView):
    permission_classes =[IsAuthenticated]
    def get(self, request):
        tasks = Task.objects.filter(user = request.user.id)
        serializer = ListTaskSerializer(tasks, many=True)

        return Response({'message': 'Task Fetched Successfully', 'data': serializer.data}, status=status.HTTP_200_OK)