from django.urls import path
from .views import *


urlpatterns = [
    path('', FrontPageView, name='FrontPage'),
    path('catalog', catalogPageView, name='Catalog'),
    path('catalog-item/<int:company_id>', catalogItemPageView, name='Catalog-item'),

    path('contacts', contactPageView, name='contact'),

    path('default', defaultPageView, name='default'),
    path('error', errorPageView, name='error'),
    path('black-list', blacklistPageView, name='black-list'),
    path('favourites', favouritesPageView, name='favourites'),
    path('auth-register', RegisterView, name='auth-register'),
    path('mailer', mailerView, name='mailer'),
    path('subscribe', SubscribeView, name='subscribe'),


    path('mobile-search', mobileSearchPageView, name='mobile-search'),

    path('news', newsPageView, name='news'),
    path('news-item/<int:news_id>', newsItemPageView, name='news-item'),



]
