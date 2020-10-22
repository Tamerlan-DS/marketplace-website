from django.shortcuts import render
from company.models import Company, Category, Subscribes
from django.http import HttpResponse, HttpResponseRedirect

def FrontPageView(request):
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = 'anon'



    categories = Category.objects.all()
    companies = Company.objects.filter(status='ACCEPTED')
    context = {
        'username': username,
        'companies': companies,
        'categories': categories,

    }
    if request.method == 'POST':
        email = request.POST['email']
        Subscribes.objects.create(email=email)
        context['error'] = 0
        return render(request, 'front/index.html', context=context)

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
