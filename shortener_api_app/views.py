from django.http import HttpResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UrlShortSerializers
from .models import req_URLS
from datetime import datetime
import pyshorteners as pys


class URLS_list(APIView):

    def get(self, request):
        url_data_obj = req_URLS.objects.all().order_by('-url_hit')
        serializer = UrlShortSerializers(url_data_obj, many=True)
        return Response(serializer.data)

    def post(self, request):
        try:
            url = request.data.get("url")
        except Exception:
            return Response({"info":"please provide url in key:value pair"}, status.HTTP_404_NOT_FOUND)
        s_url = {}
        obj = req_URLS.objects.values_list('url', flat=True)
        if url in obj:
            t = req_URLS.objects.get(url=url)
            t.url_hit += 1
            t.posting_date=datetime.now()
            t.save()
            return Response(req_URLS.objects.filter(url=url).values('url','short_url','url_hit'), status.HTTP_200_OK)
        else:
            s = pys.Shortener()
            short = s.tinyurl.short(url)
            s_url["url"] = url
            s_url["short_url"] = short
            s_url["url_hit"] = 1
            req_URLS.objects.create(url=url, short_url=short, url_hit=1, posting_date=datetime.now())
        return Response([s_url], status.HTTP_200_OK)