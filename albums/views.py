from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import redirect
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

from albums.forms.albums_form import AlbumsForm
from albums.models import Albums
from photos.models import Photos


# Create your views here.


class AlbumsView(PermissionRequiredMixin, LoginRequiredMixin, DetailView):
    model = Albums
    template_name = 'albums/albums_detail.html'
    context_object_name = 'album'

    def get_context_data(self, **kwargs):
        photos = Photos.objects.all()
        if self.object.author.pk != self.request.user.pk:
            kwargs['photos'] = photos.filter(Q(album_id=kwargs['object'].pk) & Q(private=False)).distinct().order_by(
                "-create_date")
        else:
            kwargs['photos'] = photos.filter(Q(album_id=kwargs['object'].pk)).distinct().order_by("-create_date")
        return super().get_context_data(**kwargs)

    def has_permission(self):
        return self.request.user == self.get_object().author or not self.get_object().private



class AlbumsCreateView(LoginRequiredMixin, CreateView):
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


class AlbumsUpdateView(PermissionRequiredMixin, UpdateView):
    model = Albums
    form_class = AlbumsForm
    template_name = "albums/albums_edit.html"
    permission_required = "albums.delete_albums"
    photo = Photos.objects.all()

    def form_valid(self, form):
        album = form.save(commit=False)
        if album.private:
            for photo in self.photo.all().filter(album__id=album.pk):
                photo.private = True
                photo.save()
        album.save()
        return redirect("albums:detail", pk=album.pk)

    def has_permission(self):
        return super().has_permission() or self.request.user == self.get_object().author

    def get_success_url(self):
        return reverse("albums:detail", kwargs={"pk": self.object.pk})


class AlbumsDeleteView(PermissionRequiredMixin, DeleteView):
    model = Albums
    template_name = "albums/albums_delete.html"
    context_object_name = 'album'
    success_url = reverse_lazy("photos:home")
    permission_required = "albums.delete_albums"

    def has_permission(self):
        return super().has_permission() or self.request.user == self.get_object().author
