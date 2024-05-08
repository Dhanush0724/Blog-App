from django import forms
from .models import PostModel,ProfileModel,Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models


class PostModelForm(forms.ModelForm):
    
    content = forms.CharField(widget=forms.Textarea(attrs={'rows':4}))
    class Meta:
        model = PostModel
        fields = ('title', 'content')

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User 
        fields = ['username','email']
        

class ProfileUpdateForm(forms.ModelForm):

    class Meta :
        
        model = ProfileModel
        fields = ['image']
       



class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ('title', 'content')

class CommentForm(forms.ModelForm):
      content = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder':'add comment'}))
      class Meta:
          model = Comment
          fields = {'content',}

class SearchForm(forms.Form):
    query = forms.CharField(label='Search' , max_length=100)