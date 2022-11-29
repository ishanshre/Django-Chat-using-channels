from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model

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