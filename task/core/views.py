from django.shortcuts import render

def login(request):
    return render(request, 'core/login.html')

def index(request):
    return render(request, 'core/index.html')