from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name='index'),
   #path('', views.comingSoon, name='comingsoon'),
   
   path('search/', views.search, name="search"),
   
   path('login/', views.loginPage, name="login"),
   path('logout/', views.logoutUser, name="logout"),
   path('singup/', views.singupPage, name="singup"),
   
   path('collection/<str:collection_pk>/', views.collection, name="collection"),
   path('collection/<str:collection_pk>/nft/<str:nft_pk>/', views.nft, name="nft"),
   
   path('add/nft/', views.addNft, name="add-nft"),
   path('add/collection/', views.addCollection, name="add-collection"),
   path('add/creator/', views.addCreator, name="add-creator"),

   
   path('update/nft/<str:pk>/', views.updateNft, name="update-nft"),
   path('update/collection/<str:pk>/', views.updateCollection, name="update-collection"),
   path('update/creator/<str:pk>/', views.updateCreator, name="update-creator"),
   
   path('delete/nft/<str:pk>/', views.deleteNft, name="delete-nft"),
   path('delete/collection/<str:pk>/', views.deleteCollection, name="delete-collection"),
   path('delete/creator/<str:pk>/', views.deleteCreator, name="delete-creator"),
]