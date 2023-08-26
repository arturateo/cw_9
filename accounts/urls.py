from django.contrib.auth.views import LogoutView
from django.urls import path

from accounts.views import RegisterView, ProfileView, CustomLoginView

app_name = 'accounts'

urlpatterns = [
    path('accounts/login/', CustomLoginView.as_view(), name="login"),
    path('accounts/logout/', LogoutView.as_view(), name="logout"),
    path('accounts/register/', RegisterView.as_view(), name="register"),
    path('accounts/profile/<int:pk>', ProfileView.as_view(), name='profile'),
]
