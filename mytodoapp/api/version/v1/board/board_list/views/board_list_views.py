from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User 
from ..serializers.board_list_serializers import ListBoardSerializer
from mytodoapp.models.board_model import Board
from rest_framework.permissions import IsAuthenticated

class ListBoardAPI(APIView):
    permission_classes= [IsAuthenticated]
    def get(self, request):
        print("========================================================================", request.user.id)
        # user = get_user_from_token(request) 
        # if type(user) == dict: return Response(data=user, status=user['status'])
        boards = Board.objects.filter(user = request.user.id)
        serializer = ListBoardSerializer(boards, many=True)

        return Response({'message': 'Board Fetched Successfully', 'data': serializer.data}, status=status.HTTP_200_OK)