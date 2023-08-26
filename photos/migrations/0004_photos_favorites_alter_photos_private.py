# Generated by Django 4.2.4 on 2023-08-26 12:15

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('photos', '0003_alter_photos_private'),
    ]

    operations = [
        migrations.AddField(
            model_name='photos',
            name='favorites',
            field=models.ManyToManyField(related_name='favorites_photo', to=settings.AUTH_USER_MODEL, verbose_name='Избранное'),
        ),
        migrations.AlterField(
            model_name='photos',
            name='private',
            field=models.BooleanField(default=1, verbose_name='Приватное фото'),
            preserve_default=False,
        ),
    ]