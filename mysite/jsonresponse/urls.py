from django.urls import path
from . import views

app_name = 'jsonresponse'
urlpatterns = [
    # path('', views.home, name='post-home'),
    path('echo/',views.echo,name='echo'),
    path('index/',views.index,name='index'),
    path('auth/',views.auth,name='auth'),
    path('home/',views.home,name='home'),
    path('post/',views.receive_post,name='post'),

    path('addFriends/',views.add_friends,name='addFriends'),
    path('showFriends/',views.show_friends,name='showFriends'),
    path('changeAvatar/', views.change_avatar, name='changeAvatar'),
    path('showAvatar/', views.show_avatar, name='showAvatar')
]