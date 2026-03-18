from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        'title': 'Главная страница',
        'content': 'Добро пожаловать на сайт'
    }
    return render(request, 'main/index.html', context)


def about(request):
    return HttpResponse('about page')
