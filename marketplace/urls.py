from django.urls import path
from .views import comingSoon, index
from . import views

urlpatterns = [
   path('', index, name='index'),
   path('search/', views.search, name="search"),
   path('collection/<str:collection_pk>/', views.collection, name="collection"),
   path('collection/<str:collection_pk>/nft/<str:nft_pk>/', views.nft, name="nft"),
   path('add-nft/', views.addNft, name="add-nft"),
   path('update-nft<str:pk>/', views.updateNft, name="update-nft"),
   path('delete-nft<str:pk>/', views.deleteNft, name="delete-nft"),
   #path('', comingSoon, name='coomingsoon'),
]