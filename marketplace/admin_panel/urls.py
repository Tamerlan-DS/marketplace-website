from django.urls import path
from .views import *

urlpatterns = [
    path('', adminPanelView, name='panel'),
    path('companies', companyView, name='companies'),
    path('company-edit', companyEditView, name='company-edit'),
    path('company-add', companyAddView, name='company-add'),
    path('company-category', companyCategoryView, name='company-category'),
    path('company-category-edit', companyCategoryEditView, name='company-category-edit'),
]