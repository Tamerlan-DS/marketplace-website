from django.shortcuts import render
from company.models import Company, Category

def FrontPageView(request):
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = 'anon'
    categories = Category.objects.all()
    companies = Company.objects.all()
    context = {
        'username': username,
        'companies': companies,
        'categories': categories,

    }

    return render(request, 'front/index.html',context=context)


def contactPageView(request):
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = 'anon'
    context = {
        'username': username,
    }
    return render(request, 'front/contact.html',context=context)
