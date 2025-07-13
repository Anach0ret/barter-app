from django.urls import path, include


urlpatterns = [
    path('ads/', include('ads.api_urls')),
    path('dashboard/', include('dashboard.api_urls')),
]

