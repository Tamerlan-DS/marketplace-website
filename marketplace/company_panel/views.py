from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def test(request):
    context = {
    }
    return render(request, 'company_panel/test.html', context=context)
