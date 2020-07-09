from django.shortcuts import render


# Create your views here.
def sandboxView(request):
    context = {
        'name': 's',
        '123': 'asd'
    }
    return render(request, 'sandbox/index.html', context=context)
