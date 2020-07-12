from django.urls import path
from .views import *

urlpatterns = [
    path('', adminPanelView, name='panel'),
    path('companies', companyView, name='companies'),
    path('company-edit/<int:company_id>', companyEditView, name='company-edit'),
    path('company-add', companyAddView, name='company-add'),
    path('company-category', companyCategoryView, name='company-category'),
    path('company-category-edit', companyCategoryEditView, name='company-category-edit'),
    path('users-list', userListView, name='user-list-View'),
    path('login', loginView, name='login'),
]