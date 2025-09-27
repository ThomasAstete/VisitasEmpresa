from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Visita

def registrar_visita(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        rut = request.POST.get('rut')
        motivo = request.POST.get('motivo')

        if nombre and rut and motivo:
            # Usar timezone.now() que respeta la zona horaria de settings.py
            Visita.objects.create(
                nombre=nombre,
                rut=rut,
                motivo=motivo,
                hora_entrada=timezone.now()  # Usar timezone.now() en lugar de auto_now_add
            )
            return redirect('lista_visitas')
        else:
            return render(request, 'registro_visitas/formulario_visita.html', {
                'error': 'Todos los campos son obligatorios.',
                'current_date': timezone.localdate().strftime("%d/%m/%Y")
            })

    return render(request, 'registro_visitas/formulario_visita.html', {
        'current_date': timezone.localdate().strftime("%d/%m/%Y")
    })

def lista_visitas(request):
    # Usar timezone.localdate() para obtener la fecha local correcta
    hoy = timezone.localdate()
    
    visitas = Visita.objects.filter(hora_entrada__date=hoy)
    
    visitas_activas = visitas.filter(hora_salida__isnull=True).count()
    visitas_completadas = visitas.filter(hora_salida__isnull=False).count()
    
    return render(request, 'registro_visitas/lista_visitas.html', {
        'visitas': visitas,
        'visitas_activas': visitas_activas,
        'visitas_completadas': visitas_completadas,
        'current_date': timezone.localdate().strftime("%d/%m/%Y")
    })

def registrar_salida(request, visita_id):
    visita = Visita.objects.get(id=visita_id)
    visita.hora_salida = timezone.now()  # Usar timezone.now()
    visita.save()
    return redirect('lista_visitas')