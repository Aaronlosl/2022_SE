from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from urllib3 import Retry
from postapp.models import MyPost, Friend, UserInfo, AdvancedPost
from django.contrib.auth.models import User
from django.db.models import Q
from PIL import Image
from pathlib import Path
import json, os
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
        # formal ver
        dic=json.loads(request.body)
        # use json/index to test
        # dic = request.POST
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
    PG_SIZE = 4 # page size
    content=[]
    if 'login_status' in request.COOKIES:
        cnt=0
        id = 0
        page = 1

        _type = "ALL"
        # formal ver
        try:
            dic=json.loads(request.body)
            # use json/index to test
            # dic = request.POST
            if 'post_type' in dic.keys():
                _type = dic['post_type']
            if 'page' in dic.keys():
                if int(dic['page'])>=1:
                    page = int(dic['page'])
        except:
            pass
        if _type=='ALL':
            blogs=MyPost.objects.all().order_by('-date_posted')
        else:
            blogs=MyPost.objects.filter(post_type=_type).order_by('-date_posted')
        for obj in blogs:
            id+=1
            if id>(page-1)*PG_SIZE:
                obj_content={}
                obj_content['title']=obj.title
                obj_content['content']=obj.content
                obj_content['author']=obj.author.username
                obj_content['date_posted']=obj.date_posted
                obj_content['summary']=obj.content[0:20]
                content.append(obj_content)
                cnt+=1
                if cnt>=PG_SIZE:
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
    #print(name)
    if len(User.objects.filter(username=name)) != 1:
        rep=JsonResponse({'status':-1,'message':'name not found'})
        return rep
    dic=json.loads(request.body)
    # if request tells this post have a TYPE
    _type = "ALL"
    if 'post_type' in dic.keys():
        _type = dic['post_type']
    post=MyPost(title=dic["title"],content=dic["content"],author=User.objects.filter(username=name)[0],post_type=_type)
    post.save()
    rep=JsonResponse({'status':1,'message':'post successfully !'})
    # rep.delete_cookie('login_status')
    return rep

def add_friends(request):
    if not 'login_status' in request.COOKIES:
        rep=JsonResponse({"status":0,"message":"sorry but you are not login"})
        return rep
    dic=json.loads(request.body)
    # dic=request.POST
    if ('name1' in dic.keys()) and ('name2' in dic.keys()):
        # confirm these 2 names are valid
        user = User.objects.filter(username=dic['name1'])
        if len(user)==0:
            rep=JsonResponse({"status":-2,"message":"invalid name"})
            return rep
        user = User.objects.filter(username=dic['name2'])
        if len(user)==0:
            rep=JsonResponse({"status":-2,"message":"invalid name"})
            return rep
        # confirm if these two guys are already friends
        name1 = Friend.objects.filter(name1=dic['name1'])
        for name in name1:
            if name.name2 == dic['name2']:
                # found
                rep=JsonResponse({"status":2,"message":"they are already friends !"})
                return rep
        # swap
        name1 = Friend.objects.filter(name2=dic['name1'])
        for name in name1:
            if name.name1 == dic['name2']:
                # found
                rep=JsonResponse({"status":2,"message":"they are already friends !"})
                return rep
        # not found

        friend = Friend(name1=dic['name1'],name2=dic['name2'])
        friend.save()
        rep=JsonResponse({"status":1,"message":"add friends successfully !"})
        return rep
    else:
        rep=JsonResponse({"status":-1,"message":"invalid format"})
        return rep

def show_friends(request):
    if not 'login_status' in request.COOKIES:
        rep=JsonResponse({"status":0,"message":"sorry but you are not login"})
        return rep
    dic=json.loads(request.body)
    # dic=request.POST
    if ('name' in dic.keys()):
        if(dic['name']==' '):
            # user = User.objects.filter(username=request.COOKIES['login_status'])
            dic['name']=request.COOKIES['login_status']
        else:
            user = User.objects.filter(username=dic['name'])
            if len(user)==0:
                # invalid name
                rep=JsonResponse({"status":-2,"message":"invalid name"})
                return rep
        f1 = Friend.objects.filter(name1=dic['name'])
        f2 = Friend.objects.filter(name2=dic['name'])
        f = []
        for i in f1:
            if i.name2!=dic['name']:
                f.append(i.name2)
        for i in f2:
            if i.name1!=dic['name']:
                f.append(i.name1)
        
        rep=JsonResponse({"status":1,"message":"ok","content":f})
        return rep
    else:
        rep=JsonResponse({"status":-1,"message":"invalid format"})
        return rep

def change_avatar(request):
    file = request.FILES.get('avatar', None)
    username = request.POST.get("name")
    userinfo = UserInfo.objects.filter(author=username)
    if len(userinfo) == 0:
        userinfo = UserInfo(author=username)
    else:
        userinfo = userinfo[0]
    username = userinfo.author
    if file:
        # save image
        filename = file.name
        if not os.path.exists(os.path.join(Path(__file__).resolve().parent.parent, "jsonresponse", "static", username)):
            os.mkdir(os.path.join(Path(__file__).resolve().parent.parent, "jsonresponse", "static", username))
        image = Image.open(file)
        if image:
            path = os.path.join(Path(__file__).resolve().parent.parent, "jsonresponse", "static", username, filename)
            image.save(r'%s' % path)
        else:
            rep = JsonResponse({"status":-3, "message":"invalid image"})
            return rep
        # remove
        last = userinfo.avatar
        try:
            os.remove(os.path.join(Path(__file__).resolve().parent.parent, "jsonresponse", "static", username, last))
        except:
            pass
        userinfo.avatar = filename
        userinfo.save()
        return JsonResponse({"status":0, "message":"change success"})
    # else:
        # return JsonResponse({"status":-1, "message":"invalid format"})

def show_avatar(request):
    username = request.POST.get("name")
    userinfo = UserInfo.objects.filter(author=username)
    if len(userinfo) == 0:
        userinfo = UserInfo(author=username)
    else:
        userinfo = userinfo[0]
    username = userinfo.author
    filename = userinfo.avatar
    if not (username and filename):
        return JsonResponse({"status":-1, "message":"invalid format"})
    path = os.path.join(Path(__file__).resolve().parent.parent, "jsonresponse", "static", username, filename)
    image = open(path, "rb").read()
    if image:
        return HttpResponse(image, content_type="image/png")
    else:
        return JsonResponse({"status":-1, "message":"invalid format"})


def mark_ad_post(request):
    dic = json.loads(request.body)

    with open('results.json', 'w') as result_file:
        json.dump(dic, result_file)

    key1, key2, key3 = dic['academy'], dic['institution'], dic['professor']
    starting_date = dic['starting_date']
    try:
        post_set = AdvancedPost.objects.filter(professor__contains=key3)
        for obj in post_set:
            with open('results2.json', 'w') as result_file:
                dic.update({'date':obj.date_posted})
                json.dump(dic, result_file)
            if obj.date_posted >= starting_date:
                obj.post_visible = "YES"
                obj.save()
    except:
        pass
    rep = JsonResponse({"status": 1,"message":"search successfully !"})
    return rep


def show_ad_post(request):
    #dic = json.loads(request.body)
    #key1, key2, key3 = dic['academy'], dic['institution'], dic['professor']
    #starting_date = dic['starting_date']
    #post_set = AdvancedPost.object.filter(Q(academy__contains=key1) | Q(institution__contains=key2) | Q(professor__contains=key3))

    content = []
    try:
        post_set = AdvancedPost.objects.order_by('-date_posted')
        cnt = 0
        for obj in post_set:
            if obj.post_visible == "YES":
                obj_content = {}
                obj_content['title'] = obj.title
                obj_content['content'] = obj.content
                obj_content['author'] = obj.author.username
                obj_content['date_posted'] = obj.date_posted
                obj_content['summary'] = obj.content[0:20]
                content.append(obj_content)
                obj.post_visible = "NO"
                obj.save()
            cnt += 1
            if cnt >= 10:
                break
    except:
        pass
    rep = JsonResponse({"status": 1, "content": content})
    return rep


def receive_ad_post(request):
    if not 'login_status' in request.COOKIES:
        rep=JsonResponse({"status":0,"message":"sorry but you are not login"})
        return rep
    name=request.COOKIES.get('login_status')
    if len(User.objects.filter(username=name)) != 1:
        rep=JsonResponse({'status':-1,'message':'name not found'})
        return rep
    dic=json.loads(request.body)
    post=AdvancedPost(title=dic["title"],content=dic["content"],author=User.objects.filter(username=name)[0],
                      academy=dic['academy'],institution=dic['institution'],professor=dic['professor'])
    post.save()
    rep=JsonResponse({'status':1,'message':'post successfully !'})
    # rep.delete_cookie('login_status')
    return rep