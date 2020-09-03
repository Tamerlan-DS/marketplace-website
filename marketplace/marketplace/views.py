from django.shortcuts import render
from django.http import HttpResponse


def error_400_view(request, exception=None):
    # return render(request, 'link to html',)
    return HttpResponse('Ваш запрос некоректен или еще что то', status=400)


def error_403_view(request, exception=None):
    # return render(request, 'link to html',)
    return HttpResponse('У вас не хватает власти. Попросоите высшего дать вам больше власти ', status=403)


def error_404_view(request, exception=None):
    # return render(request, 'link to html',)
    return HttpResponse('Вы ищите то чего нет', status=404)


def error_500_view(request, exception=None):
    # return render(request, 'link to html',)
    return HttpResponse('Какая та ошибка на сервере(', status=500)
