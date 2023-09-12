from django.contrib import admin
from django.urls import include, path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.main),
    path('myhome/<int:user_id>/', views.myhome),
    path('profile/<int:user_id>/', views.profile),
    path('password/<int:user_id>/', views.password),
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('post/', include('post.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
