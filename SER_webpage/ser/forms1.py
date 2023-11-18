from django import forms
from .models import *


class apform(forms.ModelForm):
    class Meta:
        model = apa
        fields = "__all__"