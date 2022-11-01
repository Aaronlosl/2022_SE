from django.urls import path
from . import views

app_name = 'jsonresponse'
urlpatterns = [
    # path('', views.home, name='post-home'),
    path('echo/',views.echo,name='echo'),
    path('index/',views.index,name='index'),
    path('auth/',views.auth,name='auth'),
    path('home/',views.home,name='home')
]