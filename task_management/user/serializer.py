from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User

class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=25)
    # confirm_password = serializers.CharField(max_length=25)
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
    
       

# class SigninSerializer(serializers.ModelSerializer):
#     email = serializers.EmailField()
#     password = serializers.CharField(max_length=60)

#     class Meta:
#         model = User
#         fields = ['email', 'password']

#     def validate(self, attrs):
#         email = attrs['email']
#         password = attrs['password']
#         user = authenticate(email=email, password=password)
#         if user is None:
#             raise AuthenticationFailed("Invalid Credentials")
#         if not user.is_active:
#             raise AuthenticationFailed("Inactive User")
#         tokens = self.get_user_token(user)
#         return {
#             "email": email,
#             **tokens
#         }
    
#     def get_user_token(self, user):
#         refresh = RefreshToken.for_user(user)

#         return {
#             'refresh_token': str(refresh),
#             'access_token': str(refresh.access_token),
#         }
        