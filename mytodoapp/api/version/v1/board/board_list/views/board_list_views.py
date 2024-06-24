from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..serializers.board_list_serializers import ListBoardSerializer
from mytodoapp.models.board_model import Board

class ListBoardAPI(APIView):
    def get(self, request):
        boards = Board.objects.all()
        serializer = ListBoardSerializer(boards,many=True)

        return Response({'message': 'Board Fetched Successfully', 'data': serializer.data}, status=status.HTTP_200_OK)