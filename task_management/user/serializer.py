from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError

class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=25)
    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    def validate(self, attrs):
        if attrs.get("email", None) is None:
            raise ValidationError({'email':"Email is required field"})
        return super().validate(attrs)
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class SignInSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField()
    class Meta:
        model = User
        fields = ['username', 'password']
    
    def validate(self, attrs):
        validated_data = super().validate(attrs)
        username = validated_data.get("username")
        password = validated_data.get("password")
        user = authenticate(username=username, password=password)
        if user is None:
            raise AuthenticationFailed("Invalid Credentials")
        if not user.is_active:
            raise AuthenticationFailed("Inactive User")
        tokens = self.get_user_token(user)
        return {**tokens, 'username': username}
       
    
    def get_user_token(self, user):
        tokens = RefreshToken.for_user(user)
        return {
            'access_token': str(tokens.access_token),
            'refresh_token': str(tokens.token)
        }