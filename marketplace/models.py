from django.db import models

# Create your models here.

# Colection Class
class Collection(models.Model):
    collection_name = models.CharField("Colección", max_length=200)
    
    nfts = models.ManyToManyField('NFT', verbose_name='NFT',related_name='nfts')
    
    def __str__(self):
        return self.collection_name
    class Meta:
        verbose_name = 'Colección'
        verbose_name_plural = 'Colecciones'

#NFT Class
class NFT(models.Model):
    nft_contract_addr = models.CharField("Contract Address", max_length=256)
    nft_name = models.CharField("Token Name", max_length=200)
    nft_id = models.CharField("Token Id", max_length=5, blank=True)
    nft_standard = models.CharField("Token Standard", max_length=10)
    nft_blockchain = models.CharField("Blockchain", max_length=100)
    
    collection_name = models.ForeignKey('Collection', on_delete=models.SET_NULL, null=True,blank=True, verbose_name='Colección')
    creators = models.ManyToManyField('Creator', verbose_name='Creador', related_name='creators')
        
    def __str__(self):
        return self.nft_contract_addr
    class Meta:
        verbose_name = 'NFT'
        ordering = ['nft_contract_addr']

#Creator Class
class Creator(models.Model):
    creator_nickname = models.CharField("Nickname", max_length=200)
    
    def __str__(self):
        return self.creator_nickname
    class Meta:
        verbose_name = 'Creador'
        verbose_name_plural = 'Creadores'