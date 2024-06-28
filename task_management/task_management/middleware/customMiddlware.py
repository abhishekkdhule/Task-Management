from django.conf import settings
from django.utils.deprecation import MiddlewareMixin


class CustomJWTMiddleware(MiddlewareMixin):

    def process_request(self, request):
        if request.path not in ['/api/v1/auth/login/', '/api/v1/auth/signup/']:
            access_token = request.COOKIES.get(settings.JWT_TOKEN_COOKIE)
            if access_token:
                request.META['HTTP_AUTHORIZATION'] = f'Bearer {access_token}'
     