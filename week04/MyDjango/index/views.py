from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Name
from django.conf.urls.static import static
# Create your views here.


def index(request):

    # return HttpResponse("你好!")
    return render(request, 'index.html', context={ "content": '你好'})


def year(request, year):
    return redirect('/2020.html')
    # return HttpResponse(year)


def name(request, **kwargs):
    return HttpResponse(kwargs['name'])


def myyear(request, **kwargs):
    return render(request, 'yearview.html')

def add_books(request):
    n = Name.objects.create(name='封神演义',  author='刘', stars='9.2')
    return HttpResponse(n.id)

def books(request):
    n = Name.objects.all()
    return render(request, 'books_list.html', locals())