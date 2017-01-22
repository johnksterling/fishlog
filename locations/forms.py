from django import forms

from .models import Location
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class LocationForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(LocationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        model = Location
        fields = ('id', 'latitude', 'longitude', 'name', 'user')
        widgets = {
            'user': forms.HiddenInput(),
        }
