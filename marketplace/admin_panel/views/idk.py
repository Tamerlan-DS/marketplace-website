from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def adminPanelView(request):
    context = {
    }
    return render(request, 'admin_panel/index.html', context=context)
