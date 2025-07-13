from django.urls import path
from . import views



urlpatterns = [
    path('', views.MyAdsView.as_view(), name='dashboard'),

    path('barters-box/', views.BartersBoxListView.as_view(), name='barters_box'),
    path("barters-box/status/<int:pk>/", views.BarterStatusUpdateView.as_view(), name="barter_status"),

    path('create-ad/', views.AdCreateView.as_view(), name='create_ad'),
    path('<int:pk>/edit-ad/', views.AdUpdateView.as_view(), name='edit_ad'),
    path('<int:pk>/delete-ad/', views.AdDeleteView.as_view(), name='delete_ad'),

    path('token/', views.token_view, name='token'),
]
