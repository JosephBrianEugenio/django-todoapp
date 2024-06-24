from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from mytodoapp.models.board_model import Board
from mytodoapp.api.version.v1.board.create_board.serializers.create_board_serializers import CreateBoardSerializer


class CreateBoardAPI(APIView):
    def post(self, request, format=None):
        serializer = CreateBoardSerializer(data=request.data)
        if serializer.is_valid():
            Board.objects.create(
                board_name = request.data['board_name']
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
