from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('shortener/admin/', admin.site.urls),
    path('shortener/',include('shortener_api_app.urls'))
]
