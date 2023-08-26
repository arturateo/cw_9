from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.
class Albums(models.Model):
    author = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='author_albums',
                               verbose_name='Автор')
    title = models.CharField(null=False, blank=False, max_length=100, verbose_name='Название альбома')
    discriptions = models.TextField(null=True, blank=True, max_length=300, verbose_name='Описание альбома')
    private = models.BooleanField(null=False, blank=False, verbose_name='Приватный альбом')
    favorites = models.ManyToManyField(get_user_model(), related_name='favorites_album', verbose_name='Избранное')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        db_table = 'albums'
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'


    def __str__(self):
        return f'{self.title}'
