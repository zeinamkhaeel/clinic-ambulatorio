from django import forms
from .models import Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        widgets = {
            'data_nascita': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'data_arrivo_italia': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'prima_visita': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'terapia': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'motivo_visita': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'esame_obiettivo': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'programma': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'diario_clinico': forms.Textarea(attrs={'rows': 6, 'class': 'form-control'}),
            'allergie': forms.Textarea(attrs={'rows': 2, 'class': 'form-control'}),
        }
