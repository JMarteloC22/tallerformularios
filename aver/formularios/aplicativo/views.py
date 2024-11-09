from django.shortcuts import render
from .forms import MiFormulario

def formulario_vista(request):
    if request.method == 'POST':
        form = MiFormulario(request.POST, request.FILES)
        if form.is_valid():
            # Manejar los datos del formulario aquí
            archivo = form.cleaned_data['archivo']
            fecha_hora = form.cleaned_data['fecha_hora']
            # Guardar el archivo y procesar la fecha y hora
            return render(request, 'success.html')
    else:
        form = MiFormulario()
    return render(request, 'formulario.html', {'form': form})
