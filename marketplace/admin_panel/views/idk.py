from django.shortcuts import render


def adminPanelView(request):
    context = {
    }
    return render(request, 'admin_panel/index.html', context=context)
