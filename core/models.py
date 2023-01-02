from django.db import models

from accounts.models import Profile


class Friend(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name='friends')
    def __str__(self):
        return self.profile.user.username

# Create your models here.
class Message(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="sender")
    receiver = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="receiver")
    body = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.body
