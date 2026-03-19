from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
# from src import settings
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('src.apps.main.urls', namespace='main')),
    path('catalog/', include('src.apps.goods.urls', namespace='catalog')),
]


if settings.DEBUG:
    urlpatterns += [path("__debug__/", include("debug_toolbar.urls"))]
    # urlpatterns += (
    #     path("swagger/", SpectacularAPIView.as_view(), name="schema"),
    #     path("docs", SpectacularSwaggerView.as_view(url_name="schema"), name="docs"),
    # )


    # urlpatterns += tuple(static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)