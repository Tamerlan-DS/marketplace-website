from django.shortcuts import render, redirect, get_object_or_404
from company.helper import *
from company.models import Company, Category, CompanyCategory, news, Reviews
from admin_panel.models import Card
from django.contrib.auth.decorators import login_required
from admin_panel.decorators import *
from company_panel.models import Balance, Invoice


@login_required
@user_is_moder
def companyView(request):
    companies = Company.objects.all()
    context = {
        'companies': companies,
    }
    return render(request, 'admin_panel/admin-companies.html', context=context)


@login_required
@user_is_moder
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
                balance = Balance.objects.create(owner=user)
                balance.save()
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
@user_is_moder
def companyEditView(request, company_id):
    company = get_object_or_404(Company, pk=company_id)
    categories = Category.objects.all()
    company_categories = Category.objects.filter(
        pk__in=CompanyCategory.objects.filter(company=company).values_list('category'))
    context = {
        'company': company,
        'categories': categories,
        'company_categories': company_categories,
    }
    if request.method == 'POST':
        type = request.POST['form']
        if type == 'info':
            name = request.POST['name']
            short_description = request.POST['short_description']
            description = request.POST['description']
            city = request.POST['city']
            phone = request.POST['phone']
            email = request.POST['email']
            site = request.POST['site']
            worktime = request.POST['worktime']
            adress = request.POST['adress']
            company_info = company.info
            company_info.name = name
            company_info.short_description = short_description
            company_info.description = description
            company_info.city = city
            company_info.phone = phone
            company_info.email = email
            company_info.worktime = worktime
            company_info.adress = adress
            company_info.site = site
            company_info.save()
        if type == 'category':
            categories_id = request.POST.getlist('categories')
            company_categories = CompanyCategory.objects.filter(company=company)
            for company_category in company_categories:
                company_category.delete()
            for category_id in categories_id:
                category = Category.objects.get(pk=category_id)
                CompanyCategory(company=company, category=category).save()

    else:
        pass

    return render(request, 'admin_panel/admin-company-edit.html', context=context)


@login_required
@user_is_moder
def companytestEditView(request, company_id):
    company = get_object_or_404(Company, pk=company_id)
    categories = Category.objects.all()
    company_categories = Category.objects.filter(pk__in=CompanyCategory.objects.filter(company=company).values_list('category'))
    context = {
        'company': company,
        'categories': categories,
        'company_categories': company_categories,
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
            company_categories = CompanyCategory.objects.filter(company=company)
            for company_category in company_categories:
                company_category.delete()
            for category_id in categories_id:
                category = Category.objects.get(pk=category_id)
                CompanyCategory(company=company, category=category).save()

    else:
        pass

    return render(request, 'admin_panel/test/company-edit.html', context=context)


@login_required
@user_is_moder
def companyCategoryView(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    if request.method == 'POST':
        name = request.POST['name']
        parent_id = int(request.POST['parent_id'])
        if parent_id:
            parent = Category.objects.get(pk=parent_id)
        else:
            parent = None
        if Category.objects.filter(name=name).count():
            context['error'] = 1
        elif not name:
            context['error'] = 2
        else:
            category = Category(name=name, parent=parent)
            category.save()
            context['error'] = 0
    return render(request, 'admin_panel/admin-company-category.html', context=context)


@login_required
@user_is_moder
def companyCategoryEditView(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    context = {
        'category': category,
    }
    if request.method == 'POST':
        name = request.POST['name']
        if category.name != name and Category.objects.filter(name=name).count():
            context['error'] = 1
        elif not name:
            context['error'] = 2
        else:
            category.name = name
            category.save()
            context['error'] = 0
    return render(request, 'admin_panel/admin-company-category-edit.html', context=context)

@login_required
@user_is_moder
def balanceChargeView(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    balance = user.balance
    context = {
        'user_id': user_id,
    }
    if request.method == 'POST':
        value = int(request.POST['value'])
        invoice = Invoice.objects.create(value=value, balance=balance, from_administration=True)
        invoice.save()
        invoice.update()
    return render(request, 'admin_panel/test/balance_charge.html', context=context)


@login_required
@user_is_moder
def newsView(request):
    New = News.objects.all()
    context = {
        'New': New,
    }
    return  render(request,'admin_panel/admin-news.html', context=context)

@login_required
@user_is_moder
def newsEditView(request,news_id):
    new = get_object_or_404(News, pk=news_id)
    context = {
        'new': new,
    }
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        text = request.POST['text']
        New = new
        New.title = title
        New.description = description
        New.text = text
        New.save()
    return  render(request,'admin_panel/admin-news-edit.html', context=context)

@login_required
@user_is_moder
def newsAddView(request):
    context = {
    }
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        text = request.POST['text']
        New = News.objects.create(title=title,description=description,text=text)
        New.title = title
        New.description = description
        New.text = text
        New.save()
    return  render(request,'admin_panel/admin-news-add.html', context=context)

@login_required
@user_is_moder
def ReviewsView(request,):
    Review = Reviews.objects.all()
    companies = Company.objects.all()
    context = {
     'companies': companies,
     'Reviews': Review,
    }
    return  render(request,'admin_panel/admin-reviews.html', context=context)


@login_required
@user_is_moder
def ReviewsEditView(request, Review_id):
    Review = get_object_or_404(Reviews, pk=Review_id)
    context = {
        'Reviews': Review,
    }
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        review = request.POST['review']
        status = request.POST['status']
        Review.name = name
        Review.email = email
        Review.review = review
        if status == '0':
            Review.status = Review.StatusChoices.ACTIVE
        elif status == '1':
            Review.status = Review.StatusChoices.DELETED
        else:
            Review.status = Review.StatusChoices.PENDING
        Review.save()

    return render(request, 'admin_panel/admin-reviews-edit.html', context=context)