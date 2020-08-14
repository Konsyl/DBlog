from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_post_list, name='posts_list'),
    path('create', views.create_post, name='create_post'),
    path('post/<int:post_id>/', views.get_post, name='post_read'),
]