from django.shortcuts import render
from django.contrib.auth.decorators import login_required

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


def ChatDetailView(request):
    context = {}
    return render(request, "chat/detail.html", context)