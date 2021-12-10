import pathlib
import uuid
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.urls import reverse

# Create your models here.

# Colection Class
class Collection(models.Model):
    collection_name = models.CharField("Colección", max_length=200)
    
    def collection_upload_img_url(instance, filename):
        fpath = pathlib.Path(filename)
        new_fname = str(uuid.uuid1()) # uuid1 -> uuid + timestamps
        return f"collection/{new_fname}{fpath.suffix}"
    
    collection_image = models.ImageField("Collection's image", null=True, blank=True, upload_to=collection_upload_img_url, max_length = 256)
    
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    nfts = models.ManyToManyField('NFT', verbose_name='NFT', related_name='nfts')
    
    def get_nfts(self):
        return ", ".join([n.nft_contract_addr for n in self.nfts.all()])
    
    get_nfts.short_description = 'NFTs'
    
    def get_url(self):
        return reverse("collection", kwargs={"collection_pk": self.collection_name})
    
    def __str__(self):
        return self.collection_name
    class Meta:
        verbose_name = 'Colección'
        verbose_name_plural = 'Colecciones'
        ordering = ['-created','-updated']

#NFT Class
class NFT(models.Model):
    nft_contract_addr = models.CharField("Contract Address", max_length=256)
    nft_name = models.CharField("Token Name", max_length=200, null=True, blank=True)
    nft_id = models.CharField("Token Id", max_length=5)
    nft_standard = models.CharField("Token Standard", max_length=10)
    nft_blockchain = models.CharField("Blockchain", max_length=100)
    
    def nft_upload_img_url(instance, filename):
        fpath = pathlib.Path(filename)
        new_fname = str(uuid.uuid1()) # uuid1 -> uuid + timestamps
        return f"nft/{new_fname}{fpath.suffix}"
    
    nft_image = models.ImageField("NFT's image", null=True, blank=True, upload_to=nft_upload_img_url, max_length = 256)
     
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    collection_name = models.ForeignKey('Collection', on_delete=models.SET_NULL, null=True,blank=True)
    creators = models.ManyToManyField('Creator', related_name='creators')
    
    def get_creators(self):
        return ", ".join([c.creator_nickname for c in self.creators.all()])
    
    def get_url(self):
        return reverse("nft", kwargs={"collection_pk": self.collection_name, "nft_pk":self.nft_id})
    
    def __str__(self):
        return self.nft_contract_addr
    
    class Meta:
        verbose_name = 'NFT'
        ordering = ['-created','-updated']

#Creator Class
class Creator(models.Model):
    creator_nickname = models.CharField("Nickname", max_length=200)
    
    def __str__(self):
        return self.creator_nickname
    class Meta:
        verbose_name = 'Creador'
        verbose_name_plural = 'Creadores'

#User Profile
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    
    def profile_pic_upload_img_url(instance, filename):
        fpath = pathlib.Path(filename)
        new_fname = str(uuid.uuid1()) # uuid1 -> uuid + timestamps
        return f"user_pic/{new_fname}{fpath.suffix}"
    
    user_pic = models.ImageField("Profile picture", null=True, blank=True, upload_to=profile_pic_upload_img_url, max_length = 256)
    
    def __str__(self) :
        return f'{self.user.username}'
    
    class Meta:
        verbose_name = 'profile'
    
@receiver(post_save, sender=User)
def update_profile(sender, instance, created, **kwards):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):      
    instance.profile.save()