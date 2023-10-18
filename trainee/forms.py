from django import forms

from track.models import Track


class TraineeForm(forms.Form):
    name = forms.CharField(strip=True, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Enter your name"}))
    birth_date = forms.DateField(required=True, widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    track_id = forms.ChoiceField(choices=[(track.id, track.name) for track in Track.objects.all()], label='Track', widget=forms.Select(attrs={'class': 'form-select'}))
