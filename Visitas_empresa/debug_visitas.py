#!/usr/bin/env python
import os
import sys
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Visitas_empresa.settings')
django.setup()

from registro_visitas.models import Visita
from django.utils import timezone

def debug_visitas():
    print("=== DEBUG DE VISITAS ===")
    
    # Obtener fecha actual
    hoy = timezone.now().date()
    print(f"Fecha de hoy (timezone.now().date()): {hoy}")
    print(f"Timezone actual: {timezone.get_current_timezone()}")
    print(f"Hora actual completa: {timezone.now()}")
    
    # Contar todas las visitas
    total_visitas = Visita.objects.all().count()
    print(f"\nTotal de visitas en BD: {total_visitas}")
    
    # Aplicar el mismo filtro que usa la vista
    visitas_hoy = Visita.objects.filter(hora_entrada__date=hoy)
    print(f"Visitas filtradas para hoy: {visitas_hoy.count()}")
    
    # Mostrar todas las visitas con detalles
    print("\n=== TODAS LAS VISITAS ===")
    for v in Visita.objects.all():
        fecha_visita = v.hora_entrada.date()
        es_hoy = fecha_visita == hoy
        print(f"- {v.nombre} ({v.rut})")
        print(f"  Hora entrada: {v.hora_entrada}")
        print(f"  Fecha: {fecha_visita}")
        print(f"  ¿Es hoy ({hoy})?: {es_hoy}")
        print()

if __name__ == "__main__":
    debug_visitas()