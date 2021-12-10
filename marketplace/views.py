from django.core.checks import messages
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

from .forms import NftForm, CollectionForm, CreatorForm, ProfileForm, SingupForm, UserForm
from .models import Collection, NFT, Creator, Profile

# Create your views here.
    # index
def index(request):
    collections = Collection.objects.all()
    
    nfts = NFT.objects.all()
    nft_count = nfts.count()
    
    latest_nfts = NFT.objects.order_by('-created')
    
    profiles = Profile.objects.all()
    
    context = {'collections': collections,
               'nfts': nfts,
               'nft_count': nft_count,
               'latest_nfts': latest_nfts,
               'profiles': profiles}
    return render(request, 'index.html', context)
 
    # collection
def collection(request, collection_pk):
    collection = Collection.objects.get(collection_name=collection_pk)
    nfts = collection.nfts.all()
    context = {'collection': collection, 'nft': nfts}
    return render(request, 'collection/collection.html', context)
    
    # nft
def nft(request, nft_pk, collection_pk):
    nft = NFT.objects.get(nft_id=nft_pk)
    collection = Collection.objects.get(collection_name = collection_pk)
    context = {'nft': nft, 'collection': collection}
    return render(request, 'nft/nft.html', context)

#Add Methods
@login_required(login_url='login')
def addNft(request):
    form = NftForm()
    
    if request.method == 'POST':
       form = NftForm(request.POST, request.FILES)
       if form.is_valid():
           form.save()
           return redirect('index')
        
    context = {'form': form}
    return render(request, 'forms/add_form.html', context)

@login_required(login_url='login')
def addCollection(request):
    form = CollectionForm()
    
    if request.method == 'POST':
       form = CollectionForm(request.POST, request.FILES)
       if form.is_valid():
           form.save()
           return redirect('index')
        
    context = {'form': form}
    return render(request, 'forms/add_form.html', context)

@login_required(login_url='login')
def addCreator(request):
    form = CreatorForm()
    
    if request.method == 'POST':
       form = CreatorForm(request.POST, request.FILES)
       if form.is_valid():
           form.save()
           return redirect('index')
        
    context = {'form': form}
    return render(request, 'forms/add_form.html', context)

#Update Methods
@login_required(login_url='login')
def updateNft(request, pk):
    nft = NFT.objects.get(id=pk)
    form = NftForm(instance=nft)
    
    # if request.user != nft.user:
    #    return HttpResponse('You do not have permission')
    
    if request.method == 'POST':
        form = NftForm(request.POST, request.FILES, instance=nft)
        if form.is_valid():
           form.save()
           return redirect('index')
    
    context = {'form': form}
    return render(request, 'forms/update_form.html', context)

@login_required(login_url='login')
def updateCollection(request, pk):
    collection = Collection.objects.get(id=pk)
    form = CollectionForm(instance=collection)
    
    # if request.user != collection.user:
    #    return HttpResponse('You do not have permission')
    
    if request.method == 'POST':
        form = CollectionForm(request.POST, request.FILES, instance=collection)
        if form.is_valid():
           form.save()
           return redirect('index')
    
    context = {'form': form}
    return render(request, 'forms/update_form.html', context)

@login_required(login_url='login')
def updateCreator(request, pk):
    creator = Creator.objects.get(id=pk)
    form = CreatorForm(instance=creator)
    
    # if request.user != creator.user:
    #    return HttpResponse('You do not have permission')
    
    if request.method == 'POST':
        form = CreatorForm(request.POST, request.FILES, instance=creator)
        if form.is_valid():
           form.save()
           return redirect('index')
    
    context = {'form': form}
    return render(request, 'forms/update_form.html', context)

@login_required(login_url='login')
def updateUser(request):
    
    if request.method == 'POST':
        u_form = UserForm(request.POST, instance=request.user)
        p_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
           u_form.save()
           p_form.save()
           return redirect('index')
    else:
        u_form = UserForm(instance=request.user)
        p_form = ProfileForm(instance=request.user.profile)
    context = {'u_form': u_form,
               'p_form': p_form}
    return render(request, 'update-user.html', context)
    
#Delete Methods
@login_required(login_url='login')
def deleteNft(request, pk):
    nft = NFT.objects.get(id=pk)
    
    # if request.user != nft.user:
    #    return HttpResponse('You do not have permission')
    
    if request.method == 'POST':
       nft.delete()
       return redirect('index')
    return render(request, 'forms/delete.html', {'obj':nft})

@login_required(login_url='login')
def deleteCollection(request, pk):
    collection = Collection.objects.get(id=pk)
    
    # if request.user != collection.user:
    #    return HttpResponse('You do not have permission')
    
    if request.method == 'POST':
       collection.delete()
       return redirect('index')
    return render(request, 'forms/delete.html', {'obj':collection})

@login_required(login_url='login')
def deleteCreator(request, pk):
    creator = Creator.objects.get(id=pk)
    
    # if request.user != creator.user:
    #    return HttpResponse('You do not have permission')
    
    if request.method == 'POST':
       creator.delete()
       return redirect('index')
    return render(request, 'forms/delete.html', {'obj':creator})




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

# Login Page
def loginPage(request):
    page = 'login'
    
    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        passwd = request.POST.get('password')
        
        try:
            user= User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')
        
        user = authenticate(request, username=username, password=passwd)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successfully.')
            return redirect('index')
        else:
            messages.error(request, 'Username OR password does not exist')

        
    context = {'page':page}
    return render(request, 'login_singup.html', context)

# Logout
def logoutUser(request):
    messages.success(request, 'Logout successfully.')
    logout(request)
    return redirect('index')

def singupPage(request):
    form = SingupForm()
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Some error occurred during registration.')
    
    context = {'form':form}
    return render(request, 'login_singup.html', context)

# Wallet Page
def walletPage(request):
    return render(request, 'wallet.html')

#Coming Soon View
def comingSoon(request):
    return render(request, 'comingsoon.html')
    



    