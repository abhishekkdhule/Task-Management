from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from user.serializer import SignInSerializer, SignupSerializer

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
        serializer = SignInSerializer(data=request.data)
        if serializer.is_valid():
            #create some util or some helper
            access_token = serializer.validated_data.get('access_token')
            
            response = Response(data={'username': serializer.validated_data['username']}, status=status.HTTP_200_OK)
            response.set_cookie(key='access_token', value=access_token, httponly=True, samesite='none', secure=True)
            return response
        #once user is authenticated, generate a token 
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
