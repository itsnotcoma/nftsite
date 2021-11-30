from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView

from .models import Collection, NFT, Creator

# Create your views here.
def index(request):
    num_collections = Collection.objects.all().count()
    visitas = request.session.get('visitas', 0)
    request.session['visitas']=visitas+1
    return render(request, 'index.html', 
                        context={
                            'numero de colecciones: ': num_collections, 
                            'Visitas:': visitas  
                        },
    )
    
#Coming Soon View
def comingSoon(request):
    
    return render(request, 'comingsoon.html')
    



    