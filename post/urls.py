from django.urls import path
from . import views


urlpatterns = [
    path('create/', views.create),
    path('<int:post_id>/', views.read),
]