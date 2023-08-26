from django.contrib.auth import get_user_model
from rest_framework import serializers

from albums.models import Albums
from photos.models import Photos


class AuthorModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["id", "username", "email"]


class PhotosSerializer(serializers.ModelSerializer):
    author = AuthorModelSerializer(read_only=True)

    def save(self, **kwargs):
        request = self.context['request']
        kwargs['comment_author'] = request.user
        super().save(**kwargs)

    class Meta:
        model = Photos
        fields = ['id', 'photo', 'author', 'title', 'album', 'private', 'favorites', 'create_date']
        read_only_fields = ("id", "author", 'album', 'favorites', "create_date")


class AlbumsSerializer(serializers.ModelSerializer):
    author = AuthorModelSerializer(read_only=True)

    def save(self, **kwargs):
        request = self.context['request']
        kwargs['author'] = request.user
        super().save(**kwargs)

    class Meta:
        model = Albums
        fields = ['id', 'author', 'title', 'discriptions', 'private', 'favorites', 'create_date']
        read_only_fields = ("id", "author", 'favorites', "create_date")

