from django.shortcuts import render,redirect
from company.models import Company, Category, Subscribes,  News, CompanyInfo, region
from admin_panel.models import Card
from company.helper import *
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from company_panel.models import Balance, Invoice

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
        type = request.POST['form']
        if type == 'consult':
            name = request.POST['name']
            phone = request.POST['phone']
            email = request.POST['email']
            text = request.POST['text']
            comp_id = request.POST['compid']
            company = Company.objects.get(pk=comp_id)
            existing_clicks = company.info.emailclicks
            existing_clicks += 1
            company.info.emailclicks = existing_clicks
            company.info.save()
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
            return redirect('Catalog-item', comp_id)
        if type == 'service-call':
            name = request.POST['name']
            phone = request.POST['phone']
            email = request.POST['email']
            text = request.POST['text']
            comp_id = request.POST['compid']
            service = request.POST['service']
            company = Company.objects.get(pk=comp_id)
            existing_clicks = company.info.serviceRequestclicks
            existing_clicks += 1
            company.info.serviceRequestclicks = existing_clicks
            company.info.save()
            company_email = request.POST['companyemail']
            send_mail('Заявка с сайта Topbuild',
                      'Имя отправителя: ' + name + '\n' +
                      'Телефон: ' + phone + '\n' +
                      'Email: ' + email + '\n' +
                      'Услуга: ' + service + '\n' +
                      text
                      ,
                      'ttopbild@mail.ru',
                      [company_email],
                      fail_silently=False,
                      )
            return redirect('Catalog-item', comp_id)

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


def companyRegisterView(request):
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
                return render(request, 'front/auth-register.html', context=context)
            except User.DoesNotExist:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                balance = Balance.objects.create(owner=user)
                balance.save()
                card = Card(owner=user, role=Card.RoleChoices.COMPANY_OWNER)
                card.save()
                create_company(user, name)

                return redirect('panel')
        else:
            context['error'] = 2
            return render(request, 'front/auth-register.html', context=context)
    else:
        context = {
        }
    return render(request, 'front/auth-register.html', context=context)
