from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def inicial(request):
    return render(request, 'index.html')


def core(request):
    return HttpResponse('Core')