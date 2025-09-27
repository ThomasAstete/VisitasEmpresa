from django.urls import path
from . import views

"""
Configuración de URLs para la aplicación registro_visitas.

Este archivo define el mapeo entre URLs y las vistas correspondientes.
Implementa el patrón URL -> Vista -> Template de Django.

URLs disponibles:
- / : Página principal con formulario de registro
- /lista/ : Dashboard con listado de visitas del día
- /salida/<id>/ : Endpoint para registrar salida de una visita específica
"""

urlpatterns = [
    # RUTA PRINCIPAL: Formulario de registro de nuevas visitas
    # URL: http://dominio.com/
    # Vista: registrar_visita (GET: muestra formulario, POST: procesa datos)
    # Nombre: usado en templates con {% url 'registrar_visita' %}
    path('', views.registrar_visita, name='registrar_visita'),
    
    # RUTA: Dashboard de visitas del día actual
    # URL: http://dominio.com/lista/
    # Vista: lista_visitas (muestra tabla con estadísticas)
    # Nombre: usado en templates con {% url 'lista_visitas' %}
    path('lista/', views.lista_visitas, name='lista_visitas'),
    
    # RUTA: Endpoint para registrar salida de visitantes
    # URL: http://dominio.com/salida/123/ (donde 123 es el ID de la visita)
    # Vista: registrar_salida (actualiza hora_salida y redirige)
    # Parámetro: <int:visita_id> captura el ID como entero
    # Nombre: usado en templates con {% url 'registrar_salida' visita.id %}
    path('salida/<int:visita_id>/', views.registrar_salida, name='registrar_salida'),
]