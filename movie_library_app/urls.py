from django.contrib import admin
from . import views
from django.urls import path,include

urlpatterns = [
    path('home',views.index,name='home'),
    path('MyFavorites',views.myfav,name='myfav'),
    path('PublicFavorites',views.publicfav,name='publicfav'),
    path('api/createfavoritelist',views.create_favorite_list,name="create"),
    path('api/getfavoritelist',views.get_favorite_list_details,name="getdetails"),
    path('api/addtofavorites',views.add_to_favorite,name="getdetails"),
    path('api/openlist',views.open_favlist,name="openlist"),
    path('Public/<str:username>/<str:name>',views.public_list,name="Public"),
    path('Private/<str:username>/<str:name>',views.private_list,name="Private")


]
