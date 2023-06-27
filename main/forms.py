from django import forms
from .models import ImageModel
from django.forms import formset_factory


class ImageForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = ['image']

ImageFormSet = formset_factory(form=ImageForm, extra=3)