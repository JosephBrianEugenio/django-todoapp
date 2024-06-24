from rest_framework import serializers
from mytodoapp.models.board_model import Board


class DeleteBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ['board_name']

