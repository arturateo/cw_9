from django import forms

from albums.models import Albums


class AlbumsForm(forms.ModelForm):
    class Meta:
        model = Albums
        fields = ['title', 'discriptions', 'private']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            if field != 'private':
                self.fields[field].widget.attrs.update({
                    'class': 'form-control'
                })
