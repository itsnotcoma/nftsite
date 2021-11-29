from django.contrib import admin
from django.db.models import fields
from .models import Collection, NFT, Creator

# Register your models here.

# admin.site.register(Collection)
# admin.site.register(NFT)
admin.site.register(Creator)

class NFTInline(admin.TabularInline):
    model = NFT

class CreatorInline(admin.TabularInline):
    model = Creator

@admin.register(NFT)
class NFTAdmin(admin.ModelAdmin):
    list_display = ('nft_name', 'nft_id', 'nft_standard', 'nft_blockchain', 'collection_name', 'get_creators')
    fields = ['nft_id', 'nft_name', 'nft_standard', 'nft_blockchain', 'collection_name', 'get_creators']

    def get_creators(self, obj):
        return "\n".join([c.creator_nickname for c in obj.creators.all()])
    
@admin.register(Collection)
class CollectionAmdmin(admin.ModelAdmin):
    list_display = ('collection_name', 'get_nfts')
    fields = ['collection_name', 'get_nfts']
    inlines = [NFTInline]
    
    def get_nfts(self, obj):
        return "\n".join([n.nft_contract_addr for n in obj.nfts.all()])

