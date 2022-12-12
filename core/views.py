from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from core.models import Message
# Create your views here.


@login_required
def home(request):
    user=request.user
    messages = Message.get_message(user=user)
    active_direct = None
    directs = None
    if messages:
        message = messages[0]
        active_direct = message['user'].username
        directs = Message.objects.filter(user=request.user, reciepient=message['user'])
        directs.update(is_read=True)

        for message in messages:
            if message['user'].username == active_direct:
                message['unread'] = 0
    context = {
        'messages':messages,
        'directs':directs,
        'user':user,
        'active_direct':active_direct
    }
    return render(request, "index.html", context=context)

@login_required
def Directs(request, username):
    user = request.user
    messages = Message.get_message(user=user)
    active_directs = username
    directs = Message.objects.filter(user=user, reciepient__username=username)
    directs.update(is_read=True)
    for message in messages:
        if message['user'].username == username:
            message['unread'] = 0
    context = {
        'messages': message,
        'directs':directs,
        'user':user,
        'active_directs':active_directs,
    }
    return render(request, "index.html", context=context)