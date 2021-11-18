from rest_framework             import status, views
from rest_framework.response    import Response
from rest_framework_simplejwt.serializers   import TokenObtainPairSerializer
from boletbendapp import serializers

from boletbendapp.serializers   import UserSerializer

class UserCreateView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        token_data = {"email":request.data['email'],
                      "password":request.data['password']}
        token_serializer = TokenObtainPairSerializer(data=token_data)
        token_serializer.is_valid(raise_exception=True)
        return Response(token_serializer.validate_data, status=status.HTTP_201_CREATED)