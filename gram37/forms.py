from .models import NewPost, Profile
from django import forms
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class PostForm(forms.Form):
    image = forms.ImageField()
    image_name = forms.CharField()
    image_caption = forms.CharField(widget=forms.Textarea())
    
    class Meta:
        model = NewPost
        fields = ['image']

class CommentForm(forms.Form):
    body = forms.CharField(widget = forms.TextInput(attrs = {"class": "form-control", "placeholder": "Leavea Comment"}))

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'bio']