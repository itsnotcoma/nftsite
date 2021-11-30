from django.contrib import admin
from django.db.models import fields
from .models import Collection, NFT, Creator

# Register your models here.

# admin.site.register(Collection)
# admin.site.register(NFT)
admin.site.register(Creator)

class NFTInline(admin.TabularInline):
    model = NFT

@admin.register(NFT)
class NFTAdmin(admin.ModelAdmin):
    list_display = ('nft_contract_addr','nft_name', 'nft_id', 'nft_standard', 'nft_blockchain', 'collection_name', 'creator')
    #fields = ['nft_id', 'nft_name', 'nft_standard', 'nft_blockchain', 'collection_name', 'get_creators']
    #inlines = (CreatorInline,)
    list_filter = ['creator', 'nft_standard', 'nft_blockchain']
    
@admin.register(Collection)
class CollectionAmdmin(admin.ModelAdmin):
    list_display = ('collection_name', 'get_nfts')
    #fields = ('collection_name', 'get_nfts')
    inlines = (NFTInline,)

