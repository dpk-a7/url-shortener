from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', cache_page(5*60)(views.URLS_list.as_view()))
]
