"""
Configuración principal de URLs del proyecto Visitas_empresa.

Este archivo es el punto de entrada principal para el enrutamiento
de URLs en todo el proyecto Django. Define las rutas de nivel superior
y delega a las aplicaciones específicas.

Estructura de URLs:
- /admin/ : Panel de administración de Django
- / : Todas las URLs de la aplicación registro_visitas
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # PANEL DE ADMINISTRACIÓN DE DJANGO
    # URL: http://dominio.com/admin/
    # Proporciona interfaz web para gestionar modelos y datos
    # Requiere superusuario creado con: python manage.py createsuperuser
    path('admin/', admin.site.urls),
    
    # APLICACIÓN PRINCIPAL: registro_visitas
    # URL base: http://dominio.com/
    # Incluye todas las URLs definidas en registro_visitas/urls.py
    # Esto permite que las rutas de la app sean accesibles desde la raíz
    path('', include('registro_visitas.urls')),
]