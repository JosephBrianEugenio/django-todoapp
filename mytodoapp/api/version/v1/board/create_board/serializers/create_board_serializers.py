from rest_framework import serializers
from mytodoapp.models.board_model import Board

class CreateBoardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Board
        fields = ["board_name"]
        extra_kwargs = {
            'board_name': {'required': True}
        }