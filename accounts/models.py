from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# third party
from phonenumber_field.modelfields import PhoneNumberField

# local
from accounts.countries import COUNTRIES_CHOOSE


# Create your models here.

class User(AbstractUser):
    class GENDER_CHOICE(models.TextChoices):
        MALE = "M", 'Male'
        FEMALE = "F", 'Female'
        OTHERS = "O", 'Others'
    
    email = models.EmailField(_("email address"),max_length=50, unique=True)
    gender = models.CharField(_("gender"),max_length=1, choices=GENDER_CHOICE.choices, null=True, blank=True)
    date_of_birth = models.DateField(_("date of birth"),null=True, blank=True)
    facebook = models.URLField(_("facebook address"), null=True, blank=True)
    twitter = models.URLField(_("twitter address"), null=True, blank=True)
    
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    avatar = models.ImageField(_("avatar"), upload_to="user/profile", default="default.png")
    bio = models.TextField(_("bio"), max_length=500, null=True, blank=True)
    phone = PhoneNumberField(_("phone number") ,null=True, blank=True)
    street_address = models.CharField(_("street address"), max_length=100, null=True, blank=True)
    city = models.CharField(_("city"), max_length=100, null=True, blank=True)
    country = models.CharField(_("country"), max_length=40, choices=COUNTRIES_CHOOSE.choices, null=True, blank=True)
    friends = models.ManyToManyField('core.Friend', related_name="my_friends", blank=True)

    def __str__(self):
        return self.user.username



