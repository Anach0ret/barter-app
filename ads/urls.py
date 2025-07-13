from django.urls import path
from . import views


urlpatterns = [
    path('', views.AdsView.as_view(), name='ads'),
    path('<slug:slug>/', views.AdDetailView.as_view(), name='ad_detail'),
    path('barter/<slug:slug>/', views.BarterRequestView.as_view(), name='barter_request'),
]