from django.contrib.auth import login, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView, DetailView
from accounts.forms import CustomRegisterForm
from accounts.models import User
from albums.models import Albums
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


class ProfileView(LoginRequiredMixin, DetailView):
    template_name = 'accounts/profile.html'
    model = User
    context_object_name = 'profile_user'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        photos = Photos.objects.all()
        albums = Albums.objects.all()
        if self.object.pk != self.request.user.pk:
            context['photos'] = photos.filter(Q(author__pk=self.object.pk) & Q(private=False)).distinct()
            context['albums'] = albums.filter(Q(author__pk=self.object.pk) & Q(private=False)).distinct()
        else:
            context['photos'] = photos.filter(Q(author__pk=self.object.pk)).distinct()
            context['albums'] = albums.filter(Q(author__pk=self.object.pk)).distinct()
        return context
