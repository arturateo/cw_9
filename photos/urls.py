from django.urls import path

from photos.views import PhotosList

app_name = 'topics'

urlpatterns = [
    path('', PhotosList.as_view(), name="photos"),
]
