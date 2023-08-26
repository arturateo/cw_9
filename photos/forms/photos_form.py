from django import forms
from django.core.exceptions import ValidationError

from photos.models import Photos


class PhotosForm(forms.ModelForm):
    class Meta:
        model = Photos
        fields = ['title', 'photo', 'album', 'private']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            if field != 'private':
                self.fields[field].widget.attrs.update({
                    'class': 'form-control'
                })

    def clean_private(self):
        cleaned_data = super().clean()
        private = cleaned_data.get('private')
        album = cleaned_data.get('album')
        if album.private != private:
            raise ValidationError("В приватном альбоме - фотография не может быть публичной")
        return True
