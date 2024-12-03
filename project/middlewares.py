import json
from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin
from project import util
import time

import jwt
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError

class CustomAuthMiddleware(MiddlewareMixin):
    """
    Middleware for custom token-based authentication.
    """

    SECRET_KEY = "your_secret_key"  # Replace with your actual secret key
    ALGORITHM = "HS256"  # Algorithm to decode the token

    def process_request(self, request):
        print("CustomAuthMiddleware process_request INIT")
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
        except ExpiredSignatureError:
            return JsonResponse({'error': 'The token has expired'}, status=401)
        except InvalidTokenError:
            return JsonResponse({'error': 'The token is invalid'}, status=401)
        
