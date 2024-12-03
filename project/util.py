import jwt
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError

SECRET_KEY = "your_secret_key"  # Replace with your actual secret key
ALGORITHM = "HS256"  # Algorithm to encode the token

def decode_payload(token):
    """
    Decode the token and return the payload.
    """
    try:
        # Decode the token
        decoded_payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return decoded_payload
    except ExpiredSignatureError:
        return {'error': 'The token has expired'}
    except InvalidTokenError:
        return {'error': 'The token is invalid'}
    
    