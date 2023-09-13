from django.urls import path
from . import views


urlpatterns = [
    path('create/', views.create),
    path('<int:post_id>/', views.read),
    path('delete/<int:post_id>/', views.delete),
    path('update/<int:post_id>/', views.update),
    path('comment/<int:post_id>/', views.comment),
    path('comment/delete/<int:comment_id>/', views.comment_delete),
]
