# creat your views here.


# from django.http import HttpResponse
from django.shortcuts import render


# def karibu(request):
#     return HttpResponse("<h1>karibu to Django</h1>")


def index(request):
    return render(request, "index.html")



def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')
def gallery(request):
    return render(request,'gallery.html')
