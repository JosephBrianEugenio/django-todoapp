from rest_framework import serializers
from mytodoapp.models.board_model import Board

class ListBoardSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Board
        fields = ['id',"board_name"]