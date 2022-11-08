from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from urllib3 import Retry
from postapp.models import MyPost
from django.contrib.auth.models import User
import json
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
'''   
def auth(request):
    content={}
    if request.method == 'POST':
        dic=json.loads(request.body)
        if ('username' in request.POST) and ('password' in request.POST):
            if len(User.objects.filter(username=request.POST['username'])) != 1:
                rep=JsonResponse({'status':-1,'message':'name not found'})
                return rep
            if not User.objects.filter(username=request.POST['username'])[0].check_password(request.POST['password']):
                rep=JsonResponse({'status':0,'message':'wrong password'})
                return rep
            rep=JsonResponse({'status':1,'message':'ok! cookie has been set!'})
            rep.set_cookie('login_status',request.POST['username'])
            return rep
        rep=JsonResponse({'status':-2,'message':'no username or password in post'})
        return rep
    rep=JsonResponse({'status':-3,'message':'not post request'})
    return rep
'''
def auth(request):
    content={}
    if request.method == 'POST':
        dic=json.loads(request.body)
        if ('username' in dic.keys()) and ('password' in dic.keys()):
            if len(User.objects.filter(username=dic['username'])) != 1:
                rep=JsonResponse({'status':-1,'message':'name not found'})
                return rep
            if not User.objects.filter(username=dic['username'])[0].check_password(dic['password']):
                rep=JsonResponse({'status':0,'message':'wrong password'})
                rep.delete_cookie('login_status')
                return rep
            rep=JsonResponse({'status':1,'message':'login successflly !'})
            rep.set_cookie('login_status',dic['username'])
            return rep
        rep=JsonResponse({'status':-2,'message':'no username or password in post'})
        return rep
    rep=JsonResponse({'status':-3,'message':'not post request'})
    return rep

def home(request):
    content=[]
    if 'login_status' in request.COOKIES:
        cnt=0
        for obj in MyPost.objects.all().order_by('-date_posted'):
            obj_content={}
            obj_content['title']=obj.title
            obj_content['content']=obj.content
            obj_content['author']=obj.author.username
            obj_content['date_posted']=obj.date_posted
            obj_content['summary']=obj.content[0:20]
            content.append(obj_content)
            cnt+=1
            if cnt>=5:
                break
        rep=JsonResponse({"status":1,"content":content})
        # rep.delete_cookie('login_status')
        return rep
    rep=JsonResponse({"status":0,"content":content})
    return rep

def index(request):
    return render(request,'jsonresponse/index.html')


def receive_post(request):
    if not 'login_status' in request.COOKIES:
        rep=JsonResponse({"status":0,"message":"sorry but you are not login"})
        return rep
    name=request.COOKIES.get('login_status')
    print(name)
    if len(User.objects.filter(username=name)) != 1:
        rep=JsonResponse({'status':-1,'message':'name not found'})
        return rep
    dic=json.loads(request.body)
    post=MyPost(title=dic["title"],content=dic["content"],author=User.objects.filter(username=name)[0])
    post.save()
    rep=JsonResponse({'status':1,'message':'post successfully !'})
    # rep.delete_cookie('login_status')
    return rep

