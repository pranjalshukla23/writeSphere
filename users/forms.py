from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

# custom form 1
class UserRegisterForm(UserCreationForm):
    # define extra fields which you want in the form, other than the default fields
    email = forms.EmailField()
    
    class Meta:
        # store the data in User model
        model = User
        # define the fields which you want in the form
        fields = ["username", "email", "password1", "password2"]
     
# custom form 2   
class UserUpdateForm(forms.ModelForm):
     # define extra fields which you want in the form, other than the default fields
    email = forms.EmailField()
    
    class Meta:
        # store the data in User model
        model = User
        # define the fields which you want in the form
        fields = ["username", "email"]
    
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        # store data in profile model
        model = Profile
        # define the fields which you want in the form
        fields = ["image"]
    