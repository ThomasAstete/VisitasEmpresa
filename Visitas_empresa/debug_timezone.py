#!/usr/bin/env python
import os
import sys
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Visitas_empresa.settings')
django.setup()

from registro_visitas.models import Visita
from django.utils import timezone
from django.db import connection
import datetime

def debug_timezone_issue():
    print("=== DEBUG DETALLADO DE TIMEZONE ===")
    
    # Información de timezone
    print(f"USE_TZ en settings: {django.conf.settings.USE_TZ}")
    print(f"TIME_ZONE en settings: {django.conf.settings.TIME_ZONE}")
    print(f"Timezone actual de Django: {timezone.get_current_timezone()}")
    
    # Obtener fecha actual de varias formas
    hoy_timezone = timezone.now().date()
    hoy_naive = datetime.date.today()
    
    print(f"\nFecha con timezone.now().date(): {hoy_timezone}")
    print(f"Fecha con datetime.date.today(): {hoy_naive}")
    
    # Probar diferentes tipos de filtros
    print(f"\n=== PROBANDO FILTROS ===")
    
    # Filtro original
    q1 = Visita.objects.filter(hora_entrada__date=hoy_timezone)
    print(f"hora_entrada__date={hoy_timezone}: {q1.count()} resultados")
    
    # Filtro con fecha naive
    q2 = Visita.objects.filter(hora_entrada__date=hoy_naive)
    print(f"hora_entrada__date={hoy_naive}: {q2.count()} resultados")
    
    # Filtro por rango de fechas
    inicio_dia = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)
    fin_dia = timezone.now().replace(hour=23, minute=59, second=59, microsecond=999999)
    q3 = Visita.objects.filter(hora_entrada__gte=inicio_dia, hora_entrada__lte=fin_dia)
    print(f"Rango de hoy ({inicio_dia} - {fin_dia}): {q3.count()} resultados")
    
    # Probar con timezone.localdate()
    try:
        hoy_local = timezone.localdate()
        q4 = Visita.objects.filter(hora_entrada__date=hoy_local)
        print(f"hora_entrada__date={hoy_local} (localdate): {q4.count()} resultados")
    except:
        print("No se pudo usar timezone.localdate()")
    
    # Ver SQL generado
    print(f"\n=== SQL GENERADO ===")
    print("Query 1 SQL:")
    print(str(q1.query))
    
    # Información de la BD
    print(f"\n=== INFO BASE DE DATOS ===")
    with connection.cursor() as cursor:
        cursor.execute("SELECT datetime('now');")
        db_time = cursor.fetchone()[0]
        print(f"Hora en BD SQLite: {db_time}")

if __name__ == "__main__":
    debug_timezone_issue()