from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django import forms

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['first_name','last_name','username','email']


class CustomUserChangeForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','gender','date_of_birth','facebook','twitter']


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput, max_length=255, required=True)
    password = forms.CharField(max_length=255, widget=forms.PasswordInput)
    remember_me = forms.BooleanField(required=False, initial=False)
    
    class Meta:
        model = User
        fields = ["username","password","remember_me"]
