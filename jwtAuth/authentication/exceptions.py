from rest_framework.views import exception_handler
from utils.utils import *



def core_exception_handler(exc, context):

    response = exception_handler(exc, context)
    handlers = {
        'ValidationError': _handle_generic_error,
        'ParseError': _handle_generic_error,
        'AuthenticationFailed': _handle_generic_error,
        'NotAuthenticated': _handle_generic_error,
        'PermissionDenied': _handle_generic_error,
        'NotFound': _handle_generic_error,
        'MethodNotAllowed': _handle_generic_error,
        'NotAcceptable': _handle_generic_error,
        'UnsupportedMediaType': _handle_generic_error,
        'Throttled': _handle_generic_error
    }

    exception_class = exc.__class__.__name__

    if exception_class in handlers:

        return handlers[exception_class](exc, context, response, exception_class)


    return response

def _handle_generic_error(exc, context, response, error):

    if error == "ValidationError":
        response.data = responseSerializer(920, "Missing or Unacceptable Fields Exist")
    elif error == "AuthenticationFailed":
        response.data = responseSerializer(920, "Authentication is Failed For Some Reason")
    elif error == "PermissionDenied":
        response.data = responseSerializer(920, "You Don't Have a Permission To Do This Process")
    elif error == "MethodNotAllowed":
        response.data = responseSerializer(920, "This Method is Not Allowed")
    elif error == "UnsupportedMediaType":
        response.data = responseSerializer(920, "This Media is Not Supported")
    else:
        response.data = responseSerializer(920, error + " Occured")
    return response