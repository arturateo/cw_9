from django.urls import path

from photos.views import PhotosListView, PhotosView, PhotosCreateView, PhotosDeleteView, PhotosUpdateView, get_uniq_url, PhotosPrivateView

app_name = 'photos'

urlpatterns = [
    path('', PhotosListView.as_view(), name="home"),
    path('photo/<int:pk>/', PhotosView.as_view(), name="detail"),
    path('photo-create/', PhotosCreateView.as_view(), name="create"),
    path('photo-change/<int:pk>/', PhotosUpdateView.as_view(), name="change"),
    path('photo-delete/<int:pk>/', PhotosDeleteView.as_view(), name="delete"),
    path('photo-create-uniq_url/<int:pk>/', get_uniq_url, name="create_uniq_url"),
    path('photo-private/<slug:url>/', PhotosPrivateView.as_view(), name="private_detail"),
]
