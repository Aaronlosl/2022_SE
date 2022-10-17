from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from urllib3 import Retry
from postapp.models import MyPost
from django.contrib.auth.models import User
# Create your views here.
def echo(request):
    content={}
    if request.method == 'GET':
        l=len(request.GET)
        print("len of get = ",l)
        content['requestmethod']='GET'
        for i in request.GET.keys():
            content[i]=request.GET[i]
        print(content)
    if request.method == 'POST':
        l=len(request.POST)
        print("len of post = ",l)
        content['requestmethod']='POST'
        for i in request.POST.keys():
            content[i]=request.POST[i]
        print(content)
    rep=JsonResponse(content)
    rep.set_cookie("auth",'echo')
    return rep

def auth(request):
    content={}
    if request.method == 'POST':
        if ('username' in request.POST) and ('password' in request.POST):
            if len(User.objects.filter(username=request.POST['username'])) != 1:
                rep=JsonResponse({'message':'name not found'})
                return rep
            if not User.objects.filter(username=request.POST['username'])[0].check_password(request.POST['password']):
                rep=JsonResponse({'message':'wrong password'})
                return rep
            rep=JsonResponse({'message':'ok! cookie has been set!'})
            rep.set_cookie('login_status',request.POST['username'])
            return rep
        rep=JsonResponse({'message':'no username or password in post'})
        return rep
    rep=JsonResponse({'message':'not post request'})
    return rep

def home(request):
    content=[]
    if 'login_status' in request.COOKIES:
        for obj in MyPost.objects.all():
            obj_content={}
            obj_content['title']=obj.title
            obj_content['content']=obj.content
            obj_content['author']=obj.author.username
            obj_content['date_posted']=obj.date_posted
            obj_content['summary']=obj.content[0:20]
            content.append(obj_content)
        rep=JsonResponse({"status":1,"content":content})
        rep.delete_cookie('login_status')
        return rep
    rep=JsonResponse({"status":0,"content":content})
    return rep

def index(request):
    return render(request,'jsonresponse/index.html')


    

