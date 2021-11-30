from django.urls import path
from .views import comingSoon, index

urlpatterns = [
   #path('', index, name='index'),
   path('', comingSoon, name='coomingsoon'),
]