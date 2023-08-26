from django.urls import path

from photos.views import PhotosListView, PhotosView, PhotosCreateView, PhotosDeleteView, PhotosUpdateView

app_name = 'photos'

urlpatterns = [
    path('', PhotosListView.as_view(), name="home"),
    path('photo/<int:pk>/', PhotosView.as_view(), name="detail"),
    path('photo-create/', PhotosCreateView.as_view(), name="create"),
    path('photo-change/<int:pk>/', PhotosUpdateView.as_view(), name="change"),
    path('photo-delete/<int:pk>/', PhotosDeleteView.as_view(), name="delete"),
]
