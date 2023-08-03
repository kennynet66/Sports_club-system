from django.contrib.auth import views as auth_views
from django.urls import path
from .views import index
from .forms import LoginForm

app_name= 'core'

urlpatterns =[
    path('index/', index, name='index'),
    path('', auth_views.LoginView.as_view(template_name="core/login.html",authentication_form=LoginForm), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]