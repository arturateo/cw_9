from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accounts.views import RegisterView, ProfileView

app_name = 'accounts'

urlpatterns = [
    path('accounts/login/', LoginView.as_view(template_name='accounts/login.html'), name="login"),
    path('accounts/logout/', LogoutView.as_view(), name="logout"),
    path('accounts/register/', RegisterView.as_view(), name="register"),
    path('accounts/profile/<int:pk>', ProfileView.as_view(), name='profile'),
]
