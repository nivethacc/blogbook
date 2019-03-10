from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()  # additional field

    # specify the model for this form to interact with.
    # Whenever the form validates,it is going to create a new user.Hence model is user
    # Class Meta gives us a nested namespace for configurations and keeps the config in one place
    # config =>model which is going to get affected is User model when form.save()
    class Meta:
        model = User
        # These field are going to be snown on the form
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        # These field are going to be snown on the form
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    #No additional field here.SO directly to Meta
    class Meta :
        model = Profile
        fields = ['image']