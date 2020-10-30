from django.core.exceptions import PermissionDenied
from .models import Card
from company.models import Company

def user_is_admin(function):
    def wrap(request, *args, **kwargs):
        try:
            card = request.user.card
        except Card.DoesNotExist:
            card = Card(owner=request.user)
            card.save()
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
            card.save()
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

def user_is_company(function):
    def wrap(request, *args, **kwargs):
        try:
            card = request.user.card
        except Card.DoesNotExist:
            card = Card(owner=request.user)
            card.save()
        if (
                card.status == Card.StatusChoices.ACTIVE and
                (
                        card.role == Card.RoleChoices.MODERATOR or
                        card.role == Card.RoleChoices.ADMINISTRATOR or
                        card.role == Card.RoleChoices.COMPANY_OWNER
                )
        ):
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
def company_is_active(function):
    company = Company.objects.all()
    def wrap(request, *args, **kwargs):
        try:
            card = request.user.card
        except Card.DoesNotExist:
            card = Card(owner=request.user)
            card.save()
        if (
                card.status == Card.StatusChoices.ACTIVE and
                (
                        card.role == Card.RoleChoices.MODERATOR or
                        card.role == Card.RoleChoices.ADMINISTRATOR or
                        card.role == Card.RoleChoices.COMPANY_OWNER
                )
        ):
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
