from django.urls import path
from .views import *

urlpatterns = [
    path('', adminPanelView, name='panel'),

    path('companies', companyView, name='companies'),
    path('company-edit/<int:company_id>', companyEditView, name='company-edit'),
    path('company-testedit/<int:company_id>', companytestEditView, name='company-testedit'),
    path('company-add', companyAddView, name='company-add'),

    path('company-category', companyCategoryView, name='company-category'),
    path('company-category-edit/<int:category_id>', companyCategoryEditView, name='company-category-edit'),

    path('login', loginView, name='login'),
    path('logout', logoutView, name='logout'),

    path('employees', employeesView, name='employees'),
    path('employee-add', employeeAddView, name='employee-add'),
    path('employee-edit/<int:employee_card_id>', employeeEditView, name='employee-edit'),

    path('balance-charge/<int:user_id>', balanceChargeView, name='balance-charge'),

    path('takeout/company/<int:company_id>', companyTakeoutView, name='takeout-company'),

    path('news', newsView, name='admin-news'),
    path('news-edit/<int:news_id>', newsEditView, name='news-edit'),
    path('news-add', newsAddView, name='news-add'),

    path('reviews', ReviewsView, name='reviews'),
    path('review-edit/<int:Review_id>', ReviewsEditView, name='review-edit'),
]

