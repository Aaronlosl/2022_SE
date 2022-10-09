from django.urls import path

from . import views

app_name = 'login'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:user_id>/', views.userlog, name='url01'),
    path('<int:user_id>/result/', views.result, name='result')
]
