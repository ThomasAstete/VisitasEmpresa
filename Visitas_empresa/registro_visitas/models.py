from django.db import models

class Visita(models.Model):
<<<<<<< HEAD
    nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=12)
    motivo = models.TextField()
    hora_entrada = models.DateTimeField(auto_now_add=True)
    hora_salida = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} ({self.rut})"
=======
    """
    Modelo de datos para el registro de visitas a la empresa.
    
    Este modelo define la estructura de la tabla en la base de datos
    que almacena la información de cada visitante y su visita.
    
    Características implementadas:
    - Registro automático de timestamp de entrada
    - Campo opcional para timestamp de salida
    - Validación de RUT en la capa de vista
    - Representación string legible del objeto
    
    Tabla generada: registro_visitas_visita
    """
    
    # CAMPO: Nombre completo del visitante
    # CharField para strings de longitud limitada
    # max_length=100 permite nombres completos largos
    nombre = models.CharField(
        max_length=100,
        verbose_name="Nombre completo",
        help_text="Nombre y apellido del visitante"
    )
    
    # CAMPO: RUT chileno del visitante  
    # max_length=12 permite formato "12345678-9" con espacios extra
    # La validación del formato se realiza en views.py
    rut = models.CharField(
        max_length=12,
        verbose_name="RUT",
        help_text="RUT chileno en formato 12345678-9"
    )
    
    # CAMPO: Motivo o propósito de la visita
    # TextField para texto de longitud variable sin límite
    motivo = models.TextField(
        verbose_name="Motivo de la visita", 
        help_text="Descripción del propósito de la visita"
    )
    
    # CAMPO: Timestamp de entrada (CHECK-IN)
    # auto_now_add=True hace que Django establezca automáticamente 
    # la fecha y hora actual cuando se crea el registro
    # Este campo no puede ser modificado después de la creación
    hora_entrada = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Hora de entrada",
        help_text="Timestamp automático al registrar la visita"
    )
    
    # CAMPO: Timestamp de salida (CHECK-OUT)
    # null=True permite valores NULL en la base de datos
    # blank=True permite que el campo esté vacío en formularios Django
    # Este campo se completa cuando el visitante registra su salida
    hora_salida = models.DateTimeField(
        null=True, 
        blank=True,
        verbose_name="Hora de salida",
        help_text="Timestamp de salida del visitante (opcional)"
    )

    def __str__(self):
        """
        Método especial para representación string del objeto.
        
        Se utiliza en:
        - Django Admin para mostrar objetos en listas
        - Shell de Django para debugging
        - Cualquier lugar donde se necesite una representación legible
        
        Returns:
            str: Formato "Nombre (RUT) - Fecha"
            
        Ejemplo: "Juan Pérez (12345678-9) - 2025-09-26"
        """
        return f"{self.nombre} ({self.rut}) - {self.hora_entrada.date()}"
    
    class Meta:
        """
        Configuración de metadatos del modelo.
        
        Define comportamientos adicionales y configuraciones
        que no son campos específicos del modelo.
        """
        # Nombre singular y plural para Django Admin
        verbose_name = "Visita"
        verbose_name_plural = "Visitas"
        
        # Ordenamiento por defecto: más recientes primero
        ordering = ['-hora_entrada']
        
        # Índices para mejorar rendimiento de consultas
        indexes = [
            models.Index(fields=['hora_entrada']),  # Para filtros por fecha
            models.Index(fields=['rut']),           # Para búsquedas por RUT
        ]
>>>>>>> parent of 925713c (correcciones menores)
