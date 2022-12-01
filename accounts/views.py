from django.shortcuts import render, redirect
from accounts.forms import CustomLoginForm, CustomUserCreationForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
# Create your views here.


class SignUpView(SuccessMessageMixin, CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("accounts:login")
    template_name = "accounts/signup.html"
    success_message: str = "User successfully created"
class UserLoginView(SuccessMessageMixin, LoginView):
    form_class = CustomLoginForm
    success_url = reverse_lazy("core:index")
    template_name: str = "accounts/login.html"
    success_message: str = "Login Successfull"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("core:index")
        return super(UserLoginView, self).dispatch(request, *args, **kwargs)