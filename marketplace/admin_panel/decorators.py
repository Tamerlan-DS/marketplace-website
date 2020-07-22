from django.core.exceptions import PermissionDenied
from .models import Card


def user_is_active(function):
    def wrap(request, *args, **kwargs):
        if request.user.card and request.user.card.status == Card.StatusChoices.ACTIVE:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap


def user_is_admin(function):
    def wrap(request, *args, **kwargs):
        if request.user.card and request.user.card.role == Card.RoleChoices.ADMINISTRATOR:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap


def user_is_moder(function):
    def wrap(request, *args, **kwargs):
        if request.user.card and request.user.card.role == Card.RoleChoices.MODERATOR:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
