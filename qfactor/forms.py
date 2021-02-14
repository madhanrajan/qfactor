from django import forms

POLARISATION_CHOICES = [
    ('TE','TE'),
    ('TM','TM'),
    ('BOTH','BOTH')
]

class FormMain(forms.Form):
    initial_wavelength = forms.CharField(label="Wavelength range; Initial Value (in nm):", initial="400",widget=forms.TextInput(attrs={'type':'number'}))
    final_wavelength = forms.CharField(label="Wavelength range; Final Value (in nm):", initial="900", widget=forms.TextInput(attrs={'type':'number'}))
    initial_polarisation = forms.CharField(label="Polarisation range; Initial Value(in degrees):",initial="0",widget=forms.TextInput(attrs={'type':'number'}))
    final_polarisation = forms.CharField(label="Polarisation range; Final Value(in degrees):", initial="40",widget=forms.TextInput(attrs={'type':'number'}))
    polarisation = forms.CharField(label="Specify the polarisation:", widget=forms.Select(choices=POLARISATION_CHOICES))
    radius = forms.CharField(label="Radius (in nm):",initial="20",widget=forms.TextInput(attrs={'type':'number'}))
    height = forms.CharField(label="Height (in nm):",initial="200",widget=forms.TextInput(attrs={'type':'number'}))
    distance = forms.CharField(label="Distance (in nm):",initial="60",widget=forms.TextInput(attrs={'type':'number'}))
    number_of_layers = forms.CharField(widget=forms.TextInput(attrs={'type':'number'}))
