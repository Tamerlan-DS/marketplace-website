from django.urls import path
from .views import *

urlpatterns = [
    path('', FrontPageView, name='FrontPage'),
]
