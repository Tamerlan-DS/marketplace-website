from django.shortcuts import render, redirect, get_object_or_404
from company.models import Company, Category, CompanyCategory

def catalogPageView(request):
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = 'anon'
    companies = Company.objects.all()
    categories = Category.objects.all()
    context = {
        'username': username,
        'companies': companies,
        'categories': categories,
    }
    return render(request, 'front/catalog.html',context=context)


def catalogItemPageView(request, company_id):
    company = get_object_or_404(Company, pk=company_id)
    categories = Category.objects.all()
    company_categories = Category.objects.filter(
        pk__in=CompanyCategory.objects.filter(company=company).values_list('category'))
    context = {
        'company': company,
        'categories': categories,
        'company_categories': company_categories,
    }
    return render(request, 'front/catalog-item.html',context=context)

