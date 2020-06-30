from django.shortcuts import render


# Create your views here.
def sandboxView(request):
    context = {
        'name': 'Dias',
    }
    return render(request, 'sandbox/index.html', context=context)
