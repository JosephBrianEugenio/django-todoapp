from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password
from mytodoapp.validators.user_helper import UserHelper
from django.contrib.auth.models import User #user
from ..serializers.user_register_serializer import UserRegisterSerializer

class CreateUserAPI(APIView):
    def post(self, request):
    
        serializer = UserRegisterSerializer(data=request.data)

        errors = UserHelper.validate_data(self, request)

        if errors:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid():
            User.objects.create(
                username = request.data['username'],
                email = request.data['email'],
                password = make_password(request.data['password'])
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)