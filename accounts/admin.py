from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.contrib.auth import get_user_model

from accounts.forms import CustomUserChangeForm, CustomUserCreationForm

# Register your models here.


@admin.register(get_user_model())
class UserAdmin(AuthUserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ['username','email','is_staff']
    fieldsets = AuthUserAdmin.fieldsets + (("Additional Info", {"fields":("gender","date_of_birth","facebook","twitter"),}),)
    add_fieldsets = AuthUserAdmin.add_fieldsets + (("Additional Info", {"fields":("gender","date_of_birth","facebook","twitter"),}),)
