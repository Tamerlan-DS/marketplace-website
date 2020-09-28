from django.shortcuts import render, redirect, get_object_or_404
from company.helper import *
from company.models import Company, Category, CompanyCategory, news
from admin_panel.models import Card
from django.contrib.auth.decorators import login_required
from admin_panel.decorators import *
from company_panel.models import Balance, Invoice
from django.core.paginator import Paginator
from django.views.generic import ListView

def newsPageView(request):
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = 'anon'


    New = News.objects.order_by('-pk')

    class NewsList(ListView):
        paginate_by = 4
        model = New

    context = {
        'username': username,
        'New': New,

    }
    return render(request, 'front/news.html',context=context)

def newsItemPageView(request, news_id):
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = 'anon'

    new = get_object_or_404(News, pk=news_id)
    context = {
        'username': username,
        'new': new,
    }
    return render(request, 'front/news-item.html',context=context)