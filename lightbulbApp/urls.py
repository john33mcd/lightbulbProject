from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='PostList'),
    path('<slug:slug>/', views.Comments.as_view(), name='comments'),
]