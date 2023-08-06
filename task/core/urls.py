from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from .forms import LoginForm

app_name= 'core'

urlpatterns =[
    path('new/',views.new, name='new'),
    path('members/', views.member, name='member'),
    path('store/', views.storage, name='store'),
    path('patrons/', views.patrons, name='patrons'),
    path('index/', views.index, name='index'),
    path('', auth_views.LoginView.as_view(template_name="core/login.html",authentication_form=LoginForm), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]