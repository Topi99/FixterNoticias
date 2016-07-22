from django.conf.urls import url, include
from django.contrib import admin
from noticias import urls as noticasUrls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^noticias/', include(noticasUrls, namespace="noticas"))
]
