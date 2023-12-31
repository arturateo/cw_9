from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.
class Photos(models.Model):
    photo = models.ImageField(null=False, blank=False, upload_to='photos', verbose_name='Фотография')
    author = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='author_photos',
                               verbose_name='Автор')
    title = models.CharField(null=False, blank=False, max_length=100, verbose_name='Подпись фотографии')
    album = models.ForeignKey('albums.Albums', on_delete=models.CASCADE, blank=True, null=True,
                              related_name='albums', verbose_name='Альбом')
    favorites = models.ManyToManyField(get_user_model(), related_name='favorites_photo', verbose_name='Избранное')
    private = models.BooleanField(null=False, blank=False, verbose_name='Приватное фото')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    uniq_url = models.CharField(max_length=32, null=False, blank=False, verbose_name="Уникальный url")

    class Meta:
        db_table = 'photos'
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'

    def __str__(self):
        return f'{self.title} {self.private}'
