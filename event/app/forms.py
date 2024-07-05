from django import forms
from .models import Event, Participant
from django.core.exceptions import ValidationError
import datetime


class EventForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Event
        fields = ['title', 'description', 'date', 'location', 'image']

    def clean_date(self):
        date = self.cleaned_data.get('date')
        now = datetime.date.today()
        if date < now:
            raise ValidationError("Дата должна быть в будущем")
        return date


class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['events']

