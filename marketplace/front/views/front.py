from django.shortcuts import render
from company.models import Company, Category, Subscribes, News, CompanyInfo, City, region
from django.http import HttpResponse, HttpResponseRedirect

def FrontPageView(request):
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = 'anon'
    New = News.objects.order_by('-pk')
    regions = region.objects.all()
    cities = City.objects.all()
    filteredcategories = Category.objects.filter(parent__isnull=True)
    companycities = CompanyInfo.objects.values_list('city',flat=True).distinct()
    print(companycities)
    categories = Category.objects.all()
    companies = Company.objects.filter(status='ACCEPTED')
    context = {
        'username': username,
        'companies': companies,
        'categories': categories,
        'filteredcategories': filteredcategories,
        'companycities': companycities,
        'cities': cities,
        'regions': regions,
        'News': New,
    }
    if request.method == 'POST':
        email = request.POST['email']
        Subscribes.objects.create(email=email)
        context['error'] = 0
        return render(request, 'front/index.html', context=context)

    return render(request, 'front/index.html',context=context)


def contactPageView(request):
    regions = region.objects.all()
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = 'anon'
    context = {
        'username': username,
        'regions': regions,
    }
    return render(request, 'front/contact.html',context=context)
