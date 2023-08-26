from django import forms
from django.core.exceptions import ValidationError

from photos.models import Photos


class PhotosForm(forms.ModelForm):
    class Meta:
        model = Photos
        fields = ['title', 'photo', 'album', 'private']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['album'].queryset = self.fields['album'].queryset.filter(author=kwargs['initial']['user'])

        for field in iter(self.fields):
            if field != 'private':
                self.fields[field].widget.attrs.update({
                    'class': 'form-control'
                })

    def clean(self):
        if self.cleaned_data['album']:
            if self.cleaned_data['album'].private != self.cleaned_data['private'] and \
                    self.cleaned_data['private'] == True:
                raise ValidationError("Приватная фотография - не может быть в публичном альбоме")
            if self.cleaned_data['album'].private != self.cleaned_data['private'] and \
                    self.cleaned_data['private'] == False:
                raise ValidationError("В приватном альбоме - фотография не может быть публичной")
        return self.cleaned_data
