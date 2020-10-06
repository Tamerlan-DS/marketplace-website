from django.shortcuts import render, redirect, get_object_or_404
from company.helper import *
from company.models import Company, Category, CompanyCategory, news, Reviews, Services, branches
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
    services = Services.objects.all()
    categories = Category.objects.all()
    branche = Branches.objects.all()
    company_categories = Category.objects.filter(
        pk__in=CompanyCategory.objects.filter(company=company).values_list('category'))
    context = {
        'company': company,
        'categories': categories,
        'company_categories': company_categories,
        'services': services,
        'branches': branche,
    }
    if request.method == 'POST':
        type = request.POST['form']
        if type == 'info' and request.POST['email']:
            name = request.POST['name']
            short_description = request.POST['short_description']
            description = request.POST['description']
            city = request.POST['city']
            phone = request.POST['phone']
            email = request.POST['email']
            site = request.POST['site']
            worktime = request.POST['worktime']
            adress = request.POST['adress']
            status = request.POST['status']
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

            if status == '0':
                company.status = company.StatusChoices.ACCEPTED
            elif status == '1':
                company.status = company.StatusChoices.PENDING
            elif status == '2':
                company.status = company.StatusChoices.BANNED
            company_info.save()
            company.save()
            return render(request, 'front/catalog-item.html', context=context)

        if type == 'category':
            categories_id = request.POST.getlist('categories')
            company_categories = CompanyCategory.objects.filter(company=company)
            for company_category in company_categories:
                company_category.delete()
            for category_id in categories_id:
                category = Category.objects.get(pk=category_id)
                CompanyCategory(company=company, category=category).save()
            return render(request, 'front/catalog-item.html', context=context)

        if type == 'service':
            name = request.POST['name']
            description = request.POST['description']
            price = request.POST['price']
            Services.objects.create(name=name, description=description, price=price, company_fk=company.pk)
            return render(request, 'front/catalog-item.html', context=context)

        if type == 'branches':
            city = request.POST['city']
            address = request.POST['address']
            phone = request.POST['phone']
            email = request.POST['email']
            worktime = request.POST['worktime']

            Branches.objects.create(city=city, address=address, phone=phone, email=email, worktime=worktime,
                                    company_fk=company.pk)
            return render(request, 'admin_panel/admin-company-edit.html', context=context)


        if type == 'files':
            files = company.files
            print('!!!!')
            print(request.FILES.get('myfile'))
            print('!!!!')
            files.picture = request.FILES.get('picture')
            files.banner = request.FILES.get('banner')
            files.save()



    else:
        pass

    return render(request, 'admin_panel/admin-company-edit.html', context=context)


@login_required
@user_is_moder
def companytestEditView(request, company_id):
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
            company_info = company.info
            company_info.name = name
            company_info.short_description = short_description
            company_info.description = description
            company_info.save()
            return render(request, 'front/catalog-item.html', context=context)

        if type == 'category':
            categories_id = request.POST.getlist('categories')
            company_categories = CompanyCategory.objects.filter(company=company)
            for company_category in company_categories:
                company_category.delete()
            for category_id in categories_id:
                category = Category.objects.get(pk=category_id)
                CompanyCategory(company=company, category=category).save()

        if type == 'files':
            files = company.files
            files.banner = request.FILES.get('banner', None)
            files.picture = request.FILES.get('picture', None)
            files.save()

    else:
        pass

    return render(request, 'admin_panel/test/company-edit.html', context=context)


@login_required
@user_is_moder
def companyCategoryView(request):
    categories = Category.objects.all()
    parents = categories.filter(parent__isnull=True)
    context = {
        'categories': categories,
        'parents': parents,
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
    return render(request, 'admin_panel/admin-news.html', context=context)


@login_required
@user_is_moder
def newsEditView(request, news_id):
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
    return render(request, 'admin_panel/admin-news-edit.html', context=context)


@login_required
@user_is_moder
def newsAddView(request):
    context = {
    }
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        text = request.POST['text']
        New = News.objects.create(title=title, description=description, text=text)
        New.title = title
        New.description = description
        New.text = text
        New.save()
    return render(request, 'admin_panel/admin-news-add.html', context=context)


@login_required
@user_is_moder
def ReviewsView(request, ):
    Review = Reviews.objects.all()
    companies = Company.objects.all()
    context = {
        'companies': companies,
        'Reviews': Review,
    }
    return render(request, 'admin_panel/admin-reviews.html', context=context)


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

    return render(request, 'admin_panel/admin-reviews-edit.html', context=context)


@login_required
@user_is_moder
def TarifView(request,company_id):
    company = get_object_or_404(Company, pk=company_id)
    tarifes=Tarif.objects.all()
    if request.method == 'POST':
        company_tarifes = CompanyTarif.objects.filter(company=company)
        tarif_id = request.POST.getlist('tarif')
        print(tarif_id)
        for company_tarif in company_tarifes:
            company_tarif.delete()
        for tarify in tarif_id:
            tarif=Tarif.objects.get(pk=tarify)
            CompanyTarif(company=company,tarif=tarif).save()

    context = {
        'company':company,
        'tarifes':tarifes,
    }
    return render(request, 'admin_panel/admin-tarif.html', context=context)

@login_required
@user_is_moder
def TarifAddView(request):

    if request.method == 'POST':
        name = request.POST['name']
        price = request.POST['price']
        timeleft = request.POST['timeleft']
        tarif = Tarif.objects.create(name=name,price=price,timeleft=timeleft)
    context = {
    }
    return render(request, 'admin_panel/admin-tarif-add.html', context=context)

@login_required
@user_is_moder
def BalanceView(request):
    user = request.user
    company = Company.objects.get(owner=user)
    company_tarifes = CompanyTarif.objects.filter(company=company)
    try:
        balance = user.balance
    except Balance.DoesNotExist:
        balance = Balance(owner=user)
        balance.save()
    if request.method == 'POST':
        type = request.POST['charge']
        if type=='charge':
            if(company.charged==False):
               for company_tarif in company_tarifes:
                   print(user.balance.value)
                   local_time = company_tarif.tarif.timeleft
                   print(company.status)
                   company.charged = True
                   company.save()
                   Charge(company_tarif,user)



    context = {
        'balance':balance,
        'user': user,
        'company': company,
    }
    return render(request, 'admin_panel/admin-balance.html', context=context)


def Charge(company_tarif,user):

    tarif_price = company_tarif.tarif.price
    user.balance.value = user.balance.value - tarif_price
    user.save()


    return

