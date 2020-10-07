from django.shortcuts import render, redirect, get_object_or_404
from company.helper import *
from company.models import Company, Category, CompanyCategory, news
from admin_panel.models import Card
from django.contrib.auth.decorators import login_required
from admin_panel.decorators import *
from company_panel.models import Balance, Invoice
from django.core.paginator import Paginator
from django.views.generic import ListView
from django.core.paginator import Paginator

def newsPageView(request):
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = 'anon'
    New = News.objects.order_by('-pk')
    paginator = Paginator(New,1)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    print(page.paginator.page_range)
    print(page.number)
    is_paginated = page.has_other_pages()
    print(page.number)
    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''

    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

    class NewsList(ListView):
        paginate_by = 4
        model = New

    context = {
        'username': username,
        'News': page,
        'is_paginated': is_paginated,
        'next_url': next_url,
        'prev_url': prev_url,
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