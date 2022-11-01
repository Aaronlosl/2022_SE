from django.urls import path
from .views import (
    PostListView,
    PostCreateView,
    PostDeleteView,
    PostDetailView,
    PostUpdateView
)
from . import views

app_name = 'postapp'
urlpatterns = [
    path('', views.home, name='post-home'),
    path('<int:pk>/detail/', PostDetailView.as_view(), name='post-detail'),
    path('new/', PostCreateView.as_view(), name='post-create'),
    path('<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('<int:pk>/delete/', PostDeleteView, name='post-delete'),
    path('search/', views.SearchMyPost, name='post-search'),
    path('login/', views.signin),
    path('loginAction/', views.signinAction, name='post-login'),
    path('logoutAction/', views.logoutAction, name='post-logout'),
    path('register/', views.register, name='post-register'),
    path('registerAction/', views.registerAction, name='post-register-action')
]