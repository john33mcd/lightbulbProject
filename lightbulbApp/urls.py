from django.urls import path
from . import views
from .views import myLoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', myLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('', views.PostList.as_view(), name='PostList'),
    path('<slug:slug>/', views.Comments.as_view(), name='comments'),
]
