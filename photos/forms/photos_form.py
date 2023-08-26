from django import forms
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
