from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from core.views import index

urlpatterns = [
    path('', include('core.urls')),
    path('index/', index, name='index'),
    path('admin/', admin.site.urls),
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)