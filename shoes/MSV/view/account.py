from rest_framework.views import APIView
from rest_framework import serializers, status
from rest_framework.response import Response
from MSV.service.account import login
from MSV.utils import inline_serializer
from drf_yasg.utils import swagger_auto_schema

class LoginView(APIView):
    class InputSerializer(serializers.Serializer):
        username = serializers.CharField(max_length=255)
        password = serializers.CharField(max_length=255)

        class Meta:
            ref_name = 'Login'
            fields = ['username', 'password']
    
    class OutputSerializer(serializers.Serializer):
        access_token = serializers.CharField()
        account = inline_serializer(fields ={
            'id' : serializers.IntegerField(),
            'username': serializers.CharField(),
            'account_type': serializers.CharField(),
            'email': serializers.CharField()
        })

        class Meta:
            ref_name = 'Login'
            fiels=['access_token','account']
    @swagger_auto_schema(request_body = InputSerializer, responses = {200: OutputSerializer})
    def post(self, request):
        serializer = self.InputSerializer(data= request.data)
        result = login(**serializer.validated_data)
        return Response(self.OutputSerializer(result).data)