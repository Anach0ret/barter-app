from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Barter API",
        default_version='v1',
        description="Документация для Barter платформы",
        contact=openapi.Contact(email="imashak4@gmail.com"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),         # для главной страницы
    path('ads/', include('ads.urls')),         # доска объявлений
    path('accounts/', include('accounts.urls')),  # для регистрации и логина
    path('dashboard/', include('dashboard.urls')),  # для кабинета пользователя

    path('api/', include('barter_platform.api_urls')), # для API

    # Swagger и ReDoc
    path("swagger/", schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path("redoc/", schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
