from django.shortcuts import render
from django.contrib.auth.models import User
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


def companyEditView(request):
    context = {
    }
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
<<<<<<< HEAD
        pass
    context = {
        'username': 'ynsm',
        'name': 'Dias',
    }
=======
        context = {
        }
>>>>>>> eaad9f53514c7cbf2c0fa97af4ef3e2948cdad49
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
