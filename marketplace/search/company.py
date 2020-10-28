from company.models import Company
import re
from operator import or_
from functools import reduce
from django.db.models import Q, F

search_fields = [
    'info__id',
    'info__name',
    'info__description',
    'info__short_description',
    'info__search_info',
]


def search_company(
        search_text=None,
        categories=None,
        properties=None,
        city=None,
        region=None,
):
    qs = Company.objects.filter(status='ACCEPTED').select_related(
        'info',
    ).prefetch_related(
        'categories',
    ).all()

    if categories:
        qs = qs.filter(categories__category__in=categories)
    if properties:
        qs = qs.filter(categories__properties__in=properties)
    if city:
        qs = qs.filter(info__city=city)
    if region:
        qs = qs.filter(info__region=region)

    if search_text:
        words = re.sub("[^\w]", "", search_text).split()
        q = Q()
        for search_field in search_fields:
            for word in words:
                q |= Q(**{f'{search_field}__contains': word.lower()})
        qs = qs.filter(q)

    return qs
