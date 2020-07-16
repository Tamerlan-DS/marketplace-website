from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from ..models import Card


def employeesView(request):
    cards = Card.objects.all()
    context = {
        'cards': cards,
    }
    return render(request, 'admin_panel/admin-sotrud.html', context=context)


def employeeAddView(request):
    context = {
    }
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        re_password = request.POST['re_password']
        role = request.POST['role']
        context['username'] = username
        context['first_name'] = first_name
        context['last_name'] = last_name
        context['email'] = email
        context['role'] = role
        if password == re_password:
            try:
                user = User.objects.get(username=username)
                context['error'] = 1
                return render(request, 'admin_panel/admin-sotrud-add.html', context=context)
            except User.DoesNotExist:
                user = User.objects.create_user(
                    username=username,
                    password=password,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                )
                user.save()
                card = Card(owner=user)
                if role == 0:
                    card.role = Card.RoleChoices.MODERATOR
                else:
                    card.role = Card.RoleChoices.ADMINISTRATOR
                card.save()
                context['error'] = 0
                return render(request, 'admin_panel/admin-sotrud-add.html', context=context)
        else:
            context['error'] = 2
            return render(request, 'admin_panel/admin-sotrud-add.html', context=context)
    else:
        pass
    return render(request, 'admin_panel/admin-sotrud-add.html', context=context)


def employeeEditView(request, employee_id):
    context = {
    }
    return render(request, 'admin_panel/admin-sotrud-edit.html', context=context)
