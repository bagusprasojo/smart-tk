from django.urls import path

from .views import UserCreateView, UserListView, UserLoginView, logout_view

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('users/', UserListView.as_view(), name='user_list'),
    path('users/add/', UserCreateView.as_view(), name='user_add'),
]
