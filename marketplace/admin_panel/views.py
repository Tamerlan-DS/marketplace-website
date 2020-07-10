from django.shortcuts import render
from .froms import *
from company.helper import *


# Create your views here.
def adminPanelView(request):
    context = {
    }
    return render(request, 'admin_panel/index.html', context=context)

def companyView(request):
    context = {
    }
    return render(request, 'admin_panel/admin-companies.html', context=context)


def companyCategoryView(request):
    context = {
    }
    return render(request, 'admin_panel/admin-company-category.html', context=context)


def companyEditView(request):
    context = {
    }
    return render(request, 'admin_panel/admin-company-edit.html', context=context)

def companyAddView(request):
    if request.method == 'POST':
        form = CompanyRegisterForm(data=request.POST)
        if form.is_valid():
            user = form.register(request)
            # create_company(user, "asd")
            # print("HELLO")
    else:
        form = CompanyRegisterForm()

    context = {
        'form': form,
    }
    return render(request, 'admin_panel/admin-company-add.html', context=context)


def companyCategoryEditView(request):
    context = {
    }
    return render(request, 'admin_panel/admin-company-category-edit.html', context=context)


def loginView(request):
    context = {
    }
    return render(request, 'admin_panel/admin-login.html', context=context)


def forgotPasswordView(request):
    context = {
    }
    return render(request, 'admin_panel/admin-forgot-password.html', context=context)


def resetPasswordView(request):
    context = {
    }
    return render(request, 'admin_panel/admin-reset-password.html', context=context)


def employeeView(request, ):
    context = {
    }
    return render(request, 'admin_panel/admin-sotrud.html', context=context)


def employeeEditView(request):
    context = {
    }
    return render(request, 'admin_panel/admin-sotrud.html', context=context)

def userListView(request):
    context = {
    }
    return render(request, 'admin_panel/page-users-list.html', context=context)