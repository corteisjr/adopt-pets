from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include

urlpatterns = (
    [
        path("admin/", admin.site.urls),
        path("auth/", include("accounts.urls.authUrls")),
        path("divulge/", include("divulge.urls.divulgeUrls")),
    ]
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)
