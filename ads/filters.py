import django_filters
from .models import Ad
from django.db.models import Q


class AdFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method="filter_search")

    class Meta:
        model = Ad
        fields = ['category', 'condition']

    def filter_search(self, queryset, name, value):
        return queryset.filter(
            Q(title__icontains=value) | Q(description__icontains=value)
        )