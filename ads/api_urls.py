from django.urls import path
from . import api_views


urlpatterns = [
    path('', api_views.AdListAPIView.as_view(), name='api_ads_list'),
    path("<slug:slug>/", api_views.AdDetailAPIView.as_view(), name="api_ad_detail"),
]