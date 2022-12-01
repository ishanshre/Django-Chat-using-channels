from django.urls import path
from accounts import views
from django.contrib.auth.views import LogoutView


app_name = "accounts"
urlpatterns = [
    path("register/", views.SignUpView.as_view(), name='signup'),
    path("login/", views.UserLoginView.as_view(), name='login'),
    path("logout/", LogoutView.as_view(), name='logout'),
]