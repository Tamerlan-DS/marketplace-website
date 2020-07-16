from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate


def loginView(request):
    if request.user.is_authenticated:
        return redirect('panel')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('panel')

    return render(request, 'admin_panel/admin-login.html')


def logoutView(request):
    logout(request)
    return redirect('login')


def forgotPasswordView(request):
    context = {
    }
    return render(request, 'admin_panel/admin-forgot-password.html', context=context)


def resetPasswordView(request):
    context = {
    }
    return render(request, 'admin_panel/admin-reset-password.html', context=context)
