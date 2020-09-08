from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from admin_panel.decorators import *
from company_panel.models import Invoice


@login_required
@user_is_moder
def adminPanelView(request):
    history = Invoice.objects.all().order_by('-date')
    context = {
        'history': history,
    }
    return render(request, 'admin_panel/index.html', context=context)
