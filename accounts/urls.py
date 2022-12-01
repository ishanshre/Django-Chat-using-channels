from django.urls import path
from accounts import views


app_name = "accounts"
urlpatterns = [
    path("accounts/register", views.SignUpView.as_view(), name='signup'),
    path("accounts/login", views.UserLoginView.as_view(), name='login'),
]