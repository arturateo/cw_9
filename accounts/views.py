from django.contrib.auth import login, get_user_model
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView, DetailView
from accounts.forms import CustomRegisterForm
from accounts.models import User
from photos.models import Photos


# Create your views here.
class RegisterView(CreateView):
    model = get_user_model()
    template_name = 'accounts/register.html'
    form_class = CustomRegisterForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.get_success_url())

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if not next_url:
            next_url = self.request.POST.get('next')
        if not next_url:
            next_url = reverse('photos:home')
        return next_url


class ProfileView(DetailView):
    template_name = 'accounts/profile.html'
    queryset = User.objects.all()
    context_object_name = 'profile_user'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        photos = Photos.objects.all()
        context['photos'] = photos.filter(author__pk=self.object.pk).distinct()
        return context
