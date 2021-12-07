from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.db.models import Q
from .forms import NftForm, CollectionForm, Creator

from .models import Collection, NFT, Creator

# Create your views here.
    # index
def index(request):

    nfts = NFT.objects.all()
    collections = Collection.objects.all()
    nft_count = nfts.count()
    
    context = {'collections': collections,
               'nfts': nfts,
               'nft_count': nft_count}
    return render(request, 'index.html', context)
 
    # collection
def collection(request, collection_pk):
    collection = Collection.objects.get(collection_name=collection_pk)
    nfts = Collection.objects.all()
    context = {'collection': collection, 'nft': nfts}
    return render(request, 'collection/collection.html', context)
    
    # nft
def nft(request, nft_pk, collection_pk):
    nft = NFT.objects.get(nft_id=nft_pk)
    collection = Collection.objects.get(collection_name = collection_pk)
    context = {'nft': nft, 'collection': collection}
    return render(request, 'nft/nft.html', context)

        #añadir nft
def addNft(request):
    form = NftForm()
    if request.method == 'POST':
       form = NftForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect('index')
        
    context = {'form': form}
    return render(request, 'nft/nft_form.html', context)

        #actualizar nft
def updateNft(request, pk):
    nft = NFT.objects.get(id=pk)
    form = NftForm(instance=nft)
    if request.method == 'POST':
        form = NftForm(request.POST, instance=nft)
        if form.is_valid():
           form.save()
           return redirect('index')
    
    context = {'form': form}
    return render(request, 'nft/nft_form.html', context)

       #eliminiar nft
def deleteNft(request, pk):
    nft = NFT.objects.get(id=pk)
    if request.method == 'POST':
       nft.delete()
       return redirect('index')
    return render(request, 'forms/delete.html', {'obj':nft})


# Search
def search(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    
    collections_filter = Collection.objects.filter(Q(collection_name__icontains=q))
    nfts_filter = NFT.objects.filter(
        Q(nft_name__icontains=q) |
        Q(nft_id__icontains=q) |
        Q(nft_blockchain__icontains=q)  |
        Q(nft_standard__icontains=q) |
        Q(nft_contract_addr__icontains=q)
    )
    creator_filter = Creator.objects.filter(Q(creator_nickname__icontains=q))
    
    context = {'collections_filter': collections_filter,
               'nfts_filter':nfts_filter,
               'creator_filter':creator_filter,
               'q':q}
    return render(request, 'search.html', context)   
 
#Coming Soon View
def comingSoon(request):
    
    return render(request, 'comingsoon.html')
    



    