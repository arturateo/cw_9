# Generated by Django 4.2.4 on 2023-08-26 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0002_albums_favorites_alter_albums_private'),
        ('photos', '0004_photos_favorites_alter_photos_private'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photos',
            name='album',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='albums', to='albums.albums', verbose_name='Альбом'),
        ),
    ]