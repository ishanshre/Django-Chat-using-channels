from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from accounts.models import Profile
from core.models import Friend

User = get_user_model()

@receiver(signal=post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        profile = Profile.objects.create(user=instance)
        profile.save()

@receiver(signal=post_save, sender=Profile)
def save_profile(sender, instance, created, **kwargs):
    if created:    
        friend = Friend.objects.create(profile=instance)
        friend.save()

    