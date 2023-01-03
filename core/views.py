from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from core.models import Friend, Message
from core.forms import ChatBodyMessage

from accounts.models import Profile

# Create your views here.
@login_required
def ChatListView(request):
    profile = request.user.profile
    friends = profile.friends.all()
    context = {
        'profile':profile,
        'friends':friends,
    }
    return render(request, "index.html", context)

@login_required
def ChatDetailView(request, pk):
    friend = Friend.objects.get(profile_id=pk)
    friend_profile = Profile.objects.get(id=friend.profile.id)
    sender_profile = request.user.profile
    chatMessages = Message.objects.filter(Q(
        sender = sender_profile,
        receiver = friend_profile,
        is_read=False
    ) | Q(
        sender = friend_profile,
        receiver = sender_profile,
        is_read=False
    )
    ).order_by("created")
    form = ChatBodyMessage()
    if request.method == "POST":
        form = ChatBodyMessage(request.POST)
        if form.is_valid():
            chat_message = form.save(commit=False)
            chat_message.sender = sender_profile
            chat_message.receiver = friend_profile
            chat_message.save()
            
            return redirect("core:chat_detail", pk=pk)
    context = {
        'friend':friend,
        'friend_profile':friend_profile,
        'sender_profile':sender_profile,
        'form':form,
        'chatMessages':chatMessages
    }
    return render(request, "chat/detail.html", context)