from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from mytodoapp.models.board_model import Board
from mytodoapp.api.version.v1.board.edit_board.serializer.edit_board_serializers import UpdateBoardSerializer
from rest_framework.permissions import IsAuthenticated
class EditBoardAPI(APIView):
    permission_classes =[IsAuthenticated]
    def put(self,request,*args,**kwargs):
        data = {}

        status = None

        message = None

        errors = {}

        try: 
            id = request.query_params['id']
            board_id = Board.objects.get(id=id)
        except Board.DoesNotExist:
            message = 'Board does not exist'
            status = 400
            return Response({"status": status, "message": message, "errors": errors})
        
        serializerBoard = UpdateBoardSerializer(board_id,data=request.data)

        if serializerBoard.is_valid():
            serializerBoard.save()
            status = 200
            message = 'Successfully updated Board'
            data = serializerBoard.data
        else:
            status =400
            message = 'Invalid Value'
            errors = serializerBoard.errors

        return Response({"status": status, "message": message, "data": data, "errors": errors})
