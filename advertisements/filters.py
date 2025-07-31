from django_filters import rest_framework as filters
from django import forms
from advertisements.models import Advertisement, AdvertisementStatusChoices


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""
    creator = filters.NumberFilter(field_name='creator__id', label='ID создателя')
    status = filters.ChoiceFilter(
        choices=AdvertisementStatusChoices.choices,
        empty_label='Все статусы',
        label='Фильтр по статусу'
    )

    created_after = filters.DateFilter(
        field_name='created_at',
        lookup_expr='gte',
        label='Создано после',
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    class Meta:
        model = Advertisement
        fields =[]