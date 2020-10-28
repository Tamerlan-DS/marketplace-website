from django.shortcuts import render,redirect
from company.models import Company, Category, Subscribes,  News, CompanyInfo, region
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail

def blacklistPageView(request):
    regions = region.objects.all()
    companies = Company.objects.all()
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = 'anon'
    context = {
        'username': username,
        'regions': regions,
        'companies': companies,
    }
    return render(request, 'front/black-list.html',context=context)

@csrf_exempt
def favouritesPageView(request):
    regions = region.objects.all()
    companies = Company.objects.all()
    arr = request.POST.get('arr[]')

    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = 'anon'
    context = {
        'username': username,
        'regions': regions,
        'companies': companies,
        'cookies': arr,
    }
    return render(request, 'front/favourites.html',context=context)


def mobileSearchPageView(request):
    regions = region.objects.all()
    filteredcategories = Category.objects.filter(parent__isnull=True)
    companycities = CompanyInfo.objects.values_list('city', flat=True).distinct()
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = 'anon'
    context = {
        'username': username,
        'filteredcategories': filteredcategories,
        'companycities': companycities,
        'regions': regions,
    }
    return render(request, 'front/mobile-search.html',context=context)


def RegisterView(request):
    regions = region.objects.all()
    context = {
        'regions': regions,
     }
    return render(request, 'front/auth-register.html', context=context)

def mailerView(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        text = request.POST['text']
        comp_id = request.POST['compid']
        company_email = request.POST['companyemail']
        send_mail('Заявка с сайта Topbuild',
                  'Имя отправителя: ' + name + '\n' +
                  'Телефон: ' + phone + '\n' +
                  'Email: ' + email + '\n' +
                  text
                  ,
                  'ttopbild@mail.ru',
                  [company_email],
                  fail_silently=False,
                  )

    return redirect('Catalog-item',comp_id)


def SubscribeView(request):
    if request.method == 'POST':
        email = request.POST['email']
        Subscribes.objects.create(email=email)

    return HttpResponseRedirect('./')


def aboutPageView(request):
    regions = region.objects.all()
    context = {
        'regions': regions,
     }
    return render(request, 'front/about.html', context=context)

def forClientsPageView(request):
    regions = region.objects.all()
    context = {
        'regions': regions,
     }
    return render(request, 'front/for-clients.html', context=context)

def forMembersPageView(request):
    regions = region.objects.all()
    context = {
        'regions': regions,
     }
    return render(request, 'front/for-members.html', context=context)
