from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
]
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
