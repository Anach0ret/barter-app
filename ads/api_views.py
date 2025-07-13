from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

from . import models, serializers, filters



class AdListAPIView(generics.ListAPIView):
    queryset = models.Ad.objects.all().order_by("-created_at")
    serializer_class = serializers.AdSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = filters.AdFilter


class AdDetailAPIView(generics.RetrieveAPIView):
    queryset = models.Ad.objects.all()
    serializer_class = serializers.AdSerializer
    lookup_field = "slug"