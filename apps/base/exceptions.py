from fastapi import HTTPException
from fastapi.exceptions import RequestValidationError
from starlette.responses import JSONResponse


def global_exception_handler(request, exc):
    err_msg = 'Server Internal Error' if exc.status_code == 500 else exc.message
    return JSONResponse({
        'code': exc.status_code,
        'msg': err_msg
    })


def validate_exception_handler(request, exc):
    err = exc.errors()[0]
    return JSONResponse({
        'code': 400,
        'msg': err['msg']
    })


def check_exception_handler(request, exc):
    return JSONResponse({
        'code': 420,
        'msg': exc.message
    })


def auth_exception_handler(request, exc):
    return JSONResponse({
        'code': 401,
        'msg': exc.message
    })


class CheckError(Exception):
    """ Base class for arithmetic errors. """

    def __init__(self, message):  # real signature unknown
        self.message = message

    def __str__(self):
        """ Create and return a new object.  See help(type) for accurate signature. """
        return f"{self.message}"


class CheckDuplicate(Exception):
    """ Base class for arithmetic errors. """

    def __init__(self, message):  # real signature unknown
        self.message = message

    def __str__(self):
        """ Create and return a new object.  See help(type) for accurate signature. """
        return f"{self.message}"


class AuthError(Exception):
    """ Base class for arithmetic errors. """

    def __init__(self, message):  # real signature unknown
        self.message = message

    def __str__(self):
        """ Create and return a new object.  See help(type) for accurate signature. """
        return f"{self.message}"


class ServerError(Exception):
    """ Base class for arithmetic errors. """

    def __init__(self, message, status_code=500):  # real signature unknown
        self.message = message
        self.status_code = status_code

    def __str__(self):
        """ Create and return a new object.  See help(type) for accurate signature. """
        return f"{self.message}"


global_exception_handlers = {
    HTTPException: global_exception_handler,
    RequestValidationError: validate_exception_handler,
    CheckError: check_exception_handler,
    CheckDuplicate: check_exception_handler,
    AuthError: auth_exception_handler,
    ServerError: global_exception_handler
}
