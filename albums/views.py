from django.shortcuts import render

# Create your views here.
from urllib.parse import urlencode

from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import redirect
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

from albums.forms.albums_form import AlbumsForm
from albums.models import Albums
from photos.models import Photos


# Create your views here.


class AlbumsView(DetailView):
    model = Albums
    template_name = 'albums/albums_detail.html'
    context_object_name = 'album'

    def get_context_data(self, **kwargs):
        photos = Photos.objects.all().filter(album_id=kwargs['object'].pk).order_by("-create_date",)
        kwargs['photos'] = photos
        return super().get_context_data(**kwargs)

class AlbumsCreateView(CreateView):
    model = Albums
    form_class = AlbumsForm
    template_name = 'albums/albums_create.html'

    def form_valid(self, form):
        album = form.save(commit=False)
        album.author = self.request.user
        album.save()
        return redirect("albums:detail", pk=album.pk)

    def get_success_url(self):
        return reverse("albums:detail", kwargs={"pk": self.object.pk})


class AlbumsUpdateView(UpdateView):
    model = Albums
    form_class = AlbumsForm
    template_name = "albums/albums_edit.html"

    def get_success_url(self):
        return reverse("albums:detail", kwargs={"pk": self.object.pk})


class AlbumsDeleteView(DeleteView):
    model = Albums
    template_name = "albums/albums_delete.html"
    context_object_name = 'album'
    success_url = reverse_lazy("photos:home")
