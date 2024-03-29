from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup),
    path('signin/', views.signin),
    path('signout/', views.signout),
    path('follow/<int:user_id>/', views.follow),
]
