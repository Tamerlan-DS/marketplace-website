from django.shortcuts import render, redirect, get_object_or_404
from company.models import Company, Category, CompanyCategory, Reviews, Services, Branches, Property, File, region
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator
from search.company import search_company
from django.db.models import Q


def catalogPageView(request):
    search_query = request.GET.get('search', None)
    city = request.GET.get('city', None)
    regiona = request.GET.get('region', None)
    properties = Property.objects.all()
    category_ids = request.GET.getlist('filter-category', [])
    categories = Category.objects.filter(Q(id__in=category_ids) | Q(parent__id__in=category_ids))
    companies = search_company(
        search_text=search_query,
        categories=categories,
        city=city,
        region=regiona,
    )
    company_number = search_company(
        search_text=search_query,
        categories=categories,
        city=city,
        region=regiona,
    ).count()
    paginator = Paginator(companies, 20)

    page_number = request.GET.get('page', 1)
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
    regions = region.objects.all()
    categories = Category.objects.filter(parent__isnull=True).all()
    context = {
        'username': username,
        'companies': page,
        'categories': categories,
        'is_paginated': is_paginated,
        'next_url': next_url,
        'regions': regions,
        'prev_url': prev_url,
        'number_of_companies': company_number,
        'properties': properties,
    }
    return render(request, 'front/catalog.html', context=context)


def catalogItemPageView(request, company_id):
    regions = region.objects.all()
    company = get_object_or_404(Company, pk=company_id)
    fil = File.objects.all()
    categories = Category.objects.all()
    services = Services.objects.filter(company_fk=company_id)
    revi = Reviews.objects.all()
    if(services):
        isServices=1
    else:
        isServices=0
    bran = Branches.objects.all()
    if(bran):
        isbranch=1
    else:
        isbranch=0
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
        'isServices': isServices,
        'isbranch': isbranch,
        'regions': regions,
        'File': fil,
    }
    if request.method == 'POST':
        pk = request.POST['pk']
        name = request.POST['name']
        email = request.POST['email']
        review_text = request.POST['review']
        Review = Reviews.objects.create(name=name, pk_number=pk, email=email, review=review_text)
        Review.save()
        return redirect('Catalog-item',company_id)

    return render(request, 'front/catalog-item.html', context=context)
