from urllib.parse import urlencode

from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import redirect
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

from photos.models import Photos


# Create your views here.
class PhotosList(ListView):
    model = Photos
    template_name = 'photos/photos_list.html'
    context_object_name = 'photos'
    ordering = ("-create_date",)


