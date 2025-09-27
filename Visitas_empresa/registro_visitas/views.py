from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Visita

def registrar_visita(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        rut = request.POST.get('rut')
        motivo = request.POST.get('motivo')

        # Validación básica
        if nombre and rut and motivo:
            Visita.objects.create(
                nombre=nombre,
                rut=rut,
                motivo=motivo
            )
            return redirect('lista_visitas')
        else:
            return render(request, 'registro_visitas/formulario_visita.html', {
                'error': 'Todos los campos son obligatorios.'
            })

    return render(request, 'registro_visitas/formulario_visita.html')

def lista_visitas(request):
    # Obtener visitas del día actual
    hoy = timezone.now().date()
    visitas = Visita.objects.filter(hora_entrada__date=hoy)
    return render(request, 'registro_visitas/lista_visitas.html', {
        'visitas': visitas
    })

def registrar_salida(request, visita_id):
    visita = Visita.objects.get(id=visita_id)
    visita.hora_salida = timezone.now()
    visita.save()
    return redirect('lista_visitas')