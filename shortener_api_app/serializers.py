from rest_framework import serializers
from .models import req_URLS

class UrlShortSerializers(serializers.ModelSerializer):
    class Meta:
        model = req_URLS
        fields = ('url', 'short_url', 'url_hit')