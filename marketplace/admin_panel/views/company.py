from django.shortcuts import render, redirect, get_object_or_404
from company.helper import *
from company.models import Company, Category
from ..models import Card
from django.contrib.auth.decorators import login_required


@login_required
def companyView(request):
    companies = Company.objects.all()
    context = {
        'companies': companies,
    }
    return render(request, 'admin_panel/admin-companies.html', context=context)


@login_required
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
                card = Card(owner=user, role=Card.RoleChoices.COMPANY_OWNER)
                card.save()
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


@login_required
def companyEditView(request, company_id):
    company = get_object_or_404(Company, pk=company_id)
    categories = Category.objects.all()
    context = {
        'company': company,
        'categories': categories,
    }
    if request.method == 'POST':
        type = request.POST['form']
        if type == 'info':
            name = request.POST['name']
            short_description = request.POST['short_description']
            description = request.POST['description']
            company_info = company.info
            company_info.name = name
            company_info.short_description = short_description
            company_info.description = description
            company_info.save()
        if type == 'category':
            categories_id = request.POST.getlist('categories')
            company_info = company.info
            company_info.categories.clear()
            for category_id in categories_id:
                category = Category.objects.get(pk=category_id)
                company_info.categories.add(category)

    else:
        pass

    return render(request, 'admin_panel/admin-company-edit.html', context=context)


@login_required
def companytestEditView(request, company_id):
    company = get_object_or_404(Company, pk=company_id)
    categories = Category.objects.all()
    context = {
        'company': company,
        'categories': categories,
    }
    if request.method == 'POST':
        type = request.POST['form']
        if type == 'info':
            name = request.POST['name']
            short_description = request.POST['short_description']
            description = request.POST['description']
            company_info = company.info
            company_info.name = name
            company_info.short_description = short_description
            company_info.description = description
            company_info.save()
        if type == 'category':
            categories_id = request.POST.getlist('categories')
            company_info = company.info
            company_info.categories.clear()
            for category_id in categories_id:
                category = Category.objects.get(pk=category_id)
                company_info.categories.add(category)

    else:
        pass

    return render(request, 'admin_panel/test/company-edit.html', context=context)


@login_required
def companyCategoryView(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    if request.method == 'POST':
        name = request.POST['name']
        if Category.objects.filter(name='name').count():
            context['error'] = 1
        elif not name:
            context['error'] = 2
        else:
            category = Category(name=name)
            category.save()
            context['error'] = 0
    return render(request, 'admin_panel/admin-company-category.html', context=context)


@login_required
def companyCategoryEditView(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    context = {
        'category': category,
    }
    if request.method == 'POST':
        name = request.POST['name']
        if category.name != name and Category.objects.filter(name='name').count():
            context['error'] = 1
        elif not name:
            context['error'] = 2
        else:
            category.name = name
            category.save()
            context['error'] = 0
    return render(request, 'admin_panel/admin-company-category-edit.html', context=context)
