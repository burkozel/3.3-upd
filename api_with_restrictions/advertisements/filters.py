from django_filters import rest_framework as filters
from advertisements.models import Advertisement
from advertisements.models import AdvertisementStatusChoices


class AdvertisementFilter(filters.FilterSet):
    status = filters.ChoiceFilter(choices=AdvertisementStatusChoices.choices)
    created_at = filters.DateFromToRangeFilter()
    creator = filters.NumberFilter()

    class Meta:
        model = Advertisement
        fields = ("status", "created_at", "creator")

        #C:\Users\Irasp\PycharmProjects\3.3-main\api_with_restrictions