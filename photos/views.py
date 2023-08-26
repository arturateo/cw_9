from urllib.parse import urlencode

from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import redirect
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

from photos.forms.photos_form import PhotosForm
from photos.models import Photos


# Create your views here.
class PhotosListView(ListView):
    model = Photos
    template_name = 'photos/photos_list.html'
    context_object_name = 'photos'
    ordering = ("-create_date",)


class PhotosView(DetailView):
    model = Photos
    template_name = 'photos/photos_detail.html'
    context_object_name = 'photo'


class PhotosCreateView(CreateView):
    model = Photos
    form_class = PhotosForm
    template_name = 'photos/photos_create.html'

    def form_valid(self, form):
        photo = form.save(commit=False)
        photo.author = self.request.user
        photo.save()
        return redirect("photos:detail", pk=photo.pk)

    def get_success_url(self):
        return reverse("photos:detail", kwargs={"pk": self.object.pk})


class PhotosUpdateView(UpdateView):
    model = Photos
    form_class = PhotosForm
    template_name = "photos/photos_edit.html"

    def get_success_url(self):
        return reverse("photos:detail", kwargs={"pk": self.object.pk})


class PhotosDeleteView(DeleteView):
    model = Photos
    template_name = "photos/photos_delete.html"
    context_object_name = 'photo'
    success_url = reverse_lazy("photos:home")
