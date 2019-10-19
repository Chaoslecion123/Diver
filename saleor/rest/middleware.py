import logging
from django.shortcuts import reverse
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django.contrib.auth.models import AnonymousUser
from rest_framework import exceptions

logger = logging.getLogger(__name__)


def jwt_middleware(get_response):
    """Sets the user object from a JWT header"""
    def middleware(request):
        logger.info(f"jwt_middleware request {request}")

        try:
            # if get user from JWT auth replace user and cached user
            authenticated = JSONWebTokenAuthentication().authenticate(request)
            msg = f"jwt_middleware authenticated {authenticated}"
            logger.info(msg)

            if authenticated:
                request._cached_user = authenticated[0]
                request.user = authenticated[0]
            # else:
            #     request.user = AnonymousUser()
        except exceptions.AuthenticationFailed as err:
            msg = f"jwt_middleware err {err}"
            logger.error(msg)
            # request.user = AnonymousUser()

        response = get_response(request)

        return response

    return middleware


def inspect_post(get_response):
    """Sets the user object from a JWT header"""
    def middleware(request):
        if request.method == 'POST':
            print(f"""*** *** ***
            POST METHODS DETECTED:

            {request.POST}
            """)

        response = get_response(request)
        return response

    return middleware
