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
    post = MyPost.objects.get(pk=pk)
    post.delete()
    return home(request)


'''
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = MyPost
    success_url = 'postapp/home.html'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
'''


def signin(request):
    return render(request, 'postapp/login.html')

def signinAction(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return home(request)
    else:
        return HttpResponse("密码不正确")


def logoutAction(request):
    logout(request)
    return render(request, "postapp/login.html")


def register(request):
    return render(request, "postapp/register.html")


def registerAction(request):
    username = request.POST['username']
    password = request.POST['password']
    email = request.POST['email']
    person = User.objects.filter(username=username)
    if any(person):
        return HttpResponse("您输入的用户名已存在！")
    if len(username)>0 and len(password)>0 and len(email)>0:
        user = User.objects.create_user(username, email, password)
        user.save()
        #return HttpResponse("注册成功！")
        return home(request)
    return HttpResponse("信息填写不全，注册失败！")


def SearchMyPost(request):
    context = {
        'posts':MyPost.objects.filter(title__contains=request.POST['search-content'])
    }
    return render(request, 'postapp/home.html', context)