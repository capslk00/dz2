from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def index(request):
#     return HttpResponse('Hello world')

def index(request):
    return render(request, 'index.html')

def about(request):
    text = {
        'title': 'ZAGOLOVOK',
        'description': 'Description'
    }
    return render(request, 'about.html', text)
