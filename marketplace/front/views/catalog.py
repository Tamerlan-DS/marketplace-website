from django.shortcuts import render, redirect, get_object_or_404
from company.models import Company, Category, CompanyCategory , Reviews

def catalogPageView(request):
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = 'anon'
    companies = Company.objects.all()
    categories = Category.objects.filter(parent__isnull=True).all()
    context = {
        'username': username,
        'companies': companies,
        'categories': categories,
    }
    return render(request, 'front/catalog.html',context=context)


def catalogItemPageView(request, company_id):
    company = get_object_or_404(Company, pk=company_id)
    categories = Category.objects.all()
    revi = Reviews.objects.all()
    company_categories = Category.objects.filter(
        pk__in=CompanyCategory.objects.filter(company=company).values_list('category'))
    context = {
        'company': company,
        'categories': categories,
        'company_categories': company_categories,
        'Reviews': revi,
    }
    if request.method == 'POST':
        pk = request.POST['pk']
        name = request.POST['name']
        email = request.POST['email']
        review_text = request.POST['review']
        Review = Reviews.objects.create(name=name,pk_number=pk,email=email,review=review_text)
        Review.save()


    return render(request, 'front/catalog-item.html',context=context)

