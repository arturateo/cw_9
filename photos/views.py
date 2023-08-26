from urllib.parse import urlencode

from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import redirect
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

from albums.models import Albums
from photos.forms.photos_form import PhotosForm
from photos.models import Photos


# Create your views here.
class PhotosListView(ListView):
    model = Photos
    template_name = 'photos/photos_list.html'
    context_object_name = 'photos'
    ordering = ("-create_date",)

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        if request.user.is_authenticated:
            response.set_cookie('token', request.user.auth_token.key)
        return response

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(Q(private=False))
        return queryset


class PhotosView(PermissionRequiredMixin, LoginRequiredMixin, DetailView):
    model = Photos
    template_name = 'photos/photos_detail.html'
    context_object_name = 'photo'

    def has_permission(self):
        return self.request.user == self.get_object().author or not self.get_object().private


class PhotosCreateView(LoginRequiredMixin, CreateView):
    model = Photos
    form_class = PhotosForm
    template_name = 'photos/photos_create.html'

    def get_form_kwargs(self):
        kw = super().get_form_kwargs()
        kw['initial'] = {"user": self.request.user}
        return kw

    def form_valid(self, form):
        print(2)
        photo = form.save(commit=False)
        photo.author = self.request.user
        photo.save()
        return redirect("photos:detail", pk=photo.pk)

    def get_success_url(self):
        print(1)
        return reverse("photos:detail", kwargs={"pk": self.object.pk})


class PhotosUpdateView(PermissionRequiredMixin, UpdateView):
    model = Photos
    form_class = PhotosForm
    template_name = "photos/photos_edit.html"
    permission_required = "photos.change_photos"

    def get_form_kwargs(self):
        kw = super().get_form_kwargs()
        kw['initial'] = {"user": self.request.user}
        return kw

    def form_valid(self, form):
        photo = form.save(commit=False)
        photo.save()
        return redirect("photos:detail", pk=photo.pk)

    def get_success_url(self):
        return reverse("photos:detail", kwargs={"pk": self.object.pk})

    def has_permission(self):
        return super().has_permission() or self.request.user == self.get_object().author


class PhotosDeleteView(PermissionRequiredMixin, DeleteView):
    model = Photos
    template_name = "photos/photos_delete.html"
    context_object_name = 'photo'
    success_url = reverse_lazy("photos:home")
    permission_required = "photos.delete_photos"

    def has_permission(self):
        return super().has_permission() or self.request.user == self.get_object().author
