from django.urls import path
from core import views

app_name = "core"

urlpatterns = [
    path('',views.ChatListView, name="index"),
    path('<int:pk>/detail', views.ChatDetailView, name="chat_detail")
]

