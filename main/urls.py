from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from coursework import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('vitrina/', include('shop.urls')),
    path('account/', include('account.urls')),
    path('main/', include('account.urls')),
    path('main/', include('shop.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)