from django.core.exceptions import PermissionDenied
from .models import Card


def user_is_admin(function):
    def wrap(request, *args, **kwargs):
        try:
            card = request.user.card
        except Card.DoesNotExist:
            card = Card(owner=request.user)
        if (
                card.status == Card.StatusChoices.ACTIVE and
                card.role == Card.RoleChoices.ADMINISTRATOR
        ):
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap


def user_is_moder(function):
    def wrap(request, *args, **kwargs):
        try:
            card = request.user.card
        except Card.DoesNotExist:
            card = Card(owner=request.user)
        if (
                card.status == Card.StatusChoices.ACTIVE and
                (
                        card.role == Card.RoleChoices.MODERATOR or
                        card.role == Card.RoleChoices.ADMINISTRATOR
                )
        ):
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
