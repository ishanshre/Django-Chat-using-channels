from django.shortcuts import render

# Create your views here.
def ChatListView(request):
    return render(request, "index.html")


def ChatDetailView(request):
    context = {}
    return render(request, "chat/detail.html", context)