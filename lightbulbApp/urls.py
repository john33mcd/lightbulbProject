from django.urls import path
from . import views
from .views import myLoginView

urlpatterns = [
    path('login/', myLoginView.as_view(), name='login'),
    path('', views.PostList.as_view(), name='PostList'),
    path('<slug:slug>/', views.Comments.as_view(), name='comments'),
]