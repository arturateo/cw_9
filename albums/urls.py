from django.urls import path

from albums.views import AlbumsView, AlbumsCreateView, AlbumsDeleteView, AlbumsUpdateView

app_name = 'albums'

urlpatterns = [
    path('album/<int:pk>/', AlbumsView.as_view(), name="detail"),
    path('album-create/', AlbumsCreateView.as_view(), name="create"),
    path('album-change/<int:pk>/', AlbumsUpdateView.as_view(), name="change"),
    path('album-delete/<int:pk>/', AlbumsDeleteView.as_view(), name="delete"),
]
