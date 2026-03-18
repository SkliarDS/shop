from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('src.apps.main.urls', namespace='main')),
    path('catalog/', include('src.apps.goods.urls', namespace='catalog')),
]
