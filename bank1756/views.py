from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def petcare(request):
    return render(request, 'petcare.html')
