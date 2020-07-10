from django.urls import path
from .views import *

urlpatterns = [
    path('', adminPanelView, name='companies'),
    path('companies', companyView, name='companies'),
    path('company-edit', companyEditView, name='company-edit'),
    path('company-category', companyCategoryView, name='company-category'),
    path('company-category-edit', companyCategoryEditView, name='company-category-edit'),
]