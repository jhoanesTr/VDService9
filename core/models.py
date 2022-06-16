from django.db import models

# Create your models here.
motivos_type = (
        (1, 'Instalacion nueva'),
        (2, 'Renovacion de instalacion'),
        (3, 'Mantenimiento'),
        (4, 'Emergencia'),
        (5, 'Reclamos'),
        (6, 'Otro'),
)
class ContactoModel(models.Model):
    Nombre = models.CharField(max_length=50)
    Email = models.EmailField(max_length=100,
                              blank=True)
    Telefono = models.CharField(max_length=9,
                                blank=True)
    Motivo = models.PositiveSmallIntegerField(choices=motivos_type)
    CP = models.PositiveIntegerField
    Comentario = models.CharField(max_length=240, blank=True)
    Disponibilidad = models.CharField(max_length=18)
    Fecha_Alta = models.DateField(auto_now=False, auto_now_add=True, null=True)
    Seguimiento = models.DateField(auto_now=True, auto_now_add=False)
