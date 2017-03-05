from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from multiupload.fields import MultiImageField
from trips.models import Trip, TripPicture


class TripForm(forms.ModelForm):
    images = MultiImageField(min_num=1, max_num=3, max_file_size=1024*1024*5)

    def __init__(self, *args, **kwargs):
        super(TripForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        model = Trip
        fields = ('id', 'description', 'comments',
                  'trip_date', 'location', 'score', 'user')
        widgets = {
            'trip_date': forms.DateInput(attrs={'class': 'datepicker'}),
            'user': forms.HiddenInput(),
        }
