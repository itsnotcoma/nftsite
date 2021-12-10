from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, fields
from .models import Collection, NFT, Creator, Profile

class NftForm(ModelForm):
    class Meta:
        model = NFT
        fields = '__all__'

class CollectionForm(ModelForm):
    class Meta:
        model = Collection
        fields = '__all__'
        
class CreatorForm(ModelForm):
    class Meta:
        model = Creator
        fields = '__all__'

class SingupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        # fields = '__all__'

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['user_pic']