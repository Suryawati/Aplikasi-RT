from django.contrib import admin
from django.urls import path, include
from django.conf import settings # new
from django.conf.urls.static import static # new

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('articles/', include('articles.urls')),
    path('', include('pages.urls')),
    path('wargas/', include('wargas.urls')),
    path('letters/', include('letters.urls')),
    path('kas/', include('kass.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
