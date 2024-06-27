from .task_details_serializers import TaskDetailSerializer
from  rest_framework import generics
from mytodoapp.models.task_model import Task
from rest_framework.permissions import IsAuthenticated
class TaskDetailView(generics.RetrieveDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskDetailSerializer
    queryset = Task.objects.all()

# class TassView(generics.ListCreateAPIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = TaskDetailSerializer
#     queryset = Task.objects.all()
    