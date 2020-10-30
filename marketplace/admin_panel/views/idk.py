from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from admin_panel.decorators import *
from company.models import Company
from company_panel.models import Invoice
from django.contrib.auth.models import User

@login_required
@user_is_company
def adminPanelView(request):
    history = Invoice.objects.all().order_by('-date')
    user_history = Invoice.objects.filter(balance__owner= request.user)
    print(user_history)
    context = {
        'history': history,
        'user_history': user_history,
    }
    return render(request, 'admin_panel/index.html', context=context)
