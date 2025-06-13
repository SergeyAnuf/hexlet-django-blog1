from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    context = {'app_name': 'article'}
    return render(request, 'articles/index.html', context)