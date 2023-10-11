from django import forms

class FormDalsitabulka(forms.Form):
    pet = forms.CharField(label="uveďte mazlíčka")
    sex = forms.CharField(label="uveďte pohlaví")