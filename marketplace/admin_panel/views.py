from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from company.helper import *
from company.models import Company


# Create your views here.
def adminPanelView(request):
    context = {
    }
    return render(request, 'admin_panel/index.html', context=context)


def companyView(request):
    companies = Company.objects.all()
    context = {
        'companies': companies,
    }
    return render(request, 'admin_panel/admin-companies.html', context=context)


def companyCategoryView(request):
    context = {
    }
    return render(request, 'admin_panel/admin-company-category.html', context=context)


def companyEditView(request, company_id):
    company = get_object_or_404(Company, pk=company_id)
    context = {
        'company': company,
    }
    if request.method == 'POST':
        name = request.POST['name']
        short_description = request.POST['short_description']
        description = request.POST['description']
        company_info = company.info
        company_info.name = name
        company_info.short_description = short_description
        company_info.description = description
        company_info.save()
    else:
        pass

    return render(request, 'admin_panel/admin-company-edit.html', context=context)


def companyAddView(request):
    if request.method == 'POST':
        username = request.POST['username']
        name = request.POST['name']
        password = request.POST['password']
        re_password = request.POST['re_password']
        context = {
            'username': username,
            'name': name,
        }
        if password == re_password:
            try:
                user = User.objects.get(username=username)
                context['error'] = 1
                return render(request, 'admin_panel/admin-company-add.html', context=context)
            except User.DoesNotExist:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                create_company(user, name)
                context['error'] = 0
                return render(request, 'admin_panel/admin-company-add.html', context=context)
        else:
            context['error'] = 2
            return render(request, 'admin_panel/admin-company-add.html', context=context)
    else:
        context = {
        }
    return render(request, 'admin_panel/admin-company-add.html', context=context)


def companyCategoryEditView(request):
    context = {
    }
    return render(request, 'admin_panel/admin-company-category-edit.html', context=context)


def loginView(request):
    if request.user.is_authenticated:
        return redirect('panel')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('panel')

    return render(request, 'admin_panel/admin-login.html')


def logoutView(request):
    logout(request)
    return redirect('login')


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
