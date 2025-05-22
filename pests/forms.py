from django import forms
from .models import Farm, SurveillanceSession, Observation
from django import forms
from pests.models import PlantPart

class FarmForm(forms.ModelForm):
    class Meta:
        model = Farm
        fields = ['location', 'num_plants', 'stocking_rate']

class SurveillanceSessionForm(forms.ModelForm):
    class Meta:
        model = SurveillanceSession
        fields = ['plant_type', 'date', 'time_of_day']

class ObservationForm(forms.ModelForm):
    class Meta:
        model = Observation
        fields = ['plant_part', 'pest', 'disease', 'result']

SEASON_CHOICES = [
    ('dry', 'Dry Season'),
    ('wet', 'Wet Season'),
]

class SurveillanceEffortForm(forms.Form):
    plant_count = forms.IntegerField(min_value=1, label="Number of Plants")
    season = forms.ChoiceField(choices=SEASON_CHOICES)
    plant_part = forms.ModelChoiceField(queryset=PlantPart.objects.all())