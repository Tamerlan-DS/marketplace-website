from django.shortcuts import render, redirect, get_object_or_404
from company.models import Company, Category, CompanyCategory , Reviews, Services, Branches
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator
from django.db.models import Q

def catalogPageView(request):

    search_query = request.GET.get('search', '')

    if search_query:
        companies = Company.objects.filter( Q(info__name = search_query) | Q(info__description = search_query))
    else:
        companies = Company.objects.all()

    paginator = Paginator(companies , 10)


    page_number =  request.GET.get('page',1)
    page = paginator.get_page(page_number)

    is_paginated = page.has_other_pages()

    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''

    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = 'anon'



    categories = Category.objects.filter(parent__isnull=True).all()
    context = {
        'username': username,
        'companies': companies,
        'categories': categories,
        'is_paginated': is_paginated,
        'next_url': next_url,
        'prev_url': prev_url,

    }
    return render(request, 'front/catalog.html',context=context)


def catalogItemPageView(request, company_id):
    company = get_object_or_404(Company, pk=company_id)
    categories = Category.objects.all()
    services = Services.objects.all()
    revi = Reviews.objects.all()
    branche = Branches.objects.all()
    company_categories = Category.objects.filter(
        pk__in=CompanyCategory.objects.filter(company=company).values_list('category'))
    context = {
        'company': company,
        'categories': categories,
        'company_categories': company_categories,
        'Reviews': revi,
        'services': services,
        'branches': branche,
    }
    if request.method == 'POST':
        pk = request.POST['pk']
        name = request.POST['name']
        email = request.POST['email']
        review_text = request.POST['review']
        Review = Reviews.objects.create(name=name,pk_number=pk,email=email,review=review_text)
        Review.save()
        return render(request, 'front/catalog-item.html',context=context)


    return render(request, 'front/catalog-item.html',context=context)

