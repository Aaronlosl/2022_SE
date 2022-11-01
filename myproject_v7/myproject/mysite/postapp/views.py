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
from .models import MyPost
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
            'err_message':"密码不正确!"
        })
        return HttpResponse("密码不正确")


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
            'err_message':"您输入的用户名已存在！"
        })
    if len(username)>0 and len(password)>0 and len(email)>0:
        user = User.objects.create_user(username, email, password)
        user.save()
        #return HttpResponse("注册成功！")
        return home(request)
    return render(request, "postapp/register.html",context={
            'err_message':"信息填写不全，注册失败！"
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