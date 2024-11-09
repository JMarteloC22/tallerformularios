from django import forms

class MiFormulario(forms.Form):
    archivo = forms.FileField(label='Selecciona un archivo')
    fecha_hora = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        label='Selecciona una fecha y hora'
    )
