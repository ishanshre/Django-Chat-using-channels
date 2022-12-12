from django.db import models
from django.contrib.auth import get_user_model as User
# Create your models here.
class Message(models.Model):
    user = models.ForeignKey(User(), on_delete=models.CASCADE, related_name="messages")
    sender = models.ForeignKey(User(), on_delete=models.CASCADE, related_name="from_user")
    reciepient = models.ForeignKey(User(), on_delete=models.CASCADE, related_name="to_user")
    body = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_sent = models.BooleanField(default=False)
    is_read = models.BooleanField(default=False)

    # send message as you start the converstation
    def sender_message(from_user, to_user, body):
        sender_message = Message(
            user = from_user, # it is you
            sender = from_user, # it is you
            reciepient = to_user, # pass the message to
            body=body,
            is_send = True,
            is_read = True
        )
        sender_message.save()

        reciepient_message = Message(
            user = to_user,
            sender=from_user,
            reciepient = from_user,
            body = body,
            is_send=True,
            is_true=True
        )
        reciepient_message.save()
        return sender_message

    def get_message(user):
        users = []
        messages = Message.objects.filter(user=user).values("reciepient").annotate(last=models.Max("created")).order_by("-last")
        for message in messages:
            users.append({
                'user': User().objects.get(pk=message['reciepient']),
                'last': message['last'],
                'unread': Message.objects.filter(user=user, reciepient__pk=message['reciepient'], is_read=False)
            })
        return users
