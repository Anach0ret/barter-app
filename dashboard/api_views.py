from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

from ads import models, serializers
from . import permissions


class CreateAdAPIView(generics.CreateAPIView):
    queryset = models.Ad.objects.all()
    serializer_class = serializers.AdSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UpdateAdAPIView(generics.RetrieveUpdateAPIView):
    queryset = models.Ad.objects.all()
    serializer_class = serializers.AdSerializer
    lookup_field = "slug"
    permission_classes = [IsAuthenticated, permissions.IsOwner]



class DeleteAdAPIView(generics.DestroyAPIView):
    queryset = models.Ad.objects.all()
    lookup_field = "slug"
    permission_classes = [IsAuthenticated, permissions.IsOwner]
