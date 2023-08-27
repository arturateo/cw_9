# Create your views here.
from django.http import HttpResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS
from rest_framework.response import Response
from rest_framework.views import APIView

from api_v1.permissions import IsAuthor
from api_v1.serializers import PhotosSerializer, AlbumsSerializer
from albums.models import Albums
from photos.models import Photos


@ensure_csrf_cookie
def get_csrf_token(request, *args, **kwargs):
    if request.method == "GET":
        return HttpResponse()
    return HttpResponseNotAllowed(['GET'])


class FavoritesPhotoViewSet(viewsets.ModelViewSet):
    queryset = Photos.objects.all()
    serializer_class = PhotosSerializer

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return []
        elif self.request.method == "POST":
            return [IsAuthenticated()]
        elif self.request.method is ['PUT', 'PATCH', 'DELETE']:
            return [IsAuthor()]
        return super().get_permissions()

    @action(methods=["POST"], detail=True, permission_classes=[IsAuthenticated], url_path="favorite",
            url_name="favorite")
    def add_favorite_photo(self, request, *args, **kwargs):
        photo = self.get_object()
        photo.favorites.add(request.user)
        return Response({"answer": "Фото добавлен в избраное"})

    @action(methods=["DELETE"], detail=True, permission_classes=[IsAuthenticated], url_path="unfavorite",
            url_name="unfavorite")
    def delete_favorite_photo(self, request, *args, **kwargs):
        photo = self.get_object()
        photo.favorites.remove(request.user)
        return Response({"answer": "Фото удален из избранного"})


class FavoritesAlbumViewSet(viewsets.ModelViewSet):
    queryset = Albums.objects.all()
    serializer_class = AlbumsSerializer

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return [IsAuthenticated()]
        elif self.request.method == "POST":
            return [IsAuthenticated()]
        elif self.request.method is ['PUT', 'PATCH', 'DELETE']:
            return [IsAuthor()]
        return super().get_permissions()

    @action(methods=["POST"], detail=True, permission_classes=[IsAuthenticated], url_path="favorite",
            url_name="favorite")
    def add_favorite_album(self, request, *args, **kwargs):
        album = self.get_object()
        album.favorites.add(request.user)
        return Response({"answer": "Альбом добавлен в избраное"})

    @action(methods=["DELETE"], detail=True, permission_classes=[IsAuthenticated], url_path="unfavorite",
            url_name="unfavorite")
    def delete_favorite_album(self, request, *args, **kwargs):
        album = self.get_object()
        album.favorites.remove(request.user)
        return Response({"answer": "Альбом удален из избранного"})


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request.user
        user.auth_token.delete()
        return Response({'status': 'ok'})
