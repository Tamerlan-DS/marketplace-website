from django.urls import path
from .views import *

urlpatterns = [
    path('', FrontPageView, name='FrontPage'),
    path('catalog', catalogPageView, name='Catalog'),
    path('catalog-item', catalogItemPageView, name='Catalog-item'),

    path('contacts', contactPageView, name='contact'),

    path('default', defaultPageView, name='default'),
    path('error', errorPageView, name='error'),
    path('black-list', blacklistPageView, name='black-list'),
    path('favourites', favouritesPageView, name='favourites'),

    path('news', newsPageView, name='news'),
    path('news-item', newsItemPageView, name='news-item'),


]
