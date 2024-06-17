from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from user.serializer import SignupSerializer

class SignUp(APIView):

    def post(self, request):
        data = request.data
        userSignUp = SignupSerializer(data=data)
        if userSignUp.is_valid():
            userSignUp.save()
            return Response(data=userSignUp.validated_data, status=status.HTTP_201_CREATED)
        return Response(data=userSignUp.errors, status=status.HTTP_400_BAD_REQUEST)

class Login(APIView):
    def post(self, request):
        data = request.data
        username = data.get('username', None)
        password = data.get('password', None)
        user = authenticate(username=username, password=password)
        #once user is authenticated, generate a token 
