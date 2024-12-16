import json
from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin
from project import util
import time
from django.conf import settings

# import jwt
import jwt
from jwt import exceptions

class CustomAuthMiddleware(MiddlewareMixin):
    """
    Middleware for custom token-based authentication.
    """

    SECRET_KEY = '-----BEGIN PUBLIC KEY-----\nMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAERtpoqxlNuYWNlGlH4ABDucH7FnJ9\n4VqqqQrbBhx+7/jDcSOrgP5GhWyrYRgR45FSdonsHD7ddr/WvwJ7ekANwA==\n-----END PUBLIC KEY-----\n';
    ALGORITHM = 'ES256'

    def process_request(self, request):
        print("CustomAuthMiddleware process_request INIT")
        print(self.ALGORITHM)
        start_time = time.time()
        body = json.loads(request.body)
        token = body.get('billing_password')
        try:
            body = json.loads(request.body)
            decoded_payload = jwt.decode(token, self.SECRET_KEY, algorithms=[self.ALGORITHM])
            
            end_time = time.time()
            request.decoded_payload = decoded_payload
            print("CustomAuthMiddleware time taken: ", end_time - start_time)
            print("CustomAuthMiddleware process_request END")
        except Exception as e:
            print("CustomAuthMiddleware Exception: ", e)
            return JsonResponse({'error': 'Invalid token'}, status=401)
        
