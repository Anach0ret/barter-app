from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import api_views


urlpatterns = [
    path('create-ad/', api_views.CreateAdAPIView.as_view(), name='api_dashboard_create_ad'),
    path('update-ad/<slug:slug>/', api_views.UpdateAdAPIView.as_view(), name='api_dashboard_update_ad'),
    path('delete-ad/<slug:slug>/', api_views.DeleteAdAPIView.as_view(), name='api_dashboard_delete_ad'),

    path('token/', obtain_auth_token, name='api_token'),
]