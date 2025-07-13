from rest_framework import serializers
from .models import Ad



class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = [
            'id',
            'title',
            'description',
            'image_url',
            'category',
            'condition',
            'slug',
            'created_at',
        ]
        read_only_fields = ['slug', 'created_at']
