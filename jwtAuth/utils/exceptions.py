
from .utils import *
#from rest_framework_jwt.utils import UserSerializer

def jwt_response_payload_handler(token, user=None, request=None):
    return responseSerializer(200, {
        'token': token,
        #'user': UserSerializer(user, context={'request': request}).data
    })