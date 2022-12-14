from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import MyPost, UserInfo
from .mysearch import search_strategy
from django.contrib.auth.models import User
# Create your views here.

# define a homepage
def home(request):
    context = {
        'posts':MyPost.objects.all()
    }
    return render(request, 'postapp/home.html', context)

# our post list
class PostListView(ListView):
    model = MyPost
    template_name = 'postapp/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = MyPost
    template_name = 'postapp/post_detail.html'

class PostCreateView(LoginRequiredMixin,CreateView):
    model = MyPost
    fields = ['title', 'content']
    success_url = '../'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = MyPost
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def PostDeleteView(request, pk):
    status = request.COOKIES.get('user')
    post = MyPost.objects.get(pk=pk)
    if(status != post.author.username):
        print("not the author of this post")
        return render(request, 'postapp/home.html')# not the author of this post
    post.delete()
    return home(request)




def signin(request):
    return render(request, 'postapp/login.html')

def signinAction(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        
        # set cookie
        context = {
        'posts':MyPost.objects.all()
        }
        rep=render(request, 'postapp/home.html', context)
        rep.set_cookie("user",username)
        return rep


        return home(request)
    else:
        return render(request, 'postapp/login.html',context={
            'err_message':"???????????????!"
        })
        return HttpResponse("???????????????")


def logoutAction(request):
    logout(request)

    # delete cookie
    rep=render(request, "postapp/login.html")
    rep.delete_cookie("user")
    return rep

    return render(request, "postapp/login.html")


def register(request):
    return render(request, "postapp/register.html")


def registerAction(request):
    username = request.POST['username']
    password = request.POST['password']
    email = request.POST['email']
    person = User.objects.filter(username=username)
    if any(person):
        return render(request, "postapp/register.html",context={
            'err_message':"?????????????????????????????????"
        })
    if len(username)>0 and len(password)>0 and len(email)>0:
        user = User.objects.create_user(username, email, password)
        user.save()
        #return HttpResponse("???????????????")
        return home(request)
    return render(request, "postapp/register.html",context={
            'err_message':"????????????????????????????????????"
        })




def SearchMyPost(request):
    obj_titles, obj_pk, obj_set = [], [], []
    for obj in MyPost.objects.all():
        obj_titles.append(obj.title)
        obj_pk.append(obj.pk)
    pk_list = search_strategy(request.POST['search-content'], obj_titles, obj_pk)
    for pk in pk_list:
        obj_set.append(MyPost.objects.get(pk=pk))

    context = {
        'posts':obj_set
    }
    return render(request, 'postapp/home.html', context)


def update_user_info_view(request):
    username = request.COOKIES.get("user")
    return render(request, "postapp/update_userinfo.html",{'author': username})


def update_user_info(request):
    username = request.COOKIES.get("user")
    userinfo = UserInfo.objects.filter(author=username)
    if len(userinfo) == 0:
        userinfo = UserInfo(author=username)
    else:
        userinfo = userinfo[0]
    userinfo.identity = request.POST["identity"]
    userinfo.info = request.POST["info"]
    userinfo.optical_contact_info = request.POST["optical_contact_info"]
    userinfo.save()
    context = {
        'author': userinfo.author,
        'identity': userinfo.identity,
        'info': userinfo.info,
        'optical_contact_info': userinfo.optical_contact_info
    }
    return render(request, 'postapp/userinfo.html', context)


def get_user_info(request):
    username = request.COOKIES.get("user")
    userinfo = UserInfo.objects.filter(author=username)
    if len(userinfo) > 0:
        userinfo = userinfo[0]
        context = {
            'author': userinfo.author,
            'identity': userinfo.identity,
            'info': userinfo.info,
            'optical_contact_info': userinfo.optical_contact_info
        }
    else:
        context = {
            'author': username,
            'identity': 'to be filled in',
            'info': 'to be filled in',
            'optical_contact_info': 'to be filled in'
        }
    return render(request, 'postapp/userinfo.html', context)