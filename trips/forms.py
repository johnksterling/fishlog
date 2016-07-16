from django import forms

from .models import Trip
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class TripForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(TripForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        model = Trip
        fields = ('id', 'description', 'comments',
                  'trip_date', 'location', 'score', 'user')
        widgets = {
            'trip_date': forms.DateInput(attrs={'class': 'datepicker'}),
            'user': forms.HiddenInput(),
        }
