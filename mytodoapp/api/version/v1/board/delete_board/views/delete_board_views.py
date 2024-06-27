from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from mytodoapp.models.board_model import Board
from mytodoapp.api.version.v1.board.delete_board.serializers.delete_board_serializers import DeleteBoardSerializer
from rest_framework.permissions import IsAuthenticated
class DeleteBoardAPI(APIView):
    permission_classes =[IsAuthenticated]
    def delete(self, request, *args, **kwargs):
        data = {}
        status = None
        message = None
        errors = {}

        if "id" in request.query_params:
            id = request.query_params["id"]
            try: 
                board = Board.objects.get(id=id)
            except Board.DoesNotExist:
                message = 'Board does not exist'
                status = 400
                return Response({"status": status, "message": message, "errors": errors})
            
            board.delete()
            message = 'Successfully Deleted'
            status = 200
            
        else:
            message = 'Invalid Value'
            status = 400
            errors = DeleteBoardSerializer.errors

        return Response({"status": status, "message": message, "data": data, "errors": errors})
