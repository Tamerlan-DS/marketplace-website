from django.shortcuts import render
from company.models import Company, Category
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

def blacklistPageView(request):
    companies = Company.objects.all()
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = 'anon'
    context = {
        'username': username,
        'companies': companies,
    }
    return render(request, 'front/black-list.html',context=context)

@csrf_exempt
def favouritesPageView(request):
    companies = Company.objects.all()
    arr = request.POST.get('arr[]')

    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = 'anon'
    context = {
        'username': username,
        'companies': companies,
        'cookies': arr,
    }
    return render(request, 'front/favourites.html',context=context)


def mobileSearchPageView(request):
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = 'anon'
    context = {
        'username': username,
    }
    return render(request, 'front/mobile-search.html',context=context)


def RegisterView(request):
    context = {
     }
    return render(request, 'front/auth-register.html', context=context)
