from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.contrib.auth import get_user_model

from accounts.forms import CustomUserChangeForm, CustomUserCreationForm


# local
from accounts.models import Profile

# Register your models here.


class ProfileInline(admin.StackedInline):
    model = Profile



@admin.register(get_user_model())
class UserAdmin(AuthUserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ['username','email','is_staff']
    fieldsets = AuthUserAdmin.fieldsets + (
        (
            "Additional Info", {
                "fields":("gender","date_of_birth","facebook","twitter"),
            }
        ),
    )
    add_fieldsets = (
        (
            "Create User",
            {
                "classes": ("wide",),
                "fields": ("username","email","password1","password2"),
            }
        ),
    )
    def get_inlines(self, request, obj=None):
        if obj:
            return [ProfileInline]
        else:
            return []

    