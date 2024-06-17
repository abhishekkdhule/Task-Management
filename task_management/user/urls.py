from django.contrib import admin
from django.urls import path
from user.views import Login, SignUp



urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('login/', Login.as_view(), name='login')
]
