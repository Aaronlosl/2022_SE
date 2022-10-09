from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import User
from django.template import loader

def index(request):
    template = loader.get_template('login/index.html')
    return HttpResponse(template.render({}, request))

def userlog(request, user_id):
    #response = "You're looking at the results of question %s."
    #return HttpResponse(response % user_id)
    try:
        user = get_object_or_404(User, pk=user_id)
    except:
        user = User(user_name='root', password='root', email='root@pku.edu.cn')
        user.save()
    return render(request, 'login/login.html', {'user':user})


def result(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    try:
        #User.objects.filter(user_name=request.POST['username']).delete()
        login_user = User.objects.get(user_name=request.POST['username'])
    except (KeyError, User.DoesNotExist):
        login_user = User(user_name=request.POST['username'], password=request.POST['password'], email=request.POST['email'])
        if len(login_user.user_name) > 0 and len(login_user.password) > 0 and len(login_user.email) > 0:
            response = "您已注册1个新的用户."
            login_user.save()
            return HttpResponse(response)
        else:
            response = "您的用户名/密码/邮箱信息未被填写."
            return HttpResponse(response)

    if login_user.password == request.POST['password']:
        response = "您已登录了用户:%s."
        return HttpResponse(response % request.POST['username'])
    else:
        response = "用户密码出现错误."
        return HttpResponse(response)
    #response = "You're looking at the results of question %s."
    #return HttpResponse(response % user_id)
    #user = get_object_or_404(User, pk=user_id)
    #return render(request, 'login/result.html', {})
