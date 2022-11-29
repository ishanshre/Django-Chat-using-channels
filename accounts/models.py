from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
# Create your models here.

class User(AbstractUser):
    class GENDER_CHOICE(models.TextChoices):
        MALE = "M", 'Male'
        FEMALE = "F", 'Female'
        OTHERS = "O", 'Others'
    
    email = models.EmailField(_("email address"),max_length=50, unique=True)
    gender = models.CharField(_("gender"),max_length=1, null=True, blank=True)
    date_of_birth = models.DateField(_("date of birth"),null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    


