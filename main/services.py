from django.conf import settings
from django.core.cache import cache

from main.models import Category


def get_cached_category():
    if settings.CACHED_ENABLED:
        key = 'category_list'
        subject_list = cache.get(key)
        if subject_list is None:
            subject_list = Category.objects
            cache.set(key, subject_list)
    else:
        subject_list = Category.objects
    return subject_list
