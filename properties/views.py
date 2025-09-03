from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from .utils import get_all_properties

# Keep view-level caching (15 minutes) + low-level queryset caching (1 hour)
@cache_page(60 * 15)
def property_list(request):
    properties = get_all_properties()
    return JsonResponse({"data": properties})

