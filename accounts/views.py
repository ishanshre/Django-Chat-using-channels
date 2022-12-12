from django.shortcuts import render, redirect
from accounts.forms import CustomLoginForm, CustomUserCreationForm, UserProfileForm, CustomUserChangeForm
from accounts.models import Profile, User
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
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

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')
        if remember_me:
            self.request.session.set_expiry(300)
        return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("core:index")
        return super(UserLoginView, self).dispatch(request, *args, **kwargs)


class UserProfileView(LoginRequiredMixin, View):
    template_name = "accounts/profile.html"
    def get(self, request, *args, **kwargs):
        profile = Profile.objects.get(user=request.user)
        user_form = CustomUserChangeForm(instance=request.user)
        profile_form = UserProfileForm(instance=profile)
        context = {
            "user_form":user_form,
            "profile_form":profile_form,
            "profile": profile,
        }
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        profile = Profile.objects.get(user=request.user)
        user_form = CustomUserChangeForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect("accounts:profile")
        context = {
            "user_form":user_form,
            "profile_form":profile_form,
            "profile": profile,
        }
        return render(request, self.template_name, context)

        
