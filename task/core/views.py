from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Sports_details, Patron

def login(request):
    return render(request, 'core/login.html')

def index(request):
    sports = Sports_details.objects.all()
    return render(request, 'core/index.html',{
        "sports" : sports,
    })

@login_required
def patrons(request):
    leader = Patron.objects.all()
    return render(request, 'core/patron.html',{
        'leader' : leader
    })
