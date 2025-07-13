from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),         # для главной страницы
    path('ads/', include('ads.urls')),         # доска объявлений
    path('accounts/', include('accounts.urls')),  # для регистрации и логина
    path('dashboard/', include('dashboard.urls')),  # для кабинета пользователя

    path('api/', include('barter_platform.api_urls')) # для API
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
