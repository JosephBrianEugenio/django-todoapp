from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from mytodoapp.models.board_model import Board
from rest_framework_simplejwt.authentication import JWTAuthentication
from mytodoapp.api.version.v1.board.create_board.serializers.create_board_serializers import CreateBoardSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User 
class CreateBoardAPI(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        serializer = CreateBoardSerializer(data=request.data)
        if serializer.is_valid():
            user_obj = User.objects.get(id = request.user.id)
            Board.objects.create(
                    user = user_obj,
                    board_name = request.data['board_name']
                )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
