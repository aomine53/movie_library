import re
from django.http import request
from django.shortcuts import render
from django.http.response import HttpResponse,JsonResponse
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.contrib.auth.models import User
from .models import *
# Create your views here.

@login_required(login_url="")
def index(request):
    ctx = {}
    arr = []
    fav_list = CreatePlaylist.objects.filter(user=request.user)
    # print(fav_list)
    if len(fav_list) != 0:
        for obj in fav_list:
            list_obj = {}
            list_obj['name'] = obj.name
            if obj.is_private == True:
                list_obj['isprivate'] = "Private"
            else:
                list_obj['isprivate'] = "Public"
            arr.append(list_obj)
    ctx['fav_list'] = arr
    return render(request,'index.html',ctx)

def add_to_favorite(request):
    if request.method == 'POST':
        imdb_id = request.POST.get('imdbid')
        name = request.POST.get('favorite_list_name')
    
    playlist = CreatePlaylist.objects.get(name=name,user=request.user)
    AddToPlaylist.objects.create(playlist=playlist,imdb_id=imdb_id)

    return JsonResponse({'message':"Added to favoritelist Successfully"})


def open_favlist(request):
    get_movie_list = []
    ids = []
    if request.method == 'POST':
        playlist_name = request.POST.get('name')
    
    playlist = CreatePlaylist.objects.get(name=playlist_name,user=request.user)
    get_movie_list = AddToPlaylist.objects.filter(playlist=playlist)
    for g in get_movie_list:
        ids.append(g.imdb_id)
    print(ids)
    return JsonResponse({"movielist":ids})    


def public_list(request,username,name):
    ids = []
    userz = User.objects.get(username=username)
    playlist = CreatePlaylist.objects.get(name=name,user=userz)
    get_movie_list = AddToPlaylist.objects.filter(playlist=playlist)
    for g in get_movie_list:
        ids.append(g.imdb_id)
    print(ids)
    return render(request,'myfav_movielist.html',{'ids':ids,'list_name':name,'created_by':username})
    # return HttpResponse("Hiii"+username+name+str(ids))

def private_list(request,username,name):
    ids = []
    # userz = User.objects.get(username=username)
    playlist = CreatePlaylist.objects.filter(name=name,user=request.user)
    print(len(playlist))
    if(len(playlist) !=0):
        get_movie_list = AddToPlaylist.objects.filter(playlist=playlist[0])
        for g in get_movie_list:
            ids.append(g.imdb_id)
        print(ids)
        return render(request,'myfav_movielist.html',{'ids':ids,'list_name':name,'created_by':username})
    else:
        return HttpResponse("<h1>Access Denied : Private Favorite List</h1>")
def create_favorite_list(request):
    message = ""
    if request.method == 'POST':
        name = request.POST.get('name')
        is_private = request.POST.get('isprivate')
    
    # print(name,is_private)
    if is_private == 'true':
        is_private = True
    else:
        is_private = False
    if(len(CreatePlaylist.objects.filter(name=name)) != 0):
        message = "Favourite List Name Should be Unique"
    else:
        CreatePlaylist.objects.create(name=name,is_private=is_private,user=request.user)
        message = "Favorite List Created Successfully"
    return JsonResponse({'message':message})

def myfav(request):
    
    # print(ctx)
    ctx = {}
    arr = []
    fav_list = CreatePlaylist.objects.filter(user=request.user)
    # print(fav_list)
    if len(fav_list) != 0:
        for obj in fav_list:
            list_obj = {}
            list_obj['name'] = obj.name
            if obj.is_private == True:
                list_obj['isprivate'] = "Private"
            else:
                list_obj['isprivate'] = "Public"
            arr.append(list_obj)
    ctx['fav_list'] = arr
    return render(request,'myfav.html',ctx)

def get_favorite_list_details(request):
    ctx = {}
    arr = []
    fav_list = CreatePlaylist.objects.filter(user=request.user)
    # print(fav_list)
    if len(fav_list) != 0:
        for obj in fav_list:
            list_obj = {}
            list_obj['name'] = obj.name
            if obj.is_private == True:
                list_obj['isprivate'] = "Private"
            else:
                list_obj['isprivate'] = "Public"
            arr.append(list_obj)
    ctx['fav_list'] = arr
    return JsonResponse(ctx)

def publicfav(request):
    public_lists = []
    info_list = []
    ctx = {}
    public_lists = CreatePlaylist.objects.filter(is_private = False)
    if len(public_lists) != 0:
        for li in public_lists:
            info={}
            info['name'] = li.name
            info['created_by'] = li.user.username
            info_list.append(info)
    ctx['public_lists'] = info_list
    return render(request,'publicfav.html',ctx)