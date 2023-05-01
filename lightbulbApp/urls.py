from django.urls import path
from . import views
from .views import MyLoginView, CreateTask, Comments, PostList
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', PostList.as_view(), name='index'),
    path('login/', MyLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('create-task/', CreateTask.as_view(), name='create-task'),
    path('<slug:slug>/', Comments.as_view(), name='comments'),
]
