from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {
        'title': 'Магазин Мир Печей - Главная',
        'content': 'Магазин Мир Печей'
    }
    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'Магазин Мир Печей - О нас',
        'content': 'О нас',
        'text_on_page': 'В этом магазине устанавливают и продают печи камины'
    }
    return render(request, 'main/about.html', context)
