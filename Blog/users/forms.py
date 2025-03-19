from django import forms
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.forms import UserCreationForm
from .models import User

class createuser(UserCreationForm):
    class Meta:
        model = User
        fields = ['email','username']


class loginform(forms.Form):
    email = forms.EmailField()
    password = forms.CharField()

# class profil_edit(forms.Form):
#     username = forms.CharField(max_lenght=100)
#     # email = forms.EmailField(unique=True)
#     about = forms.Textarea()
#     photo = forms.ImageField()


class EditProfile(forms.Form):
    username = forms.CharField(max_length=100)
    about = forms.CharField()
    photo = forms.ImageField()
   
    def __init__(self,original,*args,**kwargs):
          super().__init__(*args,**kwargs)
          self.original = original
    
    def clean_username(self):
        username = self.cleaned_data['username']
        if username != self.original:
            if User.objects.filter(username = username).exists():
                raise forms.ValidationError('username already exists')
        return username
   
    




  